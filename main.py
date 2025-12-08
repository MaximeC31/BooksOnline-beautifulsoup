from src.scraper import fetch_html
from src.parser import parse_product
from src.csv_writer import write_products_to_csv
from src.constants import DEFAULT_CSV_FILE


def main():
    product_url: str = (
        "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    )

    html_content: str | None = fetch_html(product_url)

    if html_content:
        product = parse_product(html_content, product_url)
        print(product)
        write_products_to_csv([product], DEFAULT_CSV_FILE)
    else:
        print("Scrape failed!")


main()
