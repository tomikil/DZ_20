from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from store.forms import ProductForm, VersionForm, ProductModeratorForm
from store.models import Product, Version


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('store:list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('store:view', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('store.can_unpublish_product') and user.has_perm('store.change_description_product') and user.has_perm('store.change_category_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset.filter(is_published=True)


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('store:list')
