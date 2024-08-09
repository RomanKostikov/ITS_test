from django.urls import path
from video.apps import VideoConfig

from video.views import index, VideoListView, download_file, main_page

app_name = VideoConfig.name


urlpatterns = [
    path('', main_page, name="main_page"),
    path('gettext/', index, name="index"),
    path('download/<int:pk>/', download_file, name='download_file'),
    path('videos/', VideoListView.as_view(), name="videos"),
]