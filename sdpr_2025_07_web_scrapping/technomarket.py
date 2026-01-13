import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    urlpage = 'https://www.technomarket.bg/produkti/televizor'
    print(urlpage)
    resp = requests.get(urlpage)
    soup = BeautifulSoup(resp.content, 'html.parser')
    # print(soup.prettify())

    for elem in soup.find_all("tm-product-item"):
        overview = elem.find(class_="overview")
        # print(elem.find(class_='euro_price').text)
        # print(f"| {overview.find(class_='type').text:10}")
        print(f"| {overview.find(class_='type').text} | {overview.find(class_='brand').text:10s} | {overview.find(class_='name').text:40s} | "
              f"{elem.find(class_='euro_price').text[:-1]:10.10s} |")

