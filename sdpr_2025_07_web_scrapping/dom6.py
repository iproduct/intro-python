from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import csv
import time

firefox_options = Options()
firefox_options.add_argument("--headless")

browser = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=firefox_options
)

start_url = "https://www.emag.bg/laptopi/c?type=category"
browser.get(start_url)
time.sleep(6)

links = []
cards = browser.find_elements(By.CSS_SELECTOR, "a.card-v2-title")

for card in cards:
    if len(links) == 10:
        break
    link = card.get_attribute("href")
    if link:
        links.append(link)

print("Брой намерени продукти:", len(links))

headers = [
    "Марка", "Модел", "Процесор", "RAM", "Видеокарта",
    "Екран (inch)", "Диск", "Обем диск",
    "Батерия", "Тегло (кг)", "Цена", "Промо цена", "Линк"
]

with open("emag_laptops_modified.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for product_url in links:
        browser.get(product_url)
        time.sleep(4)

        row = [""] * len(headers)
        row[-1] = product_url

        try:
            row[1] = browser.find_element(By.TAG_NAME, "h1").text
        except Exception as e:
            print(f"Грешка при заглавие: {e}")
            continue

        try:
            specs_rows = browser.find_elements(By.CSS_SELECTOR, "table.specifications-table tr")
        except Exception as e:
            print(f"Грешка при таблицата със спецификации: {e}")
            specs_rows = []

        for s in specs_rows:
            try:
                cells = s.find_elements(By.TAG_NAME, "td")
                if len(cells) != 2:
                    continue

                key = cells[0].text.lower()
                value = cells[1].text.strip()

                if "производител" in key:
                    row[0] = value
                elif "процесор" in key:
                    row[2] = value
                elif "памет" in key:
                    row[3] = value
                elif "видео" in key:
                    row[4] = value
                elif "диагонал" in key:
                    row[5] = value
                elif "тип съхранение" in key:
                    row[6] = value
                elif "капацитет съхранение" in key:
                    row[7] = value
                elif "батерия" in key:
                    row[8] = value
                elif "тегло" in key:
                    row[9] = value
            except Exception as e:
                print(f"Грешка при обработка на ред от таблицата: {e}")
                continue

        try:
            row[10] = browser.find_element(By.CSS_SELECTOR, "p.product-new-price").text
        except Exception as e:
            print(f"Грешка при нова цена: {e}")
            row[10] = ""

        try:
            row[11] = browser.find_element(By.CSS_SELECTOR, "p.product-old-price").text
        except Exception:
            row[11] = ""

        try:
            writer.writerow(row)
        except Exception as e:
            print(f"Грешка при запис в CSV: {e}")
            continue

browser.quit()
print("Файлът emag_laptops_modified.csv е създаден успешно")