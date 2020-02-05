from django.db import models
from django.db.models.signals import pre_save
from spartan.utils import unique_slug_generator


class News(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title


def slug_save(sender, instance, *agrs, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(
            instance, instance.title, instance.slug)


pre_save.connect(slug_save, sender=News)
