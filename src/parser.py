from bs4 import BeautifulSoup
from urllib.parse import urljoin


# --- MICRO-FUNCTIONS ---


def get_upc(soup: BeautifulSoup) -> str:
    upc = soup.select_one("table.table.table-striped tr:nth-child(1) > td")
    return upc.text if upc else ""


def get_title(soup: BeautifulSoup) -> str:
    title = soup.select_one("h1")
    return title.text if title else ""


def get_price_including_tax(soup: BeautifulSoup) -> str:
    price_including_tax = soup.select_one(
        "table.table.table-striped tr:nth-child(4) > td"
    )
    if not price_including_tax:
        return ""

    return "".join(c for c in price_including_tax.text if c.isdigit() or c == ".")


def get_price_excluding_tax(soup: BeautifulSoup) -> str:
    price_excluding_tax = soup.select_one(
        "table.table.table-striped tr:nth-child(3) > td"
    )
    if not price_excluding_tax:
        return ""

    return "".join(c for c in price_excluding_tax.text if c.isdigit() or c == ".")


def get_category(soup: BeautifulSoup) -> str:
    category = soup.select_one(".breadcrumb li:nth-child(3)")
    return category.text.strip() if category else ""


def get_description(soup: BeautifulSoup) -> str:
    description = soup.select_one("#product_description + p")
    return description.text if description else ""


def get_image_url(soup: BeautifulSoup, product_url: str) -> str:
    image = soup.select_one(".item.active > img")
    if not image:
        return ""

    relative_image_url: str = str(image.get("src", ""))
    return urljoin(product_url, relative_image_url)


def get_availability(soup: BeautifulSoup) -> int:
    stock = soup.select_one("p.instock.availability")
    if not stock:
        return 0

    stock_digits: str = "".join(c for c in stock.text if c.isdigit())
    return int(stock_digits)


def get_rating(soup: BeautifulSoup) -> int:
    rating_element = soup.select_one("p.star-rating")
    if not rating_element:
        return 0

    classes = rating_element.get("class")
    if not classes or len(classes) < 2:
        return 0

    rating: str = classes[1]
    match rating:
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
            return 0


# --- ORCHESTRATION ---


def parse_product(html_content: str, product_url: str) -> dict[str, str | int]:
    soup: BeautifulSoup = BeautifulSoup(html_content, "html.parser")

    return {
        "product_page_url": product_url,
        "universal_product_code": get_upc(soup),
        "title": get_title(soup),
        "price_including_tax": get_price_including_tax(soup),
        "price_excluding_tax": get_price_excluding_tax(soup),
        "stock_available": get_availability(soup),
        "product_description": get_description(soup),
        "category": get_category(soup),
        "review_rating": get_rating(soup),
        "image_url": get_image_url(soup, product_url),
    }
