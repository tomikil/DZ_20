from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from store.models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'images', 'category', 'price', 'created_at')
    success_url = reverse_lazy('store:list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'images', 'category', 'price', 'created_at')
    success_url = reverse_lazy('store:list')


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('blogs:list')
