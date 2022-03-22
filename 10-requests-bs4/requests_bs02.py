import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    r = requests.get('https://docs.python-requests.org/en/latest/user/quickstart/')
    # print(r.text[:1000])

    soup = BeautifulSoup(r.text, 'html.parser')

    # print(soup.prettify())

    print("soup.title = ", soup.title)

    print("soup.title.name = ", soup.title.name)

    print("soup.title.string = ", soup.title.string)

    print("soup.title.parent.name = ", soup.title.parent.name)

    print("soup.p = ", soup.p)

    print("soup.a = ", soup.a)

    for link in soup.find_all('a'):
        print(link, "->", link.get('href'))

    print("\nTEXT CONTENT:")
    lines = [line.strip() for line in soup.body.get_text().split("\n") if len(line.strip()) > 0]
    for l in lines:
        print(l)
