from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

if __name__ == '__main__':
    soup = BeautifulSoup(html_doc, 'html.parser')

    print(soup.prettify())

    # print("soup.title = ", soup.title)
    # # <title>The Dormouse's story</title>
    #
    # print("soup.title.name = ", soup.title.name)
    # # u'title'
    #
    # print("soup.title.string = ", soup.title.string)
    # # u'The Dormouse's story'
    #
    # print("soup.title.parent.name = ", soup.title.parent.name)
    # # u'head'
    #
    # print("soup.p = ", soup.p)
    # # <p class="title"><b>The Dormouse's story</b></p>
    #
    # print("soup.p['class'] = ", soup.p['class'])
    # # u'title'
    #
    # print("soup.a = ", soup.a)
    # # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    #
    # print("soup.find_all('a') = ", soup.find_all('a'))
    # # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    # #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    # #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
    #
    # print("soup.find(id='link3') = ", soup.find(id="link3"))
    # # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    #
    # soup.title
    # # <title>The Dormouse's story</title>
    #
    # soup.title.name
    # # u'title'
    #
    # soup.title.string
    # # u'The Dormouse's story'
    #
    # soup.title.parent.name
    # # u'head'
    #
    # soup.p
    # # <p class="title"><b>The Dormouse's story</b></p>
    #
    # soup.p['class']
    # # u'title'
    #
    # soup.a
    # # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    #
    # soup.find_all('a')
    # # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    # #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    # #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
    #
    # soup.find(id="link3")
    # # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    #
    # for link in soup.find_all('a'):
    #     print(link.get('href'))
    # # http://example.com/elsie
    # # http://example.com/lacie
    # # http://example.com/tillie
    #
    # print(soup.get_text())
    # # The Dormouse's story
    # #
    # # The Dormouse's story
    # #
    # # Once upon a time there were three little sisters; and their names were
    # # Elsie,
    # # Lacie and
    # # Tillie;
    # # and they lived at the bottom of a well.
    # #
    # ...