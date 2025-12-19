from pathlib import Path
from typing import Any
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .http_client import fetch, fetch_image
from .loaders import create_csv, append_row, save_image
from .transform import transform_book
from .constants import *


def scrape_site(main_url: str) -> None:
    html = fetch(main_url)
    if not html:
        return

    soup = BeautifulSoup(html, "html.parser")
    for link in soup.select(".side_categories ul.nav-list ul li a"):
        category_url = urljoin(main_url, str(link.get("href", "")))
        print(f"\n[INFO] Category: {category_url}")
        scrape_category(category_url)


def scrape_category(category_url: str) -> None:
    current_url = category_url
    category_name: str | None = ""
    csv_path: Path | None = None

    while True:
        html = fetch(current_url)
        if not html:
            break

        soup = BeautifulSoup(html, "html.parser")
        if not category_name:
            breadcrumb = soup.select(".breadcrumb li")
            category_name = breadcrumb[2].get_text().strip() if len(breadcrumb) > 2 else "Unknown"
            csv_path = create_csv(category_name)
            print(f"[INFO] {category_name}")

        for link in soup.select("h3 > a"):
            book_url = urljoin(current_url, str(link.get("href", "")))
            scrape_book(book_url, category_name, csv_path)

        next_link = soup.select_one(".next a")
        if not next_link:
            break
        current_url = urljoin(current_url, str(next_link.get("href", "")))

    print(f"[INFO] {category_name}: done")


def scrape_book(book_url: str, category_name: str, csv_path: Path) -> None:
    if not csv_path:
        print(f"[ERROR] No CSV path for {book_url}")
        return

    html = fetch(book_url)
    if not html:
        return

    soup = BeautifulSoup(html, "html.parser")
    raw: dict[str, Any] = {
        PRODUCT_PAGE_URL: book_url,
        TITLE: soup.select_one("h1"),
        UPC: soup.select_one("table.table-striped tr:nth-child(1) > td"),
        PRICE_INCLUDING_TAX: soup.select_one("table.table-striped tr:nth-child(4) > td"),
        PRICE_EXCLUDING_TAX: soup.select_one("table.table-striped tr:nth-child(3) > td"),
        NUMBER_AVAILABLE: soup.select_one("p.instock.availability"),
        PRODUCT_DESCRIPTION: soup.select_one("#product_description + p"),
        REVIEW_RATING: soup.select_one("p.star-rating"),
        IMAGE_URL: soup.select_one(".item.active img"),
    }
    book_data = transform_book(raw, book_url, category_name)

    append_row(csv_path, book_data)

    image_bytes = fetch_image(book_data[IMAGE_URL])
    if image_bytes:
        save_image(image_bytes, book_data[TITLE])

    print(f"[INFO] {book_data[TITLE]}")
