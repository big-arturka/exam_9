from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import ReviewForm
from webapp.models import Review, Product
from django.views.generic import CreateView, UpdateView, DeleteView


class ReviewCreateView(LoginRequiredMixin, CreateView):
    template_name = 'review/review_create.html'
    form_class = ReviewForm
    model = Review
    permission_required = 'webapp.add_review'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.author = self.request.user
        review.save()
        return redirect('product_view', pk=product.pk)

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.product.pk})


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'review/review_update.html'
    form_class = ReviewForm
    model = Review
    permission_required = 'webapp.change_review'

    def has_permission(self):
        review = self.get_object()
        return super().has_permission() or self.request.user == review.author

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.product.pk})


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'review/review_delete.html'
    model = Review
    permission_required = 'webapp.delete_review'

    def has_permission(self):
        review = self.get_object()
        return super().has_permission() or self.request.user == review.author

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.product.pk})