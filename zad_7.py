from dataclasses import dataclass

import requests


@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: str | None
    address_2: str | None
    address_3: str | None
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: float | None
    latitude: float | None
    phone: str | None
    website_url: str | None
    state: str
    street: str | None

    def __str__(self) -> str:
        return (
            f"Nazwa: {self.name}, "
            f"Typ: {self.brewery_type}, "
            f"Miasto: {self.city}, "
            f"Stan: {self.state_province}, "
            f"Kraj: {self.country}, "
            f"Adres: {self.address_1}, "
            f"Kod pocztowy: {self.postal_code}, "
            f"Telefon: {self.phone}, "
            f"Strona: {self.website_url}"
        )


def get_breweries() -> list[Brewery]:
    url = "https://api.openbrewerydb.org/v1/breweries"
    response = requests.get(
        url,
        params={"per_page": 20},
        timeout=30
    )
    response.raise_for_status()

    data = response.json()
    return [Brewery(**item) for item in data]


if __name__ == "__main__":
    breweries = get_breweries()

    for brewery in breweries:
        print(brewery)

    print(f"Liczba browarów: {len(breweries)}")
