from .http_client import fetch_page
from .extract import get_product_raw, get_product_urls, get_next_page_url
from .transform import transform_product_data
from .csv_writer import write_products_csv

TEST_URL = (
    "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
)


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
    all_product_urls = scrape_category_pages(TEST_URL, max_pages=2)

    if len(all_product_urls) == 0:
        print("No products found")
        return

    books_raw = scrape_products_data(all_product_urls)

    print(f"\nDone: {len(books_raw)} products scraped")
    print(books_raw[len(books_raw) - 1])
