from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from imagekit import ImageSpec, register
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(upload_to='images')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(320, 320)],
                                     format='JPEG',
                                     options={'quality': 60})
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']
