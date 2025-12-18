# Скрапване на динамични сайтове
# ИЗточник: https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f
# Трябва да се инсталира драйвера geckodriver за Mozilla Firefox и да се добави в пътя:
# https://github.com/mozilla/geckodriver/releases

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import pandas as pd


# specify the url
urlpage = 'https://groceries.asda.com/search/yogurt'
print(urlpage)
driver = webdriver.Firefox(executable_path = '/Users/valerina/Downloads/geckodriver')
# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(30)

# find elements by xpath
# Извличане на пътя с таговете, които ни трябват:
# Отваряме страницата в браузъра, маркира някой от продуктите и с десен клик избираме "Inspect Element"
# След това, върху маркирания текст избираме отново десен клик, но този път "XPATH"
# element представлява точно такова копие на пътя
results = driver.find_elements_by_xpath("//*[@class=' co-product-list__main-cntr']//*[@class=' co-item ']//*[@class='co-product']//*[@class='co-item__title-container']//*[@class='co-product__title']")
print('Number of results', len(results))
# create empty array to store data
data = []
# loop over results
for result in results:
    product_name = result.text
    link = result.find_element_by_tag_name('a')
    product_link = link.get_attribute("href")
    # append dict to array
    data.append({"product" : product_name, "link" : product_link})
# close driver
driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)
# write to csv
df.to_csv('asdaYogurtLink.csv')