from django.db import models, connection


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=70, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание категории', **NULLABLE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    @classmethod
    def restart_id(cls):
        with connection.cursor() as cur:
            cur.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')


class Product(models.Model):
    name = models.CharField(max_length=70, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание продукта')
    images = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products')
    price = models.FloatField(max_length=15, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(verbose_name='Дата создания')
    updated_at = models.DateTimeField(**NULLABLE, verbose_name='Дата последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, verbose_name='Продукт', related_name='product',
                                on_delete=models.SET_NULL, null=True, blank=True)
    numbers_version = models.CharField(max_length=50, verbose_name='Номер версии')
    name_version = models.CharField(max_length=150, verbose_name='Название версии')
    sign_version = models.BooleanField(verbose_name='Активно', default=False)

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


    def __str__(self):
        return self.numbers_version