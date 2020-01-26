from datetime import datetime
from bs4 import BeautifulSoup
import requests
import time

from django.core.management.base import BaseCommand, CommandError
from news.models import News, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        #lenta.ru
        def parser1():
            url = 'https://lenta.ru/rss'
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            item_xml = soup.find_all('item')[0]
            get_title = item_xml.find('title').text
            get_category = item_xml.find('category').text
            get_link = item_xml.find('guid').text
            icon = 'https://apke.ru/images/icon/14911692214102_icon.png'

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

        #interfax
        def parser2():
            url = 'https://www.interfax.ru/rss.asp'
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            item_xml = soup.find_all('item')[0]
            get_title = item_xml.find('title').text
            get_category = item_xml.find('category').text
            get_link = item_xml.find('guid').text
            icon = 'https://www.interfax.ru/img/interfax_icon_300.png'

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

        #gazeta.ru
        def parser3():
            url = 'https://www.gazeta.ru/export/rss/first.xml'
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            item_xml = soup.find_all('item')[0]
            get_title = item_xml.find('title').text
            get_category = item_xml.find('category').text
            get_link = item_xml.find('guid').text
            icon = 'https://www.gazeta.ru/i/gazeta_og_image.jpg'

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

        #vestiru
        def parser4():
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

        while True:

            parser1()
            parser2()
            parser3()
            parser4()
            time.sleep(300)