from django.urls import path
from store.apps import StoreConfig
from store.views import index, product

app_name = StoreConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:pk>/', product, name='product')
]
