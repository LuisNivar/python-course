import os
import requests
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin

parser = argparse.ArgumentParser(description="Web scraping to check SEO for giving URL")
parser.add_argument("url",type=str, help="The URL of the site you want to scrape and check.")

args = parser.parse_args()

url = args.url

response = requests.get(url, verify=False)

if response.status_code == 200:
    os.system("cls")
    print("Connection succsesful!")
    print("\033[34m═"*90,end="\n\033[0m")
    print("\033[34m SEO • CLI \033[0m")
    print("\033[34m■"*90,end="\n\033[0m")
    
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.text  # type: ignore
    print("\033[1mWeb URL\033[0m:","\033[0;33m" + url + "\033[0m")
    print("\033[1mTitle URL\033[0m:","\033[0;33m" + title + "\033[0m")
    print("\033[1;30m─"*90,end="\n\033[0m")
    

    soup = BeautifulSoup(response.text, "html.parser")

    if len(title) < 70:
        print("\033[0;32m✅ The title is correct!\033[0m")
    else:
        print("\033[0;31m❌ The tittle is TOO long!\033[0m")

    print("\033[1;30m─"*90,end="\n\033[0m")
   


