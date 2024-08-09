from django.contrib import admin
from video.models import Video


@admin.register(Video)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'video', 'create_time')
    search_fields = ('message', )
