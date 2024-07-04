import scrapy
import csv


class DzSpider(scrapy.Spider):
    name = "DZ"
    allowed_domains = ["divan.ru"] # разрешенные домены для парсинга
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self,  response):  # этот метод отвечает за парсинг каждой страницы сайта поиска светильников. self - это объект класса. response - это ответ сервера поиска светильников
        lamps = response.css('div._Ud0k')  # этот метод ищет все div с атрибутом Ud0k (диваны и кресла) внутри div с атрибутом Ud0k (диваны и кресла)
        vse_syuda = []
        for lamp in lamps:  # перебирает все div с атрибутом Ud0k (диваны и кресла) внутри div с атрибутом Ud0k (диваны и кресла)

            name = lamp.css("div.lsooF span::text").get()
            price = lamp.css("div.pY3d2 span::text").get()
            url = lamp.css("a").attrib['href']

            vse_syuda.append([name, price, url])

        with open('light.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['наименование товара', 'цена', 'ссылка'])
            writer.writerows(vse_syuda)