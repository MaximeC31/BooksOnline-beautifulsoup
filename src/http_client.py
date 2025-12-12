import requests
from typing import Optional


def fetch_page(url: str, timeout: int = 10) -> str:
    """
    Requête GET simple avec timeout (10s par défaut).
    Retourne le HTML brut (str).

    Implémentation attendue par l'utilisateur :
    - utiliser requests.get(url, timeout=timeout)
    - gérer les erreurs réseau (raise ou return "") de manière cohérente
    """
    # TODO: implémenter la logique de requête HTTP
    raise NotImplementedError
