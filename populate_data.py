"""
Script to populate the store with sample clothing data.
Run with: python manage.py shell < populate_data.py
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Category, Product

# Create categories
categories_data = [
    {'name': 'T-Shirts', 'slug': 't-shirts', 'description': 'Casual & graphic tees for every mood', 'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=600'},
    {'name': 'Shirts', 'slug': 'shirts', 'description': 'Formal & casual shirts for a polished look', 'image_url': 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=600'},
    {'name': 'Jeans', 'slug': 'jeans', 'description': 'Denim that fits your style', 'image_url': 'https://images.unsplash.com/photo-1542272454315-4c01d7abdf4a?w=600'},
    {'name': 'Jackets', 'slug': 'jackets', 'description': 'Outerwear for every season', 'image_url': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=600'},
    {'name': 'Dresses', 'slug': 'dresses', 'description': 'Elegant dresses for every occasion', 'image_url': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=600'},
    {'name': 'Accessories', 'slug': 'accessories', 'description': 'Complete your look', 'image_url': 'https://images.unsplash.com/photo-1584916201218-f4242ceb4809?w=600'},
    {'name': 'Shoes', 'slug': 'shoes', 'description': 'Step out in style', 'image_url': 'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=600'},
    {'name': 'Sweaters', 'slug': 'sweaters', 'description': 'Stay cozy and stylish', 'image_url': 'https://images.unsplash.com/photo-1614055535564-9a72138dc538?w=600'},
]

for cat_data in categories_data:
    Category.objects.get_or_create(slug=cat_data['slug'], defaults=cat_data)
    print(f"  + Category: {cat_data['name']}")

# Create products
products_data = [
    # T-Shirts
    {'name': 'Classic White Tee', 'slug': 'classic-white-tee', 'price': 599, 'stock': 50, 'description': 'A timeless white cotton t-shirt. Soft, breathable fabric with a relaxed fit. Perfect for layering or wearing on its own.', 'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500', 'category': 'T-Shirts'},
    {'name': 'Midnight Black Tee', 'slug': 'midnight-black-tee', 'price': 649, 'stock': 40, 'description': 'Essential black t-shirt crafted from premium cotton. A wardrobe staple with a modern slim fit.', 'image_url': 'https://images.unsplash.com/photo-1503341504253-dff4815485f1?w=500', 'category': 'T-Shirts'},
    {'name': 'Striped Summer Tee', 'slug': 'striped-summer-tee', 'price': 799, 'stock': 30, 'description': 'Navy and white striped t-shirt. Breezy cotton blend perfect for sunny days. Classic nautical vibes.', 'image_url': 'https://images.unsplash.com/photo-1523381210434-271e8be1f52b?w=500', 'category': 'T-Shirts'},
    {'name': 'Vintage Graphic Tee', 'slug': 'vintage-graphic-tee', 'price': 899, 'stock': 25, 'description': 'Retro-inspired graphic print on soft washed cotton. Fade-resistant print with a perfectly worn-in feel.', 'image_url': 'https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=500', 'category': 'T-Shirts'},

    # Shirts
    {'name': 'Oxford Blue Shirt', 'slug': 'oxford-blue-shirt', 'price': 1499, 'stock': 35, 'description': 'Classic Oxford button-down in sky blue. Premium cotton fabric with a tailored fit. Ideal for office or smart casual.', 'image_url': 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500', 'category': 'Shirts'},
    {'name': 'Linen Casual Shirt', 'slug': 'linen-casual-shirt', 'price': 1799, 'stock': 20, 'description': 'Relaxed-fit linen shirt in natural beige. Breathable and lightweight — perfect for summer weekends.', 'image_url': 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=500', 'category': 'Shirts'},
    {'name': 'Flannel Check Shirt', 'slug': 'flannel-check-shirt', 'price': 1299, 'stock': 28, 'description': 'Warm brushed flannel in a classic red and black check pattern. Soft and cozy for cooler days.', 'image_url': 'https://images.unsplash.com/photo-1589310243389-96a5483213a8?w=500', 'category': 'Shirts'},

    # Jeans
    {'name': 'Slim Fit Dark Wash', 'slug': 'slim-fit-dark-wash', 'price': 1999, 'stock': 45, 'description': 'Dark indigo slim-fit jeans with stretch comfort. Clean lines and a modern silhouette. Versatile enough for any occasion.', 'image_url': 'https://images.unsplash.com/photo-1542272454315-4c01d7abdf4a?w=500', 'category': 'Jeans'},
    {'name': 'Relaxed Fit Light Blue', 'slug': 'relaxed-fit-light-blue', 'price': 1799, 'stock': 32, 'description': 'Light wash relaxed-fit jeans with a comfortable straight leg. Casual and effortlessly cool.', 'image_url': 'https://images.unsplash.com/photo-1604176354204-9268737828e4?w=500', 'category': 'Jeans'},
    {'name': 'Black Skinny Jeans', 'slug': 'black-skinny-jeans', 'price': 2199, 'stock': 3, 'description': 'Jet black skinny jeans with premium stretch denim. Sleek, modern and incredibly comfortable.', 'image_url': 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=500', 'category': 'Jeans'},

    # Jackets
    {'name': 'Classic Denim Jacket', 'slug': 'classic-denim-jacket', 'price': 2999, 'stock': 15, 'description': 'Timeless denim jacket in medium wash. Sturdy cotton denim with classic button front and chest pockets.', 'image_url': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=500', 'category': 'Jackets'},
    {'name': 'Bomber Jacket Black', 'slug': 'bomber-jacket-black', 'price': 3499, 'stock': 12, 'description': 'Sleek black bomber jacket with ribbed cuffs and hem. Lightweight and versatile for transitional weather.', 'image_url': 'https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=500', 'category': 'Jackets'},
    {'name': 'Leather Biker Jacket', 'slug': 'leather-biker-jacket', 'price': 5999, 'stock': 8, 'description': 'Premium faux leather biker jacket with asymmetric zip. Bold and edgy — a statement piece for any wardrobe.', 'image_url': 'https://images.unsplash.com/photo-1520975954732-35dd22299614?w=500', 'category': 'Jackets'},

    # Dresses
    {'name': 'Floral Midi Dress', 'slug': 'floral-midi-dress', 'price': 2499, 'stock': 18, 'description': 'Elegant floral print midi dress with a flowing silhouette. Lightweight fabric with a cinched waist for a flattering fit.', 'image_url': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=500', 'category': 'Dresses'},
    {'name': 'Little Black Dress', 'slug': 'little-black-dress', 'price': 2999, 'stock': 22, 'description': 'The essential LBD. Sleek and sophisticated with a figure-flattering cut. Perfect for evening events.', 'image_url': 'https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=500', 'category': 'Dresses'},
    {'name': 'Summer Maxi Dress', 'slug': 'summer-maxi-dress', 'price': 1899, 'stock': 0, 'description': 'Breezy maxi dress in tropical print. Floor-length with adjustable straps. Your go-to for vacation style.', 'image_url': 'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=500', 'category': 'Dresses'},

    # Accessories
    {'name': 'Classic Aviator Sunglasses', 'slug': 'classic-aviator-sunglasses', 'price': 899, 'stock': 40, 'description': 'Timeless aviator shades with UV protection. Gold frame with dark green lenses.', 'image_url': 'https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=500', 'category': 'Accessories'},
    {'name': 'Leather Vintage Watch', 'slug': 'leather-vintage-watch', 'price': 2499, 'stock': 15, 'description': 'Minimalist analog watch with genuine brown leather strap and rose gold dial.', 'image_url': 'https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=500', 'category': 'Accessories'},
    {'name': 'Knitted Beanie', 'slug': 'knitted-beanie', 'price': 499, 'stock': 60, 'description': 'Warm and soft knitted beanie in charcoal grey. Perfect for winter days.', 'image_url': 'https://images.unsplash.com/photo-1576871337622-98d48d1cf531?w=500', 'category': 'Accessories'},

    # Shoes
    {'name': 'White Canvas Sneakers', 'slug': 'white-canvas-sneakers', 'price': 1299, 'stock': 50, 'description': 'Everyday essential white sneakers. Comfortable, versatile, and easy to clean.', 'image_url': 'https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=500', 'category': 'Shoes'},
    {'name': 'Classic Leather Oxfords', 'slug': 'classic-leather-oxfords', 'price': 3999, 'stock': 20, 'description': 'Premium black leather oxford shoes. The ultimate choice for formal events and office wear.', 'image_url': 'https://images.unsplash.com/photo-1614252339460-a1bd330dbdd8?w=500', 'category': 'Shoes'},
    {'name': 'Suede Chelsea Boots', 'slug': 'suede-chelsea-boots', 'price': 4599, 'stock': 12, 'description': 'Tan suede Chelsea boots featuring elastic side panels. A stylish and rugged addition to your wardrobe.', 'image_url': 'https://images.unsplash.com/photo-1638247025967-b4e38f787b76?w=500', 'category': 'Shoes'},

    # Sweaters
    {'name': 'Cable Knit Wool Sweater', 'slug': 'cable-knit-wool-sweater', 'price': 2199, 'stock': 35, 'description': 'Chunky cable knit sweater in cream white. Cozy wool blend to keep you exceptionally warm.', 'image_url': 'https://images.unsplash.com/photo-1614055535564-9a72138dc538?w=500', 'category': 'Sweaters'},
    {'name': 'V-Neck Cotton Pullover', 'slug': 'v-neck-cotton-pullover', 'price': 1499, 'stock': 40, 'description': 'Lightweight cotton v-neck sweater in navy blue. Ideal for layering over shirts.', 'image_url': 'https://images.unsplash.com/photo-1620799139834-6b8f844fbe61?w=500', 'category': 'Sweaters'},
    {'name': 'Oversized Streetwear Hoodie', 'slug': 'oversized-streetwear-hoodie', 'price': 1899, 'stock': 25, 'description': 'Ultra-soft fleece hoodie in heather grey with an oversized, relaxed fit and a spacious front pocket.', 'image_url': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=500', 'category': 'Sweaters'},
]

for p_data in products_data:
    cat_name = p_data.pop('category')
    category = Category.objects.get(name=cat_name)
    Product.objects.get_or_create(slug=p_data['slug'], defaults={**p_data, 'category': category})
    print(f"  + Product: {p_data['name']} (Rs.{p_data['price']})")

print(f"\nDone! Added {Category.objects.count()} categories and {Product.objects.count()} products.")
