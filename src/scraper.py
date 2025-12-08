import requests


def fetch_html(url: str) -> str | None:
    try:
        response: requests.Response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error while getting page content : {e}")
        return None
