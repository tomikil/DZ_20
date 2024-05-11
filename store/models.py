from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=70, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание категории', **NULLABLE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=70, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание продукта', **NULLABLE)
    images = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products')
    price = models.FloatField(max_length=15, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(verbose_name='Дата создания')
    updated_at = models.DateTimeField(**NULLABLE, verbose_name='Дата последнего изменения')
    manufactured_at = models.DateTimeField(**NULLABLE, verbose_name='Дата производства продукта')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']

    def __str__(self):
        return self.name
