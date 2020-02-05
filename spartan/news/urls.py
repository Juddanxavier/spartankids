from django.urls import path
from . import views
urlpatterns = [
    path('', views.News_list, name='news'),
    path('<slug>', views.detail_view),
]
