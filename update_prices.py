import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from store.models import Product

# Update No Limits Hoodie
products = Product.objects.all()
for p in products:
    # Set fake original price to 1.5x the actual price just as a demonstration
    p.original_price = float(p.price) * 1.5
    p.save()

print(f"Updated {products.count()} products with an original discount price.")
