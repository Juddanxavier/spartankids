from django.contrib import admin

# Register your models here.
from .models import News

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    News = ('title', 'timestamp')
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        models = News


admin.site.register(News, NewsAdmin)
