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
    ##Appliquer un transform ici
    img_el = soup.select_one(".item.active img")
    src = img_el.get("src") if img_el else None
    return urljoin(page_url, str(src)) if src else "N/A"


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

    products_url = soup.select("h3 > a")

    ##Appliquer un transform ici
    return [
        urljoin(page_url, str(product.get("href")))
        for product in products_url
        if product.get("href")
    ]


def get_next_page_url(soup: BeautifulSoup, current_url: str) -> str | None:
    """
    Récupérer l'URL de la page suivante (bouton Next).

    Args:
        soup: BeautifulSoup object de la page actuelle
        current_url: URL de la page actuelle (pour construire URL absolue)

    Returns:
        URL absolue de la page suivante, ou None si pas de bouton Next

    Logique:
        - Sélectionner le bouton/lien "next" (CSS selector)
        - Si n'existe pas → retourner None
        - Extraire href
        - Convertir en URL absolue avec urljoin()
        - Retourner l'URL
    """
    # TODO: implémenter la détection du bouton Next
    return None


def scrape_category(url: str, max_pages: int = 3, _current_page: int = 1) -> list[str]:
    """
    Scraper récursivement une catégorie avec pagination.

    Args:
        url: URL de la page catégorie à scraper
        max_pages: Nombre maximum de pages à scraper (protection)
        _current_page: Compteur interne (ne pas modifier, utilisé en récursion)

    Returns:
        Liste de toutes les URLs de produits trouvées dans la catégorie

    Logique:
        - Vérifier si _current_page > max_pages → retourner []
        - Fetch la page avec fetch_page(url)
        - Si fetch échoue → retourner []
        - Parser avec BeautifulSoup
        - Extraire les URLs produits de cette page avec get_product_urls()
        - Chercher l'URL de la page suivante avec get_next_page_url()
        - Si next_url existe → appel récursif scrape_category(next_url, max_pages, _current_page + 1)
        - Combiner les résultats (current_products + next_products)
        - Retourner la liste complète
    """
    # TODO: implémenter la logique récursive
    return []
