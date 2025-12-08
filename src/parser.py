from bs4 import BeautifulSoup
from urllib.parse import urljoin
from src.constants import PRODUCT_FIELDS


# --- MICRO-FUNCTIONS ---


def get_upc(soup: BeautifulSoup) -> str | None:
    upc = soup.select_one("table.table.table-striped tr:nth-child(1) > td")
    return upc.text if upc else None


def get_title(soup: BeautifulSoup) -> str | None:
    title = soup.select_one("h1")
    return title.text if title else None


def get_price_including_tax(soup: BeautifulSoup) -> float | None:
    price_including_tax_element = soup.select_one(
        "table.table.table-striped tr:nth-child(4) > td"
    )
    if not price_including_tax_element:
        return None

    clean_price = "".join(
        c for c in price_including_tax_element.text if c.isdigit() or c == "."
    )
    try:
        return float(clean_price)
    except ValueError:
        return None


def get_price_excluding_tax(soup: BeautifulSoup) -> float | None:
    price_excluding_tax_element = soup.select_one(
        "table.table.table-striped tr:nth-child(3) > td"
    )
    if not price_excluding_tax_element:
        return None

    clean_price = "".join(
        c for c in price_excluding_tax_element.text if c.isdigit() or c == "."
    )
    try:
        return float(clean_price)
    except ValueError:
        return None


def get_category(soup: BeautifulSoup) -> str | None:
    category = soup.select_one(".breadcrumb li:nth-child(3)")
    return category.text.strip() if category else None


def get_description(soup: BeautifulSoup) -> str | None:
    description = soup.select_one("#product_description + p")
    return description.text if description else None


def get_image_url(soup: BeautifulSoup, product_url: str) -> str | None:
    image = soup.select_one(".item.active > img")
    if not image:
        return None

    relative_image_url = str(image.get("src", ""))
    if not relative_image_url:
        return None

    return urljoin(product_url, relative_image_url)


def get_availability(soup: BeautifulSoup) -> int | None:
    stock = soup.select_one("p.instock.availability")
    if not stock:
        return None

    stock_digits = "".join(c for c in stock.text if c.isdigit())
    return int(stock_digits) if stock_digits else None


def get_rating(soup: BeautifulSoup) -> int | None:
    rating_element = soup.select_one("p.star-rating")
    if not rating_element:
        return None

    classes = rating_element.get("class")
    if not classes or len(classes) < 2:
        return None

    rating = classes[1]
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
            return None


# --- ORCHESTRATION ---


def parse_product(
    html_content: str, product_url: str
) -> dict[str, str | int | float | None]:
    soup: BeautifulSoup = BeautifulSoup(html_content, "html.parser")

    return {
        PRODUCT_FIELDS["URL"]: product_url,
        PRODUCT_FIELDS["UPC"]: get_upc(soup),
        PRODUCT_FIELDS["TITLE"]: get_title(soup),
        PRODUCT_FIELDS["PRICE_INC_TAX"]: get_price_including_tax(soup),
        PRODUCT_FIELDS["PRICE_EXC_TAX"]: get_price_excluding_tax(soup),
        PRODUCT_FIELDS["STOCK"]: get_availability(soup),
        PRODUCT_FIELDS["DESCRIPTION"]: get_description(soup),
        PRODUCT_FIELDS["CATEGORY"]: get_category(soup),
        PRODUCT_FIELDS["RATING"]: get_rating(soup),
        PRODUCT_FIELDS["IMAGE_URL"]: get_image_url(soup, product_url),
    }
