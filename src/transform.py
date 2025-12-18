from typing import Any
from urllib.parse import urljoin
from .constants import *


def transform_price(el: Any) -> float | str:
    if not el:
        return "N/A"
    cleaned = "".join(c for c in el.get_text().strip() if c.isdigit() or c == ".")
    return float(cleaned) if cleaned else "N/A"


def transform_stock(el: Any) -> int | str:
    if not el:
        return "N/A"
    digits = "".join(c for c in el.get_text() if c.isdigit())
    return int(digits) if digits else "N/A"


def transform_description(el: Any) -> str:
    if not el:
        return "N/A"
    return el.get_text().strip().replace(";", ",")


def transform_rating(el: Any) -> int | str:
    if not el:
        return "N/A"
    classes = el.get("class", [])
    rating_str = classes[1] if len(classes) == 2 else ""

    match rating_str:
        case "One":
            return 1
        case "Two":
            return 2
        case "Three":
            return 3
        case "Four":
            return 4
        case "Five":
            return 5
        case _:
            return "N/A"


def transform_book(raw: dict[str, Any], base_url: str, category_name: str) -> dict[str, Any]:
    return {
        PRODUCT_PAGE_URL: raw[PRODUCT_PAGE_URL] if raw[PRODUCT_PAGE_URL] else "N/A",
        UPC: raw[UPC].get_text().strip() if raw[UPC] else "N/A",
        TITLE: raw[TITLE].get_text().strip() if raw[TITLE] else "N/A",
        PRICE_INCLUDING_TAX: transform_price(raw[PRICE_INCLUDING_TAX]),
        PRICE_EXCLUDING_TAX: transform_price(raw[PRICE_EXCLUDING_TAX]),
        NUMBER_AVAILABLE: transform_stock(raw[NUMBER_AVAILABLE]),
        PRODUCT_DESCRIPTION: transform_description(raw[PRODUCT_DESCRIPTION]),
        CATEGORY: category_name,
        REVIEW_RATING: transform_rating(raw[REVIEW_RATING]),
        IMAGE_URL: urljoin(base_url, raw[IMAGE_URL].get("src", "")) if raw[IMAGE_URL] else "N/A",
    }
