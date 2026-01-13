import requests
import bs4 as bs

if __name__=="__main__":
    res = requests.get('https://fmi.uni-sofia.bg/bg/departments/6222/staff')
    print(res.status_code)

    soup = bs.BeautifulSoup(res.text)
    print(soup.prettify())

    for elem in soup.find_all(class_="views-row"):
        # print(elem.prettify())
        # print(elem.div.a)
        print(f"| {elem.div.a.get_text():40} | {elem.div.a.attrs['href']:50} |")