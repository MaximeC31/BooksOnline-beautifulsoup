from src.scraper import scrape_site


if __name__ == "__main__":
    MAIN_URL: str = "https://books.toscrape.com"
    scrape_site(MAIN_URL)
