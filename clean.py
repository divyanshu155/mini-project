import os
import re

css_file = r"c:\Users\ACER\OneDrive\Desktop\miniproject\store\static\store\css\style.css"

with open(css_file, 'r', encoding='utf-8') as f:
    content = f.read()

# remove from /* ---------- Hover Image Flip ---------- */ to the end
idx = content.find("/* ---------- Hover Image Flip ---------- */")
if idx != -1:
    content = content[:idx]

new_css = """/* ---------- Hover Image Flip ---------- */
.product-img-wrap {
    position: relative;
    display: block;
    overflow: hidden;
}

.hover-image-container {
    position: relative;
    width: 100%;
    height: 100%;
    display: block;
}

.hover-image-container .img-back {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0;
    transition: opacity 0.5s ease-in-out;
    z-index: 2;
    pointer-events: none; /* Prevent back image from capturing hover separately */
}

.hover-image-container .img-front {
    transition: opacity 0.5s ease-in-out;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 1;
    display: block;
}

/* Strictly target the product card wrapper hover */
.product-card:hover .hover-image-container .img-back {
    opacity: 1 !important;
}

.product-card:hover .hover-image-container .img-front {
    opacity: 0 !important;
}
"""

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(content + new_css)

print("Updated CSS effectively.")
