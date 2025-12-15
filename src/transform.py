def transform_price(price_str: str) -> float:
    cleaned_price = "".join(c for c in price_str if c.isdigit() or c == ".")
    if not cleaned_price:
        raise ValueError(f"Invalid price format: {price_str}")
    return float(cleaned_price)


def transform_number_available(available_str: str) -> int:
    cleaned_number = "".join(c for c in available_str if c.isdigit())
    return int(cleaned_number) if cleaned_number else 0


def transform_category(category_str: str) -> str:
    return category_str.strip()


def transform_review_rating(rating_str: str) -> int | str:
    match (rating_str):
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
    books_raw: list[dict[str, str]],
) -> list[dict[str, str | float | int]]:
    transformed_batch: list[dict[str, str | float | int]] = []
    for book in books_raw:
        transformed_book: dict[str, str | float | int] = {
            "product_page_url": str(book["product_page_url"]),
            "universal_product_code": str(book["universal_product_code"]),
            "title": str(book["title"]),
            "price_including_tax": transform_price(book["price_including_tax"]),
            "price_excluding_tax": transform_price(book["price_excluding_tax"]),
            "number_available": transform_number_available(book["number_available"]),
            "product_description": str(book["product_description"]),
            "category": transform_category(book["category"]),
            "review_rating": transform_review_rating(book["review_rating"]),
            "image_url": str(book["image_url"]),
        }
        transformed_batch.append(transformed_book)
    return transformed_batch
