import requests


def fetch(url: str) -> str | None:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None
