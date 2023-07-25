from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from .models import Song
from django.shortcuts import get_object_or_404
from albums.models import Album
from rest_framework.response import Response
from rest_framework import status


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    serializer_class = SongSerializer

    def get_queryset(self):
        """
        Obtenção de músicas
        """
        album_id = self.kwargs["pk"]
        return Song.objects.filter(album_id=album_id)

    def post(self, request, pk):
        """
        Criação de música
        """
        album = get_object_or_404(Album, pk=pk)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(album=album)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
