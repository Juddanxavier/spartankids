from imagekit.cachefiles import ImageCacheFile
from imagekit.processors import ResizeToFill
from imagekit import ImageSpec
from imagekit.admin import AdminThumbnail
from django.contrib import admin
from .models import Gallery
# Register your models here.


class AdminThumbnailSpec(ImageSpec):
    processors = [ResizeToFill(100, 30)]
    format = 'JPEG'
    options = {'quality': 60}


def cached_admin_thumb(instance):
    # `image` is the name of the image field on the model
    cached = ImageCacheFile(AdminThumbnailSpec(instance.image))
    # only generates the first time, subsequent calls use cache
    cached.generate()
    return cached


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field=cached_admin_thumb)

    class Meta:
        models = Gallery


admin.site.register(Gallery, GalleryAdmin)
