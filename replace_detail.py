import re
import os

detail_file = r"c:\Users\ACER\OneDrive\Desktop\miniproject\store\templates\store\product_detail.html"

if os.path.exists(detail_file):
    with open(detail_file, 'r', encoding='utf-8') as file:
        content = file.read()
            
    content = re.sub(
        r'\{%\s*if related_product\.image_url\s*%\}\s*<img src="\{\{\s*related_product\.image_url\s*\}\}" alt="\{\{\s*related_product\.name\s*\}\}" class="product-img">',
        r'{% if related_product.image_url %}\n                        <div class="hover-image-container">\n                            <img src="{{ related_product.image_url }}" alt="{{ related_product.name }}" class="product-img img-front">\n                            {% if related_product.back_image_url %}\n                            <img src="{{ related_product.back_image_url }}" alt="{{ related_product.name }} Back" class="product-img img-back">\n                            {% endif %}\n                        </div>',
        content
    )
    
    with open(detail_file, 'w', encoding='utf-8') as file:
        file.write(content)

print("Done detailing.")
