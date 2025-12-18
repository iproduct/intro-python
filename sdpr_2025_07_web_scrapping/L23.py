# Scrapping & Crawling web sites


# # BeautifulSoup4 & Requests
# # https://bit.ly/2JQs49Z
# # https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/
# # $ pip install beautifulsoup4
#
import selenium as sele
import bs4 as bs
from urllib.request import urlopen
import requests
# url=requests.get('http://fmi.uni-sofia.bg/')
# url = requests.get('http://vivre.bg/')
url = requests.get('https://www.technomarket.bg/produkti/televizori-nad-50/')
source = url.content
# Алтернативно четене на URL адрес с Beautiful Soap
# url='https://www.technomarket.bg/produkti/televizori-nad-50/'
# source=urlopen(url)

soup = bs.BeautifulSoup(source,'lxml')
# print(soup.title) # връща тага title и текста, който е заключен в него
# print(soup.title.name) # изписва наименованието на тага
print(soup.title.string) # изписва текста, който е заключен в тага title
# print(soup.title.parent.name) # връща името на предходния таг
# print(soup.p) # ще върне първия таг "p" и заключения в него текст
# print(soup.find_all('p')) # ще върне ВСИЧКИ тагове "p" и заключените в тях текстове, под формата на списък
# for paragraph in soup.find_all('p'):
    # paragraph=soup.p
    # print(paragraph.string) # по-общият вариант за извличане на текст от таг,
    # реално ще извлече както обикновения текст, така и този, който се използва като линк за навигация
    # print(str(paragraph.text)) # извлича само обикновения текст
# tmpro=soup.tm-promo-products

for url in soup.find_all('link'):
    urln=url.get('href')
    print(urln)
    # if urln[:5]=="https":
    #     print(urln)
    # else:
    #     print("https://fmi.uni-sofia.bg"+urln)
# print(soup.get_text())

#
# # Mechanize
# # http://wwwsearch.sourceforge.net/mechanize/
# # може да се използва за достъп до сайт с акаунт, и след логване да се скрапва или изпращат данни към сайта
# #import mechanize
#
# # Scrapy, requests, lxml, sqlalchemy,celery
# import scrapy
# import lxml
# import sqlalchemy
# import celery

# <Data>
#     <id>1</id>
#         <name>Ivan</name>
#         <fname>Petrov</fname>
#         <FN>1385</FN>