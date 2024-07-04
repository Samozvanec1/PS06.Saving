import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://tomsk.hh.ru/vacancies/programmist"

driver = webdriver.Firefox()

driver.get(url)

time.sleep(5)

vacanties = driver.find_elements(By.CLASS_NAME, "vacancy-card--z_UXteNo7bRGzxWVcL7y")

parsed_data = []

for vacancy in vacanties:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, "span.vacancy-name--c1Lay3KouCl7XasYakLk").text
        company = vacancy.find_element(By.CSS_SELECTOR, "span.company-info-text--vgvZouLtf8jwBmaD1xgp").text
        sellary = vacancy.find_element(By.CSS_SELECTOR, "span.fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni").text
        link = vacancy.find_element(By.CSS_SELECTOR, "a.bloko-link").get_attribute("href")
        parsed_data.append([title, company, sellary, link])
    except:
        print('ошибка ')
        continue

driver.quit()
with open('hh.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['название вакансии', 'компания', 'зарплата', 'ссылка'])
    writer.writerows(parsed_data)