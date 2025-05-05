# coding=utf-8

from django.db import models


class Book(models.Model):
    id = models.BigAutoField(primary_key=True) # явное указание первичного ключа
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации', auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.author} ({self.pub_date})"

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['pub_date'] # Сортировка по умолчанию
