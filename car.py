import requests
from bs4 import BeautifulSoup

URL = "https://cars.kg/offers?vendor=57fa24ee2860c45a2a2c0937&model=&year_to=2022&price_to="
HEADERS = {
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
"accept": "*/*",
}
LINK = "https://cars.kg"

def get_html(url, headers):
    response = requests.get(url, headers=headers)
    return response


def get_content_from_html(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    items = soup.find_all("a", class_="catalog-list-item")
    tesla = []
    for item in items:
        tesla.append(
            {
                "title": item.find("span", class_="catalog-item-caption").get_text().replace("\n", ""),
                "run": item.find("span", class_="catalog-item-mileage").get_text().replace("\n", ""),
                "price_doll": item.find("span", class_="catalog-item-price").get_text().replace("\n", ""),
                "price_som": item.find(["price_doll"][], class_="catalog-item-price").get_text().replace("\n", ""),
                "image": item.find("img").get("src"),
            }
        ),
    print(tesla)


def get_result_parse():
    html = get_html(URL, HEADERS)
    if html.status_code == 200:
        get_content_from_html(html.text)

get_result_parse()