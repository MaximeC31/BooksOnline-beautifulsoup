from typing import Dict, Any
import re
from urllib.parse import urljoin


def transform_product_data(raw: Dict[str, str]) -> Dict[str, Any]:
    """
    Transformer les valeurs brutes en types utiles pour le CSV :
    - prices (price_including_tax, price_excluding_tax) -> float
    - number_available -> int
    - review_rating -> int (mapping si besoin)
    - image_url -> url absolu (utiliser raw['product_page_url'] + urljoin)

    Retourner un dict prêt à être sérialisé en CSV (valeurs primitives).
    """
    # TODO: implémenter la transformation
    raise NotImplementedError
