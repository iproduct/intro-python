from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title header"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">They lived once upon a time ...</p>
"""

if __name__ == '__main__':
    soup = BeautifulSoup(html_doc, 'html.parser')

    # print(soup.prettify())

    print("soup.title = ", soup.title)
    # <title>The Dormouse's story</title>

    print("soup.title.name = ", soup.title.name)
    # u'title'

    print("soup.title.string = ", soup.title.string)
    # u'The Dormouse's story'

    print("soup.title.parent.name = ", soup.title.parent.name)
    # u'head'

    print("soup.p = ", soup.p)
    # <p class="title"><b>The Dormouse's story</b></p>

    print("soup.p['class'] = ", soup.p['class'])
    # u'title'

    print("soup.a = ", soup.a)
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    print("soup.find_all('a') = ", soup.find_all('a'))
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    # print("soup.find_all('p') = ", soup.find_all('p'))
    print("\nParagraph texts:")
    for p in soup.find_all('p'):
        print(p.get_text())

    print("soup.find(id='link3') = ", soup.find(id="link3"))
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

    print("\nParagraph from 'story' class texts:")
    # print("soup.find_all(class_='link3') = ", soup.find_all("p", class_="story"))
    for p in soup.find_all("p", class_="story"):
        print(p.get_text())