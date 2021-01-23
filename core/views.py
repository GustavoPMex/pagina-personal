from django.shortcuts import render
from .models import description

# Create your views here.

def home(request):
    return render(request, "core/home.html")


def about(request):
    descripcion = description.objects.all()
    return render(request, "core/about.html", {'descripcion':descripcion})

