from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from utils.utils import create_video_opencv, convert_to_h264
from video.models import Video


def main_page(request):
    return render(request, 'video/main_page.html')


def index(request):
    message = str(request.GET.get('text', ''))
    result = create_video_opencv(message)
    # convert_to_h264(f'media/{result["path"]}')
    new_video = Video(title=result['title'], message=message, video=result['path'])
    new_video.save()
    context = {'object': new_video}
    return render(request, 'video/index.html', context)


def download_file(request, pk):
    video = Video.objects.get(pk=pk)
    response = HttpResponse(video.video, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{video.video.name}"'
    return response


class VideoListView(ListView):
    model = Video

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        print(queryset)
        return queryset
