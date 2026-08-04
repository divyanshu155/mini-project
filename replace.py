import re
import os

files_to_update = [
    r"c:\Users\ACER\OneDrive\Desktop\miniproject\store\templates\store\index.html",
    r"c:\Users\ACER\OneDrive\Desktop\miniproject\store\templates\store\category.html",
    r"c:\Users\ACER\OneDrive\Desktop\miniproject\store\templates\store\search.html"
]

for f in files_to_update:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        content = re.sub(
            r'\{%\s*if product\.image_url\s*%\}\s*<img src="\{\{\s*product\.image_url\s*\}\}" alt="\{\{\s*product\.name\s*\}\}" class="product-img">',
            r'{% if product.image_url %}\n                    <div class="hover-image-container">\n                        <img src="{{ product.image_url }}" alt="{{ product.name }}" class="product-img img-front">\n                        {% if product.back_image_url %}\n                        <img src="{{ product.back_image_url }}" alt="{{ product.name }} Back" class="product-img img-back">\n                        {% endif %}\n                    </div>',
            content
        )
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)

# wishlist.html uses item.product
wishlist_file = r"c:\Users\ACER\OneDrive\Desktop\miniproject\store\templates\store\wishlist.html"
if os.path.exists(wishlist_file):
    with open(wishlist_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = re.sub(
        r'\{%\s*if item\.product\.image_url\s*%\}\s*<img src="\{\{\s*item\.product\.image_url\s*\}\}" alt="\{\{\s*item\.product\.name\s*\}\}" class="product-img">',
        r'{% if item.product.image_url %}\n                    <div class="hover-image-container">\n                        <img src="{{ item.product.image_url }}" alt="{{ item.product.name }}" class="product-img img-front">\n                        {% if item.product.back_image_url %}\n                        <img src="{{ item.product.back_image_url }}" alt="{{ item.product.name }} Back" class="product-img img-back">\n                        {% endif %}\n                    </div>',
        content
    )
    with open(wishlist_file, 'w', encoding='utf-8') as file:
        file.write(content)

print("Done replacing.")
