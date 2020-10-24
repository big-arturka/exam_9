from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models import Photo, Favorites


class AddView(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(ensure_csrf_cookie)
    def post(self, request, pk=None):
        photo = get_object_or_404(Photo, pk=pk)
        fav, create = Favorites.objects.get_or_create(photo=photo, author=request.user)
        if create:
            return Response({'pk': pk})
        else:
            return Response(status=403)


class RemoveView(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(ensure_csrf_cookie)
    def delete(self, request, pk=None):
        photo = get_object_or_404(Photo, pk=pk)
        favorites = Favorites.objects.filter(photo=photo)
        favorites.delete()
        return Response({'pk': pk})