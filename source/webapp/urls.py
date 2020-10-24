from django.contrib import admin
from django.urls import path, include

from webapp.views import IndexView, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>', PhotoView.as_view(), name='detail_photo'),

    path('photo/create/', PhotoCreateView.as_view(), name='create_photo'),

    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='update_photo'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete_photo'),

]
