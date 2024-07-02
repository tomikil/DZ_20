from django.urls import path
from django.views.decorators.cache import cache_page

from store.apps import StoreConfig
from store.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    CategoryListView

app_name = StoreConfig.name

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create'),
    path('', ProductListView.as_view(), name='list'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('category/', CategoryListView.as_view(), name='category'),
]
