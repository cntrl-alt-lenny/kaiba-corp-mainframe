import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

API_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"


def fetch_card_data(card_name: str) -> dict:
    query = urlencode({"name": card_name})
    url = f"{API_URL}?{query}"
    with urlopen(url) as response:  # nosec B310
        return json.load(response)


def download_image(image_url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with urlopen(image_url) as response:  # nosec B310
        destination.write_bytes(response.read())


def format_stat(value: object) -> str:
    return "N/A" if value is None else str(value)


def main() -> None:
    card_name = input("Enter a Yu-Gi-Oh! card name: ").strip()
    if not card_name:
        print("Card name cannot be empty.")
        return

    try:
        payload = fetch_card_data(card_name)
    except HTTPError as error:
        print(f"API request failed ({error.code}).")
        return
    except URLError as error:
        print(f"Network error: {error.reason}.")
        return

    cards = payload.get("data", [])
    if not cards:
        print("No cards found.")
        return

    card = cards[0]
    name = card.get("name", "Unknown")
    card_type = card.get("type", "Unknown")
    atk = format_stat(card.get("atk"))
    defense = format_stat(card.get("def"))

    print(f"Name: {name}")
    print(f"Type: {card_type}")
    print(f"ATK/DEF: {atk}/{defense}")

    images = card.get("card_images", [])
    if not images:
        print("No images available to download.")
        return

    image_url = images[0].get("image_url")
    image_id = images[0].get("id")
    if not image_url or not image_id:
        print("Image data is incomplete.")
        return

    output_dir = Path(__file__).resolve().parent.parent / "card_images"
    output_file = output_dir / f"{image_id}.jpg"

    try:
        download_image(image_url, output_file)
    except HTTPError as error:
        print(f"Image download failed ({error.code}).")
        return
    except URLError as error:
        print(f"Image download error: {error.reason}.")
        return

    print(f"Image downloaded to: {output_file}")


if __name__ == "__main__":
    main()
