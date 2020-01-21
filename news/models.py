from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='категория')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['-name']

    def __str__(self):
        return self.name


class News(models.Model):
    published = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300, verbose_name='Заголовок', blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', blank=True, default='', related_name='entries', on_delete=models.CASCADE)
    icon = models.ImageField(verbose_name='иконка', null=True)
    description = models.TextField(editable=False, verbose_name='Текст новости', blank=True, null=True)
    url_source = models.CharField(max_length=1000, verbose_name='ссылка на ресурс', blank=True, null=True)

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering  = ['-published']

    def __str__(self):
        return self.title