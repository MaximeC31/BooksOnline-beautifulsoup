from src.scraper import fetch_html
from src.parser import parse_product


def main():
    bo_product_url: str = (
        "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    )

    html_content: str | None = fetch_html(bo_product_url)

    if html_content:
        print(parse_product(html_content, bo_product_url))
    else:
        print("Scrape failed!")


main()
