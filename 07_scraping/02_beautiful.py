from bs4 import BeautifulSoup
import requests
import os

os.system("cls")

url = "https://tienda.omega.com.do/es/category/list/1?Type=grid"

response = requests.get(url, verify=False)

if response.status_code == 200:
    print("Connection successful!")
    print("-"*120)
    
    soup = BeautifulSoup(response.text, "html.parser")
    title_tag = soup.title

    if title_tag:
        print(title_tag.string)
    
    print("-"*120)

    products = soup.find_all("div",class_="product-thumb-info")

    if products:
        for index, product in enumerate(products[0:6]):
            title_tag = product.find("h4") # type: ignore
            price_tag = product.find("span", class_="amount") # type: ignore

            if title_tag and price_tag:
                title = title_tag.string # type: ignore
                price = price_tag.string # type: ignore
                print(f"[{index}]: Title: {title} | Price: {price}")
        print("-"*120)
    else:
        print("Product not found!")

else:
    print("Error connection!")