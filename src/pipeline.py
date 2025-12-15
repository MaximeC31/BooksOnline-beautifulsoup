from .http_client import fetch_page
from .extract import (
    get_product_raw,
    get_product_urls,
    get_next_page_url,
    get_categories_urls,
)
from .transform import transform_product_data
from .csv_writer import write_products_csv

MAIN_URL = "https://books.toscrape.com"


def scrape_homepage_categories(main_page_url: str) -> list[str]:
    html = fetch_page(main_page_url)
    if not html:
        raise ValueError("Failed to fetch main page")

    return get_categories_urls(html, main_page_url)


def scrape_category_pages(category_url: str, max_pages: int = 2) -> list[str]:
    print("Scraping category with pagination...")

    all_product_urls: list[str] = []
    current_url = category_url
    page_count = 0

    while True:
        page_count += 1

        if page_count > max_pages:
            print(f"Max pages ({max_pages}) reached")
            break

        html = fetch_page(current_url)
        if not html:
            break

        product_urls = get_product_urls(html, current_url)
        all_product_urls.extend(product_urls)
        print(f"Page {page_count}: {len(product_urls)} products found")

        next_url = get_next_page_url(html, current_url)
        if not next_url:
            print("No more pages")
            break

        current_url = next_url

    return all_product_urls


def scrape_products_data(product_urls: list[str]) -> list[dict[str, str]]:
    print(f"\nScraping {len(product_urls)} products...")
    books_raw: list[dict[str, str]] = []

    for book_url in product_urls:
        html = fetch_page(book_url)
        if not html:
            continue

        book_raw = get_product_raw(html, book_url)
        books_raw.append(book_raw)
        print(f"Raw product added: {book_raw.get('title')}")

    return books_raw


def run_pipeline() -> None:
    try:
        all_categories_urls = scrape_homepage_categories(MAIN_URL)
    except ValueError as e:
        print(f"Error: {e}")
        return

    for category_url in all_categories_urls:
        print(f"\nProcessing category: {category_url}")

        all_product_urls = scrape_category_pages(category_url, max_pages=2)

        if len(all_product_urls) == 0:
            print("No products found")
            return

        books_raw = scrape_products_data(all_product_urls)

        print(f"\nDone: {len(books_raw)} products scraped")
        print(books_raw[len(books_raw) - 1])
