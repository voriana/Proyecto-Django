from django.urls import path
from . import views  # el "." significa en el directorio actual, importar views

urlpatterns = [
    path('', views.post, name='post'),
    path('category/<int:category_id>/', views.category, name='category'),

]
