from django.shortcuts import render


# Create your views here.
def Inicio(request):
    return render(request, template_name='core/home.html')


def Historia(request):
    return render(request, template_name='core/about.html')


def Visitanos(request):
    return render(request, template_name='core/store.html')


def Contacto(request):
    return render(request, template_name='core/contact.html')


