import requests as req # установка библиотеки requests для работы с сайтом
from bs4 import BeautifulSoup # установка библиотеки bs4 для парсинга

url = "https://google.com" # URL сайта на котором будем парсить

response = req.get(url) # получаем данные с сайта
soup = BeautifulSoup(response.text, "html.parser") # парсим данные с сайта

rows = soup.find_all("tr") # находимируемся по сайту и ищем все теги tr
data = [] # создаем пустой список

for row in rows:
    cols = row.find_all("td") # находимируемся по сайту и ищем все теги td
    cleaned_cols = [col.text.strip() for col in cols] # удаляем лишние пробелы при парсинге
    data.append(cleaned_cols) # добавляем данные в список данных


