from django.db import models
from manga.compressed_image_field import CompressedImageField


class Genre(models.Model):
    name = models.CharField("Название", max_length=200)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Manga(models.Model):
    title = models.CharField("Название", max_length=200)
    year = models.PositiveSmallIntegerField("Год")
    genre = models.ManyToManyField(Genre, related_name='genre', verbose_name="Жанр")
    synopsis = models.TextField("Описание")
    type = models.CharField("Тип", max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    create_update = models.DateTimeField(auto_now=True)
    image = CompressedImageField("Изображение", null=True, default=None, quality=85)

    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манги'

    def __str__(self):
        return self.title



