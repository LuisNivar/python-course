from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
import os

url = "https://en.wikipedia.org/wiki/Web_scraping"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)

    first_link = page.locator("p a").first
    first_link.click()

    page.wait_for_load_state()

    first_title = page.locator("h1 span").first
    title = first_title.inner_text()

    first_paragraph = page.locator("p").first
    content = first_paragraph.inner_text()

    second_image = page.locator(".mw-body-content img").nth(1)
    img_src = urljoin(url, second_image.get_attribute("src"))

    os.system("cls")
    print("═"*100)
    print("Title:",title)
    print("─"*100)
    print("Content:",content)
    print("─"*100)
    print("Image:", img_src )
    print("─"*100)

    browser.close()

