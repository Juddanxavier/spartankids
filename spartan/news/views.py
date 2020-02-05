from django.views.generic import ListView
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import News


def News_list(request):
    obj = News.objects.all()
    paginator = Paginator(obj, 5)
    page = request.GET.get('page')
    news = paginator.get_page(page)
    return render(request, 'pages/news.html', {'news': news})

def detail_view(request, slug):
    context = {}
    context["data"] = News.objects.get(slug = slug) 
          
    return render(request, "pages/newsdetail.html", context)
    