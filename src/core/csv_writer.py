import csv
from pathlib import Path
from typing import List
from src.constants.constants import CSV_HEADERS, ProductData


def write_products_to_csv(products: List[ProductData], filename: str) -> None:
    try:
        output_path = Path(filename)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with output_path.open(mode="w", encoding="utf-8-sig", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=CSV_HEADERS, restval="N/A")
            writer.writeheader()
            writer.writerows(products)

        print(f"CSV exporté avec succès : {filename} ({len(products)} produits)")

    except IOError as e:
        print(f"Erreur critique lors de l'écriture du CSV {filename} : {e}")
