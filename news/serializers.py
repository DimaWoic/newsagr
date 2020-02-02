from rest_framework import serializers
from .models import News, Category

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'published', 'category')