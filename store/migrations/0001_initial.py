# Generated by Django 5.0.6 on 2024-06-25 18:14

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Наименование категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Наименование продукта')),
                ('description', models.TextField(verbose_name='Описание продукта')),
                ('images', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Изображение')),
                ('price', models.FloatField(max_length=15, verbose_name='Цена за покупку')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликован')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category', verbose_name='Категория')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['category', 'name'],
                'permissions': [('can_unpublish_product', 'Can unpublish product'), ('change_description_product', 'Can change product description'), ('change_category_product', 'Can change product category')],
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers_version', models.CharField(max_length=50, verbose_name='Номер версии')),
                ('name_version', models.CharField(max_length=150, verbose_name='Название версии')),
                ('sign_version', models.BooleanField(default=False, verbose_name='Активно')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='store.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
