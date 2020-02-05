

from django.urls import path
from django.views.generic import ListView, DetailView
from news.models import News
from . import views
urlpatterns = [
    path('', ListView.as_view(queryset=News.objects.all().order_by("-timestamp")[:4],
                              template_name="pages/home.html"), name='home'),
    path('about', views.about, name='about')

]
