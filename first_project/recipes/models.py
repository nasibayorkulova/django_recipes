from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


# Первичная модель
class Categories(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# ORM
# Вторичная модель
class Recipes(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    category = models.ForeignKey(Categories, verbose_name='Категория', on_delete=models.CASCADE,
                                 default=1)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    photo = models.ImageField(upload_to='photos/%Y-%m-%d', verbose_name="Картинка")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE,
                                default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
