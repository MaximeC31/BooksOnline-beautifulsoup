from typing import Dict
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_product_page_url(soup: BeautifulSoup, page_url: str) -> str:
    return page_url


def get_universal_product_code(soup: BeautifulSoup) -> str:
    td_el = soup.select_one("table.table.table-striped tr:nth-child(1) > td")
    return td_el.get_text() if td_el else "N/A"


def get_title(soup: BeautifulSoup) -> str:
    h1_el = soup.select_one("h1")
    return h1_el.get_text() if h1_el else "N/A"


def get_price_including_tax(soup: BeautifulSoup) -> str:
    td_el = soup.select_one("table.table.table-striped tr:nth-child(4) > td")
    return td_el.get_text() if td_el else "N/A"


def get_price_excluding_tax(soup: BeautifulSoup) -> str:
    td_el = soup.select_one("table.table.table-striped tr:nth-child(3) > td")
    return td_el.get_text() if td_el else "N/A"


def get_number_available(soup: BeautifulSoup) -> str:
    avail_el = soup.select_one("p.instock.availability")
    return avail_el.get_text() if avail_el else "N/A"


def get_product_description(soup: BeautifulSoup) -> str:
    desc_el = soup.select_one("#product_description + p")
    return desc_el.get_text() if desc_el else "N/A"


def get_category(soup: BeautifulSoup) -> str:
    breadcrumb = soup.select(".breadcrumb li")
    return breadcrumb[2].get_text() if breadcrumb and len(breadcrumb) > 2 else "N/A"


def get_review_rating(soup: BeautifulSoup) -> str:
    rating_element = soup.select_one("p.star-rating")
    classes = rating_element.get("class") if rating_element else "N/A"
    return classes[1] if isinstance(classes, list) and len(classes) == 2 else "N/A"


def get_image_url(soup: BeautifulSoup, page_url: str) -> str:
    img_el = soup.select_one(".item.active img")
    src = img_el.get("src") if img_el else None
    return urljoin(page_url, str(src)) if src else "N/A"


def get_product_data(html: str, page_url: str) -> Dict[str, str]:
    print("[EXTRACT] Récupération produit...")
    soup = BeautifulSoup(html, "html.parser")

    return {
        "product_page_url": get_product_page_url(soup, page_url),
        "universal_product_code": get_universal_product_code(soup),
        "title": get_title(soup),
        "price_including_tax": get_price_including_tax(soup),
        "price_excluding_tax": get_price_excluding_tax(soup),
        "number_available": get_number_available(soup),
        "product_description": get_product_description(soup),
        "category": get_category(soup),
        "review_rating": get_review_rating(soup),
        "image_url": get_image_url(soup, page_url),
    }
