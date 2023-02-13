from django.shortcuts import render
from .models import Project

# Create your views here.

def portfolio(request):
    projects=Project.objects.all() # para recuperar todas las instancias (registros de la tabla de BD) del modelo Project
    return render(request,'portfolio/portfolio.html',{'projects': projects}) #agregro este dic para agregarlo en el html
