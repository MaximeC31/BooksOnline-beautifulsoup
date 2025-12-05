import requests
from typing import Optional


def fetch_html(url: str) -> Optional[str]:
    try:
        response: requests.Response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error while getting page content : {e}")
        return None
