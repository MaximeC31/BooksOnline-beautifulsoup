from bs4 import BeautifulSoup
from typing import Dict
from urllib.parse import urljoin


def extract_product_data(html: str, page_url: str) -> Dict[str, str]:
    """
    Parser le HTML et extraire les champs bruts (strings) suivants :
    - product_page_url
    - universal_product_code (upc)
    - title
    - price_including_tax
    - price_excluding_tax
    - number_available
    - product_description
    - category
    - review_rating
    - image_url

    Doit imprimer : print("[EXTRACT] Récupération produit...")
    Retourner un dict avec ces clés (valeurs brutes telles qu'extraites).
    """
    # TODO: implémenter le parsing avec BeautifulSoup
    print("[EXTRACT] Récupération produit...")
    raise NotImplementedError
