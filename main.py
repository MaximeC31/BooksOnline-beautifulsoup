from src.client.http_client import fetch_html
from src.core.parser import parse_product
from src.services.category import get_product_urls_from_category_page
from src.core.csv_writer import write_products_to_csv
from src.constants.constants import DEFAULT_CSV_FILE, ProductData


def main():
    category_url = (
        "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    )
    print(f"Scraping category: {category_url}")

    product_urls = get_product_urls_from_category_page(category_url)
    print(f"Found {len(product_urls)} products. Starting extraction...")

    products: list[ProductData] = []

    for url in product_urls:
        html = fetch_html(url)
        if not html:
            continue

        print(f"Processing: {url}")
        data = parse_product(html, url)
        products.append(data)

    if not products:
        print("No products extracted.")
        return

    write_products_to_csv(products, DEFAULT_CSV_FILE)
    print(f"Successfully wrote {len(products)} products to {DEFAULT_CSV_FILE}")


main()
