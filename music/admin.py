from django.contrib import admin

from music.models import Artist, Album, Song, AlbumSong

# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(AlbumSong)
