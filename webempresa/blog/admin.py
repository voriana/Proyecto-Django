from django.contrib import admin
from .models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published') #todo ordenar por un solo campo "," al final para que reconozca la tupla ('author',)
    search_fields = ('title','author__username', 'categories__name') #todo campos de busqueda
    date_hierarchy = 'published' #todo ordernar por campo
    list_filter = ('author__username',) #todo filtrar por campos

    def post_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])

    post_categories.short_description = 'Categorías de posteos'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
