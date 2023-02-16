from django.db import models


class Artist(models.Model):
    """
    Исполнитель
    """
    name = models.CharField(verbose_name='Название исполнителя', max_length=150)

    def __str__(self):
        return self.name


class Album(models.Model):
    """
    Альбом
    """

    name = models.CharField(verbose_name='Название альбома', max_length=150, blank=True)
    artist = models.ForeignKey(
        Artist, verbose_name='Исполнитель альбома', related_name="artist_album", on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField('Год выпуска')
    songs = models.ManyToManyField(
        'Song', verbose_name='Песни', through='AlbumSong', related_name='album_song')

    def __str__(self):
        return self.name


class Song(models.Model):
    """
    Песня
    """
    artist = models.ForeignKey(
        Artist, verbose_name='Исполнитель песни', related_name="artist_song", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Песня', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (("artist", "name"), )


class AlbumSong(models.Model):
    """
    Кастомная таблица для соотношения многие ко многим Album и Song
    """
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_song')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='song_album')
    number_in_the_album = models.PositiveSmallIntegerField('Номер в альбоме')

    class Meta:
        unique_together = (("album", "song"), ("song", 'number_in_the_album'), ("album", 'number_in_the_album'))

    def __str__(self):
        return f'{self.album.name}-{self.song.name}-{self.number_in_the_album}'
