from django.core.management import BaseCommand
import json
from store.models import Category, Product
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class Command(BaseCommand):
    @staticmethod
    def json_read_categories():
        list_categories = []
        with open(f'{parent_dir}\\data\\data.json', 'r', encoding='utf-8') as file:
            result = json.load(file)
            for item in result:
                if item['model'] == 'store.category':
                    list_categories.append(item)

            return list_categories

    @staticmethod
    def json_read_products():
        list_products = []
        with open(f'{parent_dir}\\data\\data.json', 'r', encoding='utf-8') as file:
            result = json.load(file)
            for item in result:
                if item['model'] == 'store.product':
                    list_products.append(item)

            return list_products

    def handle(self, *args, **options):
        Product.objects.all().delete()
        # Product.restart_id()
        Category.objects.all().delete()
        Category.restart_id()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['fields']['name'], description=category['fields']['description'])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(product['pk'], product['fields']['name'], product['fields']['description'],
                        product['fields']['images'], product['fields']['category'], product['fields']['price'],
                        product['fields']['created_at'], product['fields']['updated_at'])
            )

        Product.objects.bulk_create(product_for_create)
