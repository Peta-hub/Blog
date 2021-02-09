from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CategoriaResource(resources.ModelResource): #ModelResource viene de django import-export
    class Meta:
        model = Categoria
                                                 #con estas clases se pueden importar y exportar registros de la BD a la cpu
class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre'] #esto es una barra de busqueda en el admin y buscara en los campos q se pongan entre corchetes
    list_display = ('nombre','estado','fecha_creacion') #esto aparecera esos campos visibles en el admin
    resource_class = CategoriaResource

class AutorResource(resources.ModelResource):
    class Meta:  #Hace referencia al modelo al q se le aplica ese resource (Autor)
        model = Autor

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres','apellidos','correo']
    list_display = ('nombres','apellidos','estado','fecha_creacion')
    resource_class = AutorResource


admin.site.register(Categoria,CategoriaAdmin) # el primero parametro es para dar de alta el modelo en el admin
admin.site.register(Autor,AutorAdmin)                   # el segundo es para cmo se visualiza
admin.site.register(Post)



