import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from store.models import Product, Category

# Try to get or create a Category
category, _ = Category.objects.get_or_create(
    name="T-Shirts",
    defaults={'slug': 't-shirts', 'description': 'Graphic T-Shirts'}
)

# Create the product
product, created = Product.objects.get_or_create(
    slug="bonkers-travis-scott-tshirt",
    defaults={
        'name': "Bonkers Travis Scott T-Shirt",
        'category': category,
        'price': 1499.00,
        'description': 'A premium white t-shirt featuring Bonkers Travis Scott print.',
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRz-M35Xq_oYj_I9CqO2I9K41bM4K3XjB19_g&s', 
        'back_image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6Z6RzVn9uV0NlZQ3D8DqZf6sA0F7E64bW1g&s', 
        'stock': 10,
        'available': True,
    }
)

if not created:
    product.name = "Bonkers Travis Scott T-Shirt"
    product.image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRz-M35Xq_oYj_I9CqO2I9K41bM4K3XjB19_g&s'
    product.back_image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6Z6RzVn9uV0NlZQ3D8DqZf6sA0F7E64bW1g&s'
    product.save()

print(f"Product {'created' if created else 'updated'}: {product.name}")
