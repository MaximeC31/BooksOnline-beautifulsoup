from typing import Dict, Any
from .http_client import fetch_page
from .extract import extract_product_data
from .transform import transform_product_data
from .csv_writer import write_products_csv

TEST_URL = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"


def run_product_pipeline() -> None:
    """
    Orchestration minimale :
    1) fetch_page(page_url)
    2) extract_product_data(html, page_url) -> raw
    3) transform_product_data(raw) -> record
    4) write_products_csv([record], out_path)

    Gérer les erreurs de façon simple (try/except) et imprimer l'état.
    """
    # TODO: implémenter l'orchestration

    print("Pipeline non encore implémentée.")
