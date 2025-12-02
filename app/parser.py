from bs4 import BeautifulSoup


# --- MICRO-FUNCTIONS ---


def get_upc(soup):
    upc = soup.select_one("table.table.table-striped tr:nth-child(1) > td")
    return upc.text if upc else ""


def get_title(soup):
    title = soup.select_one("h1")
    return title.text if title else ""


def get_price_including_tax(soup):
    ## TODO: corriger les caractères spéciaux, ex: £ et return number ou string ?
    price_including_tax = soup.select_one(
        "table.table.table-striped tr:nth-child(4) > td"
    )
    return price_including_tax.text if price_including_tax else ""


def get_price_excluding_tax(soup):
    ## TODO: corriger les caractères spéciaux, ex: £ et return number ou string ?
    price_excluding_tax = soup.select_one(
        "table.table.table-striped tr:nth-child(3) > td"
    )
    return price_excluding_tax.text if price_excluding_tax else ""


def get_category(soup):
    category = soup.select_one(".breadcrumb li:nth-child(3)")
    return category.text.strip() if category else ""


def get_description(soup):
    description = soup.select_one("#product_description + p")
    return description.text if description else ""


def get_image_url(soup):
    # TODO: reconstruire l'url de relative à absolue
    image = soup.select_one(".item.active > img")
    return image["src"] if image else ""


def get_availability(soup):
    # TODO: extraire le number du innertext de p.instock.availability
    return 0


def get_rating(soup):
    # TODO: récupérer le className complet de star-rating, la deuxième class.
    # Convertir cette class en switch case selon valeur de cette deuxième class.
    return 0


# --- ORCHESTRATION ---


def parse_product(html_content, product_url):
    soup = BeautifulSoup(html_content, "html.parser")

    return {
        "product_page_url": product_url,
        "universal_product_code": get_upc(soup),
        "title": get_title(soup),
        "price_including_tax": get_price_including_tax(soup),
        "price_excluding_tax": get_price_excluding_tax(soup),
        "number_available": get_availability(soup),
        "product_description": get_description(soup),
        "category": get_category(soup),
        "review_rating": get_rating(soup),
        "image_url": get_image_url(soup),
    }
