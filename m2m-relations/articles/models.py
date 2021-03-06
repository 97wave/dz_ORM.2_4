from django.db import models
from .settings_local import *


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):

    name = models.CharField(max_length=25, verbose_name='Название')
    relation = models.ManyToManyField(Article, through='Relationship', verbose_name='Темы статьи')
    
    class Meta:
        verbose_name = 'Тема статьи'
        verbose_name_plural = 'Темы статьи'
        ordering = ['-name']

    def __str__(self):
        return self.tag


class Relationship(models.Model):
    
    articles = models.ForeignKey(Article, related_name='scopes', on_delete=models.CASCADE, verbose_name='Статья')
    tag = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name='Раздел')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Тема статьи'
        verbose_name_plural = 'Темы статьи'
        ordering = ['-is_main']

