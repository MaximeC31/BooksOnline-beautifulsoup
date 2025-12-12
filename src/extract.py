from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_product_page_url(soup: BeautifulSoup, page_url: str) -> str:
    return page_url


def get_universal_product_code(soup: BeautifulSoup) -> str:
    td = soup.select_one("table.table.table-striped tr:nth-child(1) > td")
    return td.get_text() if td else "N/A"


def get_title(soup: BeautifulSoup) -> str:
    h1 = soup.select_one("h1")
    return h1.get_text() if h1 else "N/A"


def get_price_including_tax(soup: BeautifulSoup) -> str:
    td = soup.select_one("table.table.table-striped tr:nth-child(4) > td")
    return td.get_text() if td else "N/A"


def get_price_excluding_tax(soup: BeautifulSoup) -> str:
    td = soup.select_one("table.table.table-striped tr:nth-child(3) > td")
    return td.get_text() if td else "N/A"


def get_number_available(soup: BeautifulSoup) -> str:
    avail = soup.select_one("p.instock.availability")
    return avail.get_text() if avail else "N/A"


def get_product_description(soup: BeautifulSoup) -> str:
    desc = soup.select_one("#product_description + p")
    return desc.get_text() if desc else "N/A"


def get_category(soup: BeautifulSoup) -> str:
    breadcrumb = soup.select(".breadcrumb li")
    return breadcrumb[2].get_text() if breadcrumb and len(breadcrumb) > 2 else "N/A"


def get_review_rating(soup: BeautifulSoup) -> str:
    rating = soup.select_one("p.star-rating")
    classes = rating.get("class") if rating else "N/A"
    return classes[1] if isinstance(classes, list) and len(classes) == 2 else "N/A"


def get_image_url(soup: BeautifulSoup, page_url: str) -> str:
    img = soup.select_one(".item.active img")
    ##Appliquer un transform ici
    return urljoin(page_url, str(img.get("src"))) if img else "N/A"


def get_product_raw(html: str, page_url: str) -> dict[str, str]:
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


def get_product_urls(html: str, page_url: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")

    product_urls = soup.select("h3 > a")
    ##Appliquer un transform ici
    return [
        urljoin(page_url, str(product.get("href")))
        for product in product_urls
        if product_urls
    ]


def get_next_page_url(html: str, category_url: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")

    next_link = soup.select_one(".next a")
    return urljoin(category_url, str(next_link.get("href"))) if next_link else None
