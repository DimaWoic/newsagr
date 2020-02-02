from django.shortcuts import render
from django.http import JsonResponse
from .models import News, Category
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


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

@api_view(['GET'])
def api_news(request):
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)