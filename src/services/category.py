from bs4 import BeautifulSoup
from src.client.http_client import fetch_html
from src.core.parser import get_product_urls


def get_product_urls_from_category_page(category_url: str) -> list[str]:
    html_content = fetch_html(category_url)
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, "html.parser")
    return get_product_urls(soup, category_url)
