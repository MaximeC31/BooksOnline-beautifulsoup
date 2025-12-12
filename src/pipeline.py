from .http_client import fetch_page
from .extract import get_product_raw, get_product_urls
from .transform import transform_product_data
from .csv_writer import write_products_csv

TEST_URL = (
    "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
)


def run_product_pipeline() -> None:
    """
    Orchestration minimale :
    1) fetch_page(page_url)
    2) extract_product_data(html, page_url)
    3) Extract products + pagination
    4) Extract catégories
    5) transform_product_data(raw) -> record
    6) write_products_csv([record], out_path)
    """

    print("Fetching category...")
    cat_html = fetch_page(TEST_URL)
    if cat_html is None:
        return

    books_cat_collection = get_product_urls(cat_html, TEST_URL)
    if len(books_cat_collection) == 0:
        print("No products found")
        return

    print(f"Scraping {len(books_cat_collection)} products...")
    books_raw: list[dict[str, str]] = []

    for book_url in books_cat_collection:
        page_html = fetch_page(book_url)
        if page_html is None:
            continue

        raw_product = get_product_raw(page_html, book_url)
        books_raw.append(raw_product)
        print(f"Raw product added: {raw_product.get('title')}")

    print(f"Done: {len(books_raw)} products")
