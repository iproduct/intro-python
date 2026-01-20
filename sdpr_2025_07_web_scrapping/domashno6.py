from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
import time

options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

URL = "https://www.emag.bg/laptopi/c?ref=hp_menu_quick-nav_1_1&type=category"
driver.get(URL)
time.sleep(5)

product_links = []

product_elements = driver.find_elements(By.CSS_SELECTOR, "a.card-v2-title")

for el in product_elements[:10]:
    href = el.get_attribute("href")
    if href:
        product_links.append(href)

print(f"Намерени продукти: {len(product_links)}")

data = []

for link in product_links:
    driver.get(link)
    time.sleep(4)

    try:
        title = driver.find_element(By.TAG_NAME, "h1").text
    except:
        continue

    specs = driver.find_elements(By.CSS_SELECTOR, "table.specifications-table tr")
    spec_dict = {}

    for spec in specs:
        tds = spec.find_elements(By.TAG_NAME, "td")
        if len(tds) == 2:
            spec_dict[tds[0].text.strip()] = tds[1].text.strip()

    try:
        price = driver.find_element(By.CSS_SELECTOR, "p.product-new-price").text
    except:
        price = ""

    try:
        promo_price = driver.find_element(By.CSS_SELECTOR, "p.product-old-price").text
    except:
        promo_price = price

    data.append({
        "Марка": spec_dict.get("Производител", ""),
        "Модел": title,
        "Процесор": spec_dict.get("Процесор", ""),
        "RAM": spec_dict.get("Капацитет памет", ""),
        "Видеокарта": spec_dict.get("Видео карта", ""),
        "Екран (inch)": spec_dict.get("Диагонал дисплей", ""),
        "Диск": spec_dict.get("Тип съхранение", ""),
        "Обем диск": spec_dict.get("Капацитет съхранение", ""),
        "Батерия": spec_dict.get("Батерия", ""),
        "Тегло (кг)": spec_dict.get("Тегло", ""),
        "Цена": price,
        "Промо цена": promo_price,
        "Линк": link
    })
    print({
        "Марка": spec_dict.get("Производител", ""),
        "Модел": title,
        "Процесор": spec_dict.get("Процесор", ""),
        "RAM": spec_dict.get("Капацитет памет", ""),
        "Видеокарта": spec_dict.get("Видео карта", ""),
        "Екран (inch)": spec_dict.get("Диагонал дисплей", ""),
        "Диск": spec_dict.get("Тип съхранение", ""),
        "Обем диск": spec_dict.get("Капацитет съхранение", ""),
        "Батерия": spec_dict.get("Батерия", ""),
        "Тегло (кг)": spec_dict.get("Тегло", ""),
        "Цена": price,
        "Промо цена": promo_price,
        "Линк": link
    })

driver.quit()
pd.set_option('display.max_columns', None)
df = pd.DataFrame(data)
print(df)
df.to_csv("emag_gaming_laptops.csv", index=False, encoding="utf-8-sig")

print("Файлът emag_gaming_laptops.csv е създаден")
print(f"Записани продукти: {len(df)}")