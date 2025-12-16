import csv
from pathlib import Path
from .constants import PRODUCT_FIELDS, ProductTransformed

OUTPUT_DATA_DIR = Path("output/data")


def write_products_category(products: list[ProductTransformed]) -> None:
    try:
        category_raw = str(products[0]["category"])
        category_name = "_".join(category_raw.lower().split())
        OUTPUT_DATA_DIR.mkdir(parents=True, exist_ok=True)
        out_path = OUTPUT_DATA_DIR / f"{category_name}.csv"

        with out_path.open("w", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=PRODUCT_FIELDS)
            writer.writeheader()
            writer.writerows(products)

        print(f"[LOAD] Writing {category_name}.csv - {len(products)} products")
    except Exception as e:
        print(f"[ERROR] Cannot write CSV: {e}")
        return
