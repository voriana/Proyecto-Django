from django.db import models

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=200,verbose_name='Titulo')
    description= models.TextField(verbose_name='Descripcion')
    image= models.ImageField(verbose_name='Imagen', upload_to='projects')
    link= models.URLField(null=True,blank=True,verbose_name='Enlace Web')
    created= models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion' ) # se ejecuta solo cuando se crea
    updated= models.DateField(auto_now=True,verbose_name='Fecha de actualizacion') # Se ejecuta cada vez que se actualiza/modifica la tabla
    

    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
        ordering= ['-created']

    def __str__(self) -> str:
        return self.title