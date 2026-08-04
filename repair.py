import os

css_file = r"c:\Users\ACER\OneDrive\Desktop\miniproject\store\static\store\css\style.css"

with open(css_file, 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the messy ending
messy_end = """}
    transition: opacity 0.3s ease-in-out;
}"""

if messy_end in content:
    content = content.replace(messy_end, "}")
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed!")
else:
    print("Not found.")
