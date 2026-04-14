from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Category, Cart, CartItem, Order, OrderItem, Wishlist, Review
from .forms import CheckoutForm, RegisterForm, UserEditForm
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def _get_cart(request):
    """Get or create a cart for the current user/session."""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart


def home(request):
    product_list = Product.objects.filter(available=True)
    paginator = Paginator(product_list, 8)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    cart = _get_cart(request)
    context = {
        'products': products,
        'categories': categories,
        'cart': cart,
    }
    return render(request, 'store/index.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    related = Product.objects.filter(category=product.category, available=True).exclude(id=product.id)[:4]
    cart = _get_cart(request)
    context = {
        'product': product,
        'related_products': related,
        'cart': cart,
    }
    return render(request, 'store/product_detail.html', context)


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    product_list = Product.objects.filter(category=category, available=True)
    paginator = Paginator(product_list, 8)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    cart = _get_cart(request)
    context = {
        'category': category,
        'products': products,
        'categories': categories,
        'cart': cart,
    }
    return render(request, 'store/category.html', context)


def search(request):
    query = request.GET.get('q', '')
    product_list = Product.objects.filter(name__icontains=query, available=True) if query else Product.objects.none()
    paginator = Paginator(product_list, 8)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    cart = _get_cart(request)
    context = {
        'products': products,
        'categories': categories,
        'cart': cart,
        'query': query,
    }
    return render(request, 'store/search.html', context)


def cart_view(request):
    cart = _get_cart(request)
    context = {'cart': cart}
    return render(request, 'store/cart.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = _get_cart(request)
    size = request.POST.get('size', 'M')
    item, created = CartItem.objects.get_or_create(cart=cart, product=product, size=size)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f'Added "{product.name}" to your cart!')
    # Redirect back to where the user came from
    next_url = request.POST.get('next', request.META.get('HTTP_REFERER', '/'))
    return redirect(next_url)


def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('store:cart')


def checkout(request):
    cart = _get_cart(request)
    if cart.items.count() == 0:
        messages.warning(request, 'Your cart is empty.')
        return redirect('store:home')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                zip_code=form.cleaned_data['zip_code'],
                total=cart.get_total(),
            )
            for cart_item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price,
                    size=cart_item.size,
                )
            cart.items.all().delete()
            messages.info(request, 'Order pending. Proceed to payment.')
            return redirect('store:dummy_payment', order_id=order.id)
    else:
        initial = {}
        if request.user.is_authenticated:
            initial = {
                'full_name': request.user.get_full_name(),
                'email': request.user.email,
            }
        form = CheckoutForm(initial=initial)

    context = {'form': form, 'cart': cart}
    return render(request, 'store/checkout.html', context)


def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'store/order_success.html', {'order': order})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created! Welcome!')
            return redirect('store:home')
    else:
        form = RegisterForm()
    return render(request, 'store/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('store:home')

@login_required(login_url='store:login')
def wishlist_view(request):
    wishlist_items = request.user.wishlist.all()
    categories = Category.objects.all()
    cart = _get_cart(request)
    context = {
        'wishlist_items': wishlist_items,
        'categories': categories,
        'cart': cart,
    }
    return render(request, 'store/wishlist.html', context)

@login_required(login_url='store:login')
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = request.user.wishlist.get_or_create(product=product)
    
    if not created:
        wishlist_item.delete()
        messages.success(request, f'Removed "{product.name}" from your wishlist.')
    else:
        messages.success(request, f'Added "{product.name}" to your wishlist!')
        
    next_url = request.META.get('HTTP_REFERER', '/')
    return redirect(next_url)

@login_required(login_url='store:login')
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        rating = request.POST.get('rating', 5)
        comment = request.POST.get('comment', '')
        if comment:
            Review.objects.create(
                product=product,
                user=request.user,
                rating=rating,
                comment=comment
            )
            messages.success(request, 'Your review has been added!')
        else:
            messages.error(request, 'Review comment cannot be empty.')
    return redirect('store:product_detail', slug=product.slug)

@login_required(login_url='store:login')
def profile_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    cart = _get_cart(request)
    context = {
        'orders': orders,
        'cart': cart,
    }
    return render(request, 'store/profile.html', context)

@login_required(login_url='store:login')
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('store:profile')
    else:
        form = UserEditForm(instance=request.user)
    
    cart = _get_cart(request)
    return render(request, 'store/edit_profile.html', {'form': form, 'cart': cart})

def dummy_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'store/dummy_payment.html', {'order': order})

def create_checkout_session(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    domain_url = request.build_absolute_uri('/')[:-1]
    
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'inr',
                    'unit_amount': int(order.total * 100),
                    'product_data': {
                        'name': f'Threadory Order #{order.id}',
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=domain_url + reverse('store:stripe_success', kwargs={'order_id': order.id}),
            cancel_url=domain_url + reverse('store:dummy_payment', kwargs={'order_id': order.id}),
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        messages.error(request, f"Stripe error: {str(e)}")
        return redirect('store:dummy_payment', order_id=order.id)

def stripe_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.paid = True
    order.save()
    messages.success(request, f'Payment of ₹{order.total} via Stripe was successful!')
    return redirect('store:order_success', order_id=order.id)

