from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='images', verbose_name='Фото')
    signature = models.CharField(max_length=200, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(get_user_model(), max_length=50, verbose_name='Автор',
                               related_name='image_author', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.signature}-{self.author}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Favorites(models.Model):
    photo = models.ForeignKey(Photo, related_name='favorite_photo', verbose_name='Фото', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), related_name='favorite_author',
                               verbose_name='Автор', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.photo}-{self.author}'

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
