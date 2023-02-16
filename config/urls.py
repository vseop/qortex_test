from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from config import settings
from music.api.viewsets import ArtistViewSet, AlbumViewSet, SongViewSet, AlbumSongViewSet, AllInformationArtist

schema_view = get_schema_view(
    openapi.Info(
        title="Тестовое задание Кортекс",
        default_version='v1',
        description="Тестовое задание Кортекс",
        contact=openapi.Contact(email='ivdjango@mail.ru'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register('artist', ArtistViewSet, basename='artist')
router.register('album', AlbumViewSet, basename='album')
router.register('song', SongViewSet, basename='song')
router.register('albumsong', AlbumSongViewSet, basename='albumsong')
router.register('artistsinfo', AllInformationArtist, basename='artistsinfo')

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns = [path('__debug__/', include('debug_toolbar.urls'))] + urlpatterns
