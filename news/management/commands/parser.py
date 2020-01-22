from datetime import datetime
from bs4 import BeautifulSoup
import requests
import time

from django.core.management.base import BaseCommand, CommandError
from news.models import News, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        def parser1(url):
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            item_xml = soup.find_all('item')[0]
            get_title = item_xml.find('title').text
            get_category = item_xml.find('category').text
            get_link = item_xml.find('guid').text
            icon = soup.find('url').text

            list_category = []
            list_title = []

            for c in Category.objects.all():
                list_category.append(c.name)

            if get_category in list_category:
                print(get_category, " Категория существует")
            elif get_category not in list_category:
                new_category = Category()
                new_category.name = get_category
                new_category.save()
                print("Добавлена новая категория ", get_category)

            for t in News.objects.all():
                list_title.append(t.title)

            if get_title in list_title:
                print("новость существует в базе")
            elif get_title not in list_title:
                print("Добавление новой новости")
                new_news = News()
                new_news.title = get_title
                new_news.category_id = Category.objects.get(name=get_category).pk
                new_news.url_source = get_link
                new_news.icon = icon
                new_news.save()

        def vestiru():
            url = 'https://www.vesti.ru/vesti.rss'
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            item_xml = soup.find_all('item')[0]
            get_title = item_xml.find('title').text
            get_category = item_xml.find('category').text
            get_link = item_xml.find('amplink').text
            icon = 'https://www.vesti.ru/i/logo_new.png'

            list_category = []
            list_title = []

            for c in Category.objects.all():
                list_category.append(c.name)

            if get_category in list_category:
                print(get_category, " Категория существует")
            elif get_category not in list_category:
                new_category = Category()
                new_category.name = get_category
                new_category.save()
                print("Добавлена новая категория ", get_category)

            for t in News.objects.all():
                list_title.append(t.title)

            if get_title in list_title:
                print("новость существует в базе")
            elif get_title not in list_title:
                print("Добавление новой новости")
                new_news = News()
                new_news.title = get_title
                new_news.category_id = Category.objects.get(name=get_category).pk
                new_news.url_source = get_link
                new_news.icon = icon
                new_news.save()





        vestiru()
        urls = ['https://lenta.ru/rss', 'https://www.interfax.ru/rss.asp', 'https://www.gazeta.ru/export/rss/first.xml']

        for url in urls:
            parser1(url)