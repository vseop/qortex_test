from rest_framework import viewsets

from music.api.serializers import ArtistSerializer, AlbumlSerializers, SongSerializers, AlbumSongSerializer, \
    AllInformationSerializer
from music.models import Artist, Album, Song, AlbumSong


class AllInformationArtist(viewsets.ReadOnlyModelViewSet):
    queryset = Artist.objects.prefetch_related('artist_album__album_song__song').all()
    serializer_class = AllInformationSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    """Исполнители CRUD """
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()


class AlbumViewSet(viewsets.ModelViewSet):
    """Альбомы CRUD """
    queryset = Album.objects.prefetch_related('songs').all()
    serializer_class = AlbumlSerializers


class SongViewSet(viewsets.ModelViewSet):
    """Песни CRUD """
    serializer_class = SongSerializers
    queryset = Song.objects.all()


class AlbumSongViewSet(viewsets.ModelViewSet):
    """Установка связей между альбомами и песнями """
    serializer_class = AlbumSongSerializer
    queryset = AlbumSong.objects.all()
