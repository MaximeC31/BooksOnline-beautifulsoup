from .http_client import fetch_page
from .extract import get_product_data
from .transform import transform_product_data
from .csv_writer import write_products_csv

TEST_URL = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"


def run_product_pipeline() -> None:
    """
    Orchestration minimale :
    1) fetch_page(page_url)
    2) extract_product_data(html, page_url) -> raw
    3) Extract catégories + pagination
    4) transform_product_data(raw) -> record
    5) write_products_csv([record], out_path)

    Gérer les erreurs de façon simple (try/except) et imprimer l'état.
    """
    # TODO: implémenter l'orchestration

    page_data = fetch_page(TEST_URL)

    if page_data is None:
        print("Failed to fetch page data.")
        return

    print(f"Fetched {len(page_data)} chars")
    print(get_product_data(page_data, TEST_URL))
