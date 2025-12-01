import requests


def fetch_html(url):

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error while getting page content : {e}")
        return None


def main():

    bo_product_url = (
        "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    )

    html_content = fetch_html(bo_product_url)

    if html_content:
        print("Scrape worked!")
    else:
        print("Scrape failed!")


main()
