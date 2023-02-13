from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


# Register your models here.
admin.site.register(Project,ProjectAdmin) #se le pasa la configuraicion extendida para que tomo los campos readonly

