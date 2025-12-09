from typing import Dict, List

ProductData = Dict[str, str | int | float | None]

PRODUCT_FIELDS: Dict[str, str] = {
    "URL": "product_page_url",
    "UPC": "universal_product_code",
    "TITLE": "title",
    "PRICE_INC_TAX": "price_including_tax",
    "PRICE_EXC_TAX": "price_excluding_tax",
    "STOCK": "stock_available",
    "DESCRIPTION": "product_description",
    "CATEGORY": "category",
    "RATING": "review_rating",
    "IMAGE_URL": "image_url",
}

CSV_HEADERS: List[str] = list(PRODUCT_FIELDS.values())

DEFAULT_CSV_FILE = "data/products.csv"
