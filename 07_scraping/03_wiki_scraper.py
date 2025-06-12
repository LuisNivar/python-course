from bs4 import BeautifulSoup
from urllib.parse import urljoin 
import requests
import os

os.system("cls")

url = "https://en.wikipedia.org/wiki/Web_scraping"

response = requests.get(url, verify=False)

if response.status_code == 200:
    print("Connection successful!")
    print("-"*120)
    
    soup = BeautifulSoup(response.text, "html.parser")
    title_tag = soup.title

    if title_tag:
        print(title_tag.string)
    
    print("-"*120)

    tittle = [tittle.string for tittle in soup.find_all("h1")] # type: ignore
    sub_tittle = [sub_tittle.string for sub_tittle in soup.find_all("h2")] # type: ignore
    links = [urljoin(url,link.get("href")) for link in soup.find_all("a")] # type: ignore

    print(tittle)
    print(sub_tittle)
    print(links[:10])

    print("-"*120)

else:
    print("Error connection!")