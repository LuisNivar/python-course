import os
import requests
import re

os.system("cls")

url = "http://books.toscrape.com"

response = requests.get(url, verify=False) # verify=False for practice purposes 


if response.status_code == 200:
    print("Connection successful!")
    print("-"*120)

    html = response.text

    # Patrón más robusto para extraer cada bloque de producto
    product_pattern = r'<article class="product_pod">(.*?)</article>'
    products = re.finditer(product_pattern, html, re.DOTALL)
    

    # Patrón para el título y el precio
    title_pattern = r'title="(.*?)"'
    price_pattern = r'<p class="price_color">(.*?)</p>'

    for index, product in enumerate(products):
        inner_html = product.group(0)  # contenido completo del div.product

        title = re.search(title_pattern, inner_html)
        price = re.search(price_pattern, inner_html)

        if title and price:
            print(f"[{index}] Title: {title.group(1)} | Price: {price.group(1)}")
    
    print("-"*120)
else:
    print("Connection error!")