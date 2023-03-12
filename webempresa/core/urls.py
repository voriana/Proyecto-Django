from django.urls import path
from . import views  # el "." significa en el directorio actual, importar views

urlpatterns = [
    path('', views.Inicio, name='Ini'),
    path('about/', views.Historia, name='Hist'),
    path('store/', views.Visitanos, name='Visits'),
    path('contact/', views.Contacto, name='Contac'),
    # path('blog/', views.Blog, name='Blog'),
    # path('sample/', views.Blog, name='Sample'),
]
