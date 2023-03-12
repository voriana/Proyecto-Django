from django.urls import path
from . import views  # el "." significa en el directorio actual, importar views

urlpatterns = [
    path('', views.services, name="service"),
]
