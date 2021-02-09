from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la categoria', max_length= 100, null= False, blank= False)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada', default= True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now= False, auto_now_add= True) #cambia cuando se añade

    class Meta:
        verbose_name = 'Categoria'   #es como se va a identificar en el sitio de admin de django
        verbose_name_plural = 'Categorias'

    def __str__(self):   # con esto se renderiza cada instancia del modelo
        return self.nombre  #y se regresa el nombre de la categoria

class Autor(models.Model):
    id= models.AutoField(primary_key = True)
    nombres = models.CharField('Nombres de Autor', max_length= 255, null= False, blank= False)
    apellidos = models.CharField('Apellidos de autor', max_length= 255, null= False, blank = False)
    facebook = models.URLField('Facebook', null= True, blank= True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    email = models.EmailField('Correo Electronico', blank= False, null= False)
    estado = models.BooleanField('Autor Activo/No Activo', default= True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now= False, auto_now_add= True)

    #el primer parametro de es para cmo se vera en el sitio admin

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):     #Aqui se pone cmo se va a renderizar el modelo
        return "{0},{1}".format(self.apellidos, self.nombres)

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length= 90, blank= False, null= False)
    slug = models.CharField('Slug', max_length= 100, blank= False, null= False) #Se agrega como un campo en la bd y sirve para que al mandar a llamar un objeto en una url con su id, ESTE no se vea
    descripcion = models.CharField('Descripcion', max_length= 110, blank= False, null=False)
    contenido = RichTextField('Contenido') #RichTextField hace q en el admin el cuadro de contenido tenga muchas opciones de word
    imagen = models.URLField(max_length= 255, blank= False, null= False)# el URLField es para renderizar imagenes desde internet
    autor = models.ForeignKey(Autor, on_delete=  models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default= True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now= False, auto_now_add= True)


    class Meta:
        verbose_name = 'POST'
        verbose_name_plural = 'POSTS'

    def __str__(self):
        return self.titulo


