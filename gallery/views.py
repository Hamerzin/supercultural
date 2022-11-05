from django.shortcuts import render
from blog.models import Galeria

# Create your views here.
def gallery(request):
    
    galeria2 = Galeria.objects.order_by('id')
    return render(request, "gallery.html", {'galeria': galeria2})


