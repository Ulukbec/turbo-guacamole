from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .service import MangaFilter
from .pagination import MangaPagination
from rest_framework.filters import SearchFilter


# Create your views here.


class MangaView(ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = MangaFilter
    pagination_class = MangaPagination
    search_fields = ['title', 'type']
    permission_classes = [IsAdminUser]


class GenreView(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



