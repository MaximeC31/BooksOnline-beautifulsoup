from .constants import ProductRaw, ProductTransformed


def transform_price(price_str: str) -> float:
    cleaned_price = "".join(c for c in price_str if c.isdigit() or c == ".")
    if not cleaned_price:
        print(f"[WARNING] Invalid price format: '{price_str}', using 0.0")
        return 0.0
    return float(cleaned_price)


def transform_stock(stock_str: str) -> int:
    cleaned = "".join(c for c in stock_str if c.isdigit())
    return int(cleaned) if cleaned else 0


def transform_category(category_str: str) -> str:
    return category_str.strip()


def transform_rating(rating_str: str) -> int | str:
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


def transform_product_data(
    books_raw: list[ProductRaw],
) -> list[ProductTransformed]:
    return [
        {
            "product_page_url": product["product_page_url"],
            "universal_product_code": product["universal_product_code"],
            "title": product["title"],
            "price_including_tax": transform_price(product["price_including_tax"]),
            "price_excluding_tax": transform_price(product["price_excluding_tax"]),
            "number_available": transform_stock(product["number_available"]),
            "product_description": product["product_description"],
            "category": transform_category(product["category"]),
            "review_rating": transform_rating(product["review_rating"]),
            "image_url": product["image_url"],
        }
        for product in books_raw
    ]
