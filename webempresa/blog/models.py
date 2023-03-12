from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

#creo modelo categorias
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-created']

    def __str__(self):
        return self.name

#creo modelo Post
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido", default="a completar")
    published = models.DateTimeField(verbose_name= "Fecha de publicacion", default= now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    #TODO ESTO ES UNA RELACION 1 AL MODELO DE USUARIOS DEL LA CONSOLA ADMIN, SI SE ELIMINA UN AUTOR SE ELIMINAN SUS POSTEOS POR CASCADE
    author = models.ForeignKey(User,verbose_name="Autor",on_delete=models.CASCADE)
    #TODO RELACION MUCHOS A MUCHOS
    categories = models.ManyToManyField(Category,verbose_name="Categorías",related_name= 'get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Posteo"
        verbose_name_plural = "Posteos"
        ordering = ['-created']

    def __str__(self):
        return self.title
