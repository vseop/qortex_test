from rest_framework import serializers

from music.models import Artist, Album, Song, AlbumSong
from django.core.exceptions import ObjectDoesNotExist


class ArtistSerializer(serializers.ModelSerializer):
    """Исполнители"""

    class Meta:
        model = Artist
        fields = "__all__"


class SongSerializers(serializers.ModelSerializer):
    """Песни"""

    class Meta:
        model = Song
        fields = "__all__"


class AlbumSongSerializer(serializers.ModelSerializer):
    """Связь между альбомом и исполнителями"""

    class Meta:
        model = AlbumSong
        fields = "__all__"


class AlbumlSerializers(serializers.ModelSerializer):
    """Альбомы"""

    class Meta:
        model = Album
        fields = "__all__"



class AlbumSongReadSerializer(serializers.ModelSerializer):
    """Связь между альбомом и исполнителями для чтения с номерами песен в альбоме"""

    name = serializers.CharField(source='song.name')

    class Meta:
        model = AlbumSong
        fields = ('name', 'number_in_the_album')


class AlbumlInfoSerializer(serializers.ModelSerializer):
    """Вывод альбома со списком песен"""

    songs = AlbumSongReadSerializer(many=True, source='album_song')

    class Meta:
        model = Album
        fields = ('name', 'year', 'songs')


class AllInformationSerializer(serializers.ModelSerializer):
    """Вывод исполнителей со всеми альбомами и песнями"""
    albums = AlbumlInfoSerializer(source='artist_album', many=True)

    class Meta:
        model = Artist
        fields = ('id','name', 'albums')
