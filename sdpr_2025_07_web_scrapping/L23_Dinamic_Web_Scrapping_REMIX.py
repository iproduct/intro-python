# Целият код е разработен за смесен динамичен уеб сайт. Това означава, че сайтът използва както java script
# за да генерира рязултата от заявката, така и метода get() за формиране на самата заявка
# Основният ни URL адрес е: 'https://remixshop.com/bg/'
# Имаме възможност за програмно поодаване на различните начални url-и за различните категории продукти:
# към него може да се залепи: 'womens-clothes', 'mens-clothes', 'bags', 'accessories', 'shoes','child-clothes'
# преди това залепване може да стои друго залепване: 'outlet' или 'secondhand' или 'pre', като последното отговаря на "следващ сезон"
# след категорията мъжки/дамски дрехи може да се сложи уточнение (да се залепи) типа на дрехата или аксесоара
# Пример 1: 'https://remixshop.com/bg/womens-clothes/dresses' - дамски дрехи/рокли
# Пример 2: 'https://remixshop.com/bg/outlet/womens-clothes/dresses' - нови дамски дрехи/рокли
# Пример 3: 'https://remixshop.com/bg/womens-clothes/dresses/summer-dresses' - дамски дрехи/рокли/летни рокли
# Пример 4: 'https://remixshop.com/bg/outlet/womens-clothes/dresses/summer-dresses' - нови дамски дрехи/рокли/летни рокли
# Всички тези категории и под-категории можем да извлечем програмно, за залепването е елеменетарно залепване на стрингове
# Самите категории и подкатегории могат да бъдат организирани например в речници, като ключовете отговарят на категорията,
# а стойностите могат да бъдат от тип списък и да включват подкатегориите
# Всички останали филтри за размер, цвят, състояние, материя, сезон, кога е добавено, промоции, ценови диапазон се залагат
# като параметри в променливата filter
# Познаването на категориите и филтрите позволява добавянето на нови входни параметри за функцията, която обработва
# една страница от резултатите scrap_by_page()
# Интересуват ни следните тагове и атрибути:
# <a>: text, href; <img>: alt


# Импортване на необходимите библиотеки:
import requests
from selenium import webdriver
import time
import pandas as pd
import random as rd

data = []
def loading_url(api_url,filter_params=dict()):
    if len(filter_params)==0:
        respons = requests.get(api_url)
    else:
        respons = requests.get(api_url, params=filter_params)
    urlpage = respons.url
    print(urlpage)
    driver = webdriver.Firefox(executable_path='/Users/valerina/Downloads/geckodriver')
    # Извличане на страницата
    driver.get(urlpage)
    # Обхождане на страницата от горе до долу
    # Този ред не се променя и е постоянен
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    # Забавяне с 30 секунди, за да може да се свали цялата информация за страницата
    time.sleep(30)
    # # Показване на съдържанието на страницата:
    # if respons.headers['content-type'][:9] == "text/html":
    #     print(respons.text)
    # else:
    #     print(respons.json())
    return driver

def get_cathegories():
    # Функцията извлича всички възможни категории
    # Връща dataframe с категории, подкатегории и абсолютни линкове от типа на тези в Примерите по-горе
    main_url='https://remixshop.com/bg/'
    driver=loading_url(main_url)
    tag_a=driver.find_elements_by_tag_name('a')
    cathegories_all=[]
    cats=['womens-clothes', 'mens-clothes', 'bags', 'accessories', 'shoes','child-clothes']
    for a in tag_a:
        link=a.get_attribute('href')
        cat=str(link)
        cat=cat.split("/")
        try:
            if cat[-2] in cats:
                cathegories_all.append({"main_cat":"All","cat":cat[-2],"sub-cat":cat[-1],"full_sub_cat_link":link})
        except:
            pass
    driver.quit()
    cathegories_outlet=[]
    cathegories_secondhand=[]
    cathegories_pre=[]
    for cat_all in cathegories_all:
        tmp_link=str(cat_all["full_sub_cat_link"])
        break_point_in_link=tmp_link.find("/bg/")+4

        secondhand_link=tmp_link[:break_point_in_link]+"secondhand/"+tmp_link[break_point_in_link:]
        cathegories_secondhand.append({"main_cat":"Second Hand","cat":cat_all["cat"],"sub-cat":cat_all["sub-cat"],"full_sub_cat_link":secondhand_link})

        outlet_link = tmp_link[:break_point_in_link] + "outlet/" + tmp_link[break_point_in_link:]
        cathegories_outlet.append({"main_cat": "Outlet", "cat": cat_all["cat"], "sub-cat": cat_all["sub-cat"],
                                   "full_sub_cat_link": outlet_link})

        pre_link = tmp_link[:break_point_in_link] + "pre/" + tmp_link[break_point_in_link:]
        cathegories_pre.append({"main_cat": "Next season", "cat": cat_all["cat"], "sub-cat": cat_all["sub-cat"],
                                   "full_sub_cat_link": pre_link})

    df_1 = pd.DataFrame(cathegories_all)
    df_2 = pd.DataFrame(cathegories_outlet)
    df_3 = pd.DataFrame(cathegories_secondhand)
    df_4 = pd.DataFrame(cathegories_pre)

    main_cats_2=['outlet','secondhand','pre','']
    df_5=[]
    # Добавяне на линковете с основните категории:
    for mc2 in main_cats_2:
        for cat in cats:
            if mc2=='':
                link = main_url + cat
                df_5.append({"main_cat":"All","cat":cat,"sub-cat":'',"full_sub_cat_link":link})
            else:
                link = main_url + mc2 + "/" + cat
                df_5.append({"main_cat": mc2, "cat": cat, "sub-cat": '', "full_sub_cat_link": link})

    df_5 = pd.DataFrame(df_5)
    df=pd.concat([df_1,df_2,df_3,df_4,df_5])
    df.to_csv('Remix_categories.csv')
    return df
cat_links=get_cathegories()

# Взимане на произволна категория с подкатегория
random_url_row=rd.randint(0,cat_links.shape[0])
random_url=cat_links.iat[random_url_row,-1]

# Filter settings:
filter=dict()
# filter={'size':'S','last':1}
# last=1 означава "добавени днес"
# last=2 означава "добавени последните 3 дни"

# loaded_page=loading_url(random_url,filter) # когато имаме някакъв filter
loaded_page=loading_url(random_url) # когато нямаме зададен filter

def get_number_of_pages_and_items(loaded_page):
    # Извличане на общия брой резултати по конкретното търсене:
    string_results_as_list=loaded_page.find_elements_by_class_name("text")[1].text.split(" ")
    if len(string_results_as_list)<=6:
        # <span class="shownText"></span> 1 - 30 от 157 резултата
        number_of_results=int(string_results_as_list[4])
    else:
        # <span class="shownText"></span> 1 - 30 от 6 157 резултата, т.е. при повече от 999 резултата:
        # при използване на split(" ") числото 6157, ще бъде разделено на два стринга: "6" и "157"
        # затова ги залепяме и резултата обръщаме в integer
        number_of_results=int(string_results_as_list[4]+string_results_as_list[5])
    items_per_page=int(string_results_as_list[2])
    number_of_pages=number_of_results//items_per_page+1
    data={"Общо артикули":number_of_results,"Брой страници":number_of_pages,"Артикули на страница":items_per_page}
    print(data)
    loaded_page.quit()
    return data
pages=get_number_of_pages_and_items(loaded_page)["Брой страници"]

def scrap_by_page(api_url, page_number):
    # Функцията обработва конкретна страница с резултати от всички страници, които съответстват на дадена заявка по
    # конкретните параметри (филтри)
    global data
    global filter
    filter['page']=str(page_number)
    print(filter)
    load_page = loading_url(api_url,filter)

    results=load_page.find_elements_by_class_name('product-box-content')
    for result in results:
        rl = result.find_elements_by_tag_name('a')[0]
        link = rl.get_attribute("href")
        info=result.text.split("\n")
        info2=rl.find_element_by_tag_name("img")
        # "alt" се явява атрибут (attribute) или свойство (property) на тага "img"
        alt=info2.get_attribute("alt").split(",") # alt става списъсък
            # alt[0] е марката - имаме я таг "a" => да пропуснем
            # alt[1] е Размера - имаме от таг "a" => да пропуснем
            # alt[2] е цвета
            # всичко, което е между alt[2] и alt[-1] е типа на материята
            # alt[-1] и alt[-2] отговарят на цената - имаме от таг "a" => да пропуснем, защото:
            # десетичният разделител е запетая и разделя цената на две части!
        if len(alt)>4:
            textile=','.join(alt[3:-2])
        # Обработваме стринга с информацията от тага "а":
        if len(info)<8:
            info.insert(0, 0)
            info.insert(5,'0%')
            info.insert(6,info[4])
        # append dict to array
        data.append({"Марка":info[1],"Размер":info[2],"Цвят":alt[2][5:],"Материя":textile,"Цена":info[6],"link":link})
    # close driver
    load_page.quit()

# Извличане на информацията за продуктите от всички страници, които връща заявката по определените критерии
for p in range(1,pages+1):
    scrap_by_page(random_url,p)
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)

# write to csv
df.to_csv('Remix.csv')
