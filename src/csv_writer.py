import csv
from pathlib import Path
from typing import List, Dict, Any


CSV_COLUMNS = [
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


def write_products_csv(products: List[Dict[str, Any]], out_path: str = "products.csv") -> None:
    """
    Écrire la liste de produits dans out_path (UTF-8, délimiteur virgule).
    - products: liste de dicts contenant les mêmes clés que CSV_COLUMNS
    - Imprimer: print("[LOAD] Écriture CSV ->", out_path)
    """
    # TODO: implémenter l'écriture CSV
    raise NotImplementedError
