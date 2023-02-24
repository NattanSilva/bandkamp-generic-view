from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from albums.models import Album

from .models import Song
from .serializers import SongSerializer


class SongView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_queryset(self):
        album = get_object_or_404(Album, id=self.kwargs["pk"])
        return Song.objects.filter(album=album)
    
    def perform_create(self, serializer):
        album = get_object_or_404(Album, id=self.kwargs["pk"])
        serializer.save(album=album)