from .http_client import fetch_page
from .extract import (
    extract_product_data,
    get_product_urls,
    get_next_page_url,
    get_categories_urls,
)
from .transform import transform_product_data
from .csv_writer import write_products_category
from .constants import MAIN_URL, DEFAULT_MAX_PAGES, ProductRaw


def scrape_homepage_categories(main_page_url: str) -> list[str]:
    html = fetch_page(main_page_url)
    if not html:
        raise ValueError("Failed to fetch main page")

    return get_categories_urls(html, main_page_url)


def scrape_category(category_url: str, max_pages: int = DEFAULT_MAX_PAGES) -> list[str]:
    print("[INFO] Scraping category with pagination...")

    all_product_urls: list[str] = []
    current_url = category_url
    page_count = 0

    while True:
        page_count += 1
        if page_count > max_pages:
            print(f"[INFO] Max pages ({max_pages}) reached")
            break
        html = fetch_page(current_url)
        if not html:
            print(f"[WARNING] Failed to fetch page {page_count}")
            break

        product_urls = get_product_urls(html, current_url)
        all_product_urls.extend(product_urls)
        print(f"[INFO] Page {page_count}: {len(product_urls)} products found")

        next_url = get_next_page_url(html, current_url)
        if not next_url:
            print("[INFO] No more pages")
            break

        current_url = next_url

    return all_product_urls


def scrape_products_data(product_urls: list[str]) -> list[ProductRaw]:
    print(f"[INFO] Scraping {len(product_urls)} products...")

    products_raw: list[ProductRaw] = []
    for product_url in product_urls:
        html = fetch_page(product_url)
        if not html:
            print(f"[WARNING] Failed to fetch product: {product_url}")
            continue

        product_raw = extract_product_data(html, product_url)
        products_raw.append(product_raw)
        print(f"[INFO] Raw product added: {product_raw.get('title')}")

    return products_raw


def scrape_all_categories() -> None:
    try:
        all_categories_urls = scrape_homepage_categories(MAIN_URL)
    except ValueError as e:
        print(f"[ERROR] {e}")
        return

    for category_url in all_categories_urls:
        print(f"\n[INFO] Processing category: {category_url}")

        all_product_urls = scrape_category(category_url, max_pages=DEFAULT_MAX_PAGES)
        if not all_product_urls:
            print("[WARNING] No products found, skipping category...")
            continue

        products_raw = scrape_products_data(all_product_urls)
        products_transformed = transform_product_data(products_raw)

        if not products_transformed:
            print("[WARNING] No transformed products, skipping CSV write")
            continue

        write_products_category(products_transformed)

        print(
            f"[INFO] Category {products_transformed[0]['category']}: {len(products_transformed)} products"
        )
