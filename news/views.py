from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from .models import News, Category


def by_category(request, category_id):
    news = News.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'news': news, 'categories': categories, 'current_category': current_category}
    return render(request, 'news/by_category.html', context)


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {'news': news, 'categories': categories}
    return render(request, 'news/index.html', context)