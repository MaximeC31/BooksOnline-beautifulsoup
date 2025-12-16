MAIN_URL: str = "https://books.toscrape.com"
DEFAULT_MAX_PAGES: int = 2

PRODUCT_FIELDS: list[str] = [
    "product_page_url",
    "universal_product_code",
    "title",
    "price_including_tax",
    "price_excluding_tax",
    "number_available",
    "product_description",
    "category",
    "review_rating",
    "image_url",
]

ProductRaw = dict[str, str]
ProductTransformed = dict[str, str | float | int]
