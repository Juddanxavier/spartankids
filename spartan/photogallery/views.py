from django.shortcuts import render, HttpResponse
from .models import Gallery
from django.core.paginator import Paginator

# Create your views here.


def gallery_view(request):
    obj = Gallery.objects.all()
    paginator = Paginator(obj, 9)
    page = request.GET.get('page')
    photos = paginator.get_page(page)
    return render(request, 'pages/gallery.html', {'photos': photos})
