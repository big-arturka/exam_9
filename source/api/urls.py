from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from api.views import AddView, RemoveView

app_name = 'api'

urlpatterns = [
    path('<int:pk>/add/', AddView.as_view(), name='add'),
    path('<int:pk>/remove/', RemoveView.as_view(), name='remove'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)