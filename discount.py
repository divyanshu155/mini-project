import os
import re

templates_dir = r"c:\Users\ACER\OneDrive\Desktop\miniproject\store\templates\store"

pattern1 = r'(<span class="product-price">₹\{\{\s*product\.price\s*\}\}</span>)'
replace1 = r'{% if product.original_price and product.original_price > product.price %}<span class="product-price-original" style="text-decoration: line-through; color: var(--text-muted); font-size: 0.85em; margin-right: 6px;">₹{{ product.original_price }}</span>{% endif %}\1'

pattern2 = r'(<span class="product-price">₹\{\{\s*related_product\.price\s*\}\}</span>)'
replace2 = r'{% if related_product.original_price and related_product.original_price > related_product.price %}<span class="product-price-original" style="text-decoration: line-through; color: var(--text-muted); font-size: 0.85em; margin-right: 6px;">₹{{ related_product.original_price }}</span>{% endif %}\1'

pattern3 = r'(<p class="detail-price">₹\{\{\s*product\.price\s*\}\}</p>)'
replace3 = r'<p class="detail-price">{% if product.original_price and product.original_price > product.price %}<span class="detail-price-original" style="text-decoration: line-through; color: var(--text-muted); font-size: 0.8em; margin-right: 12px; font-weight: 500;">₹{{ product.original_price }}</span>{% endif %}₹{{ product.price }}</p>'

pattern4 = r'(<span class="product-price">₹\{\{\s*item\.product\.price\s*\}\}</span>)'
replace4 = r'{% if item.product.original_price and item.product.original_price > item.product.price %}<span class="product-price-original" style="text-decoration: line-through; color: var(--text-muted); font-size: 0.85em; margin-right: 6px;">₹{{ item.product.original_price }}</span>{% endif %}\1'

for f_name in os.listdir(templates_dir):
    if f_name.endswith('.html'):
        f_path = os.path.join(templates_dir, f_name)
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = re.sub(pattern1, replace1, content)
        new_content = re.sub(pattern2, replace2, new_content)
        new_content = re.sub(pattern3, replace3, new_content) # Changed to replace fully since <p> was part of the group
        new_content = re.sub(pattern4, replace4, new_content)
        
        if content != new_content:
            with open(f_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {f_name}")
