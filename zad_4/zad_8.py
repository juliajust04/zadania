import argparse
import requests

from zad_7 import Brewery


def get_breweries(city: str | None = None) -> list[Brewery]:
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": 20}

    if city:
        params["by_city"] = city

    response = requests.get(
        url,
        params=params,
        timeout=30
    )
    response.raise_for_status()

    data = response.json()
    return [Brewery(**item) for item in data]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", type=str)
    args = parser.parse_args()

    breweries = get_breweries(args.city)

    for brewery in breweries:
        print(brewery)

    print(f"Liczba browarów: {len(breweries)}")


if __name__ == "__main__":
    main()