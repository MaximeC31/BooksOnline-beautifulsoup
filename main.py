from app.scraper import fetch_html
from app.parser import parse_product


def main():
    bo_product_url = (
        "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    )

    html_content = fetch_html(bo_product_url)

    if html_content:
        product_data = parse_product(html_content, bo_product_url)
        print(product_data)
    else:
        print("Scrape failed!")


main()
