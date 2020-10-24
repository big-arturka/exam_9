from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

from webapp.forms import PhotoForm
from webapp.models import Photo
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'photos'
    paginate_by = 10
    paginate_orphans = 5

    def get_queryset(self):
        return Photo.objects.all().order_by('-created_at')


class PhotoView(DetailView):
    template_name = 'detail_photo.html'
    model = Photo


class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create_photo.html'
    form_class = PhotoForm
    model = Photo

    def get_success_url(self):
        return reverse('webapp:detail_photo', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        return redirect('webapp:detail_photo', pk=photo.pk)


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'update_photo.html'
    form_class = PhotoForm
    model = Photo
    permission_required = 'webapp.change_photo'

    def has_permission(self):
        photo = self.get_object()
        return super().has_permission() or photo.author == self.request.user

    def get_success_url(self):
        return reverse('webapp:detail_photo', kwargs={'pk': self.object.pk})


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_photo.html'
    model = Photo
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_photo'

    def has_permission(self):
        photo = self.get_object()
        return super().has_permission() or photo.author == self.request.user
