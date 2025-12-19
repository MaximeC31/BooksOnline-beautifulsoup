from pathlib import Path
import re

OUTPUT_IMAGES_DIR = Path("output/images")


def save_image(image_bytes: bytes, file_name: str) -> None:
    OUTPUT_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    sanitized_name = re.sub(r"[^\w\-]", "", "_".join(file_name.lower().split()))
    if not sanitized_name:
        sanitized_name = "unknown"
    print(f"[INFO] Saving image as {sanitized_name}.jpg")

    file_path = OUTPUT_IMAGES_DIR / f"{sanitized_name}.jpg"
    try:
        with file_path.open("wb") as img_file:
            img_file.write(image_bytes)
    except Exception as e:
        print(f"[ERROR] Cannot save image: {e}")
