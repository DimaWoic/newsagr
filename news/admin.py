from django.contrib import admin

# Register your models here.
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ('published', 'category', 'title', 'description')
    list_display_links = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
