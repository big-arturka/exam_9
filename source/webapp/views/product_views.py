from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy

from webapp.forms import ProductForm
from webapp.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(ListView):
    template_name = 'product/index.html'
    context_object_name = 'products'
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return Product.objects.all()


class ProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product
    paginate_review_by = 2
    paginate_review_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.object.review_products.all()
        context['reviews'] = reviews

        return context


class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'product/product_create.html'
    form_class = ProductForm
    model = Product
    permission_required = 'webapp.add_product'

    # def post(self, request, *args, **kwargs):
    #     form = ProductForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'product/product_update.html'
    form_class = ProductForm
    model = Product
    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    success_url = reverse_lazy('index')
    permission_required = 'webapp.delete_product'
