# Скрапване на динамични сайтове
# Източник: https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f
# Трябва да се инсталира драйвера geckodriver за Mozilla Firefox и да се добави в пътя:
# https://github.com/mozilla/geckodriver/releases

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options

# specify the url
urlpage = 'https://www.technomarket.bg/produkti/televizor'
print(urlpage)
# Този път е специфичен, и зависи от настройките, които сте направили за драйвера
# path='/Users/valerina/Downloads/geckodriver'
# driver = webdriver.Firefox(executable_path = path)
# driver = webdriver.Chrome()

# 1. Create ChromeOptions instance
options = Options()

# 2. Add the 'headless=new' argument for the new headless mode
# options.add_argument("--headless=new")

# Optional: Add other arguments like disabling GPU for performance
# options.add_argument("--disable-gpu")

# 3. Initialize ChromeDriver with the options
driver = webdriver.Chrome(options=options)

# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(30)
# Определяне на броя на артикулите, броя на страниците за обхождане и броя на артикулите на последна страница
# total_items

# Извличане на първата страница с резултати:
results=driver.find_elements("tag name", 'tm-product-item') # 34 резултата=24+10
results=results[:24] # защото на страницата се визуализират по 24 резултата, останалите 10 са други
tex='Number of results'
print(tex, len(results))
# create empty array to store data
data = []
# loop over results
for result in results:
    tex=result.text.split("\n")
    if len(tex)<5:
        tex.insert(0,0)
        tex.append(tex[3])
    tex.pop(2)

    rl = result.find_elements("tag name", 'a')[0]
    link = rl.get_attribute("href")
    # append dict to array
    data.append({"TV" :tex[1],"Стара цена":tex[2],"Клас ЕЕ":tex[3],"Модел":tex[0],"Линк" : link})
# # close driver
driver.quit()

# # save to pandas dataframe
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

df = pd.DataFrame(data)
print(df)
# #
# # # # write to csv
df.to_csv('Promo_TechnoMarket.csv')