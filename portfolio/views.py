from django.shortcuts import render
from .models import project
# Create your views here.

def portfolio(request):
    projects = project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects':projects})