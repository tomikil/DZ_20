from django.core.cache import cache

from config.settings import CACHE_ENABLED
from store.models import Category


def get_category_from_cache():
    """
    Получает данные по Категориям из кеша, если кеш пустой то возвращает из БД
    """
    queryset = Category.objects.all()
    if CACHE_ENABLED:
        key = 'category'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)
        return cache_data
    return queryset