from django.shortcuts import render
from django.shortcuts import get_object_or_404  #Esto hace para cuando no existe una consulta se manda el error 404
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
from .models import Post, Categoria


def home(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    posts = Post.objects.filter(estado=True)
    if queryset:  #Esta es la funcion de barra de busqueda que buscara cosas en una vista html
         posts = Post.objects.filter(
             Q(titulo__icontains = queryset) | #__icontains de manera paresida a iexact sirve para que se busque algo aunque lo que se puso no sea exacto
             Q(descripcion__icontains = queryset)          #en esta caso lo que hace es preguntar como una consulta de like %queryset% osea si en donde se busca contiene en algun logar la frase
         ).distinct()

    paginator = Paginator(posts,2) #Se llama a la clase Paginator y se le pasan 2 parametor, uno son los objetos que salieron de la busqueda y el otro es el  numero de ellos que aparesera
    page  = request.GET.get('page') #Esto se hace para saber la pagina actual y asi se pueda pasar a la siguiente con los sig elementos
    posts = paginator.get_page(page) #Con esto en la pagina que estamos le mandamos lo que traia el query o las busquedas

    return render(request, 'index.html', {'posts':posts})


def detallePost(request, slug): #slug para que no sea visible un id al viajar por la url, se ponde donde ya esta creado un registro para que se acceda a su atributo slug y no haya problema
     post = get_object_or_404(Post, slug = slug) #aqui se valida si existe la consulta ya lleva internamente la creacion de una instancia usando como referencia el slug
     return render(request, 'post.html', {'detalle_post':post})

def generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,

        categoria = Categoria.objects.get(nombre__iexact = 'General') #filtracion por dos caracteristicas UNA DE ellas es un modelo con una relacion con la tabla en la que se esta preguntando
    )                                                                 #nombre__iexact sirve para que no importe si el usuario manda el formulario con mayusculas o minusculkas siempre que sea la palabra
    if queryset:  #OOJO primero pide q el estado este en true osea publicado
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'General'),
        ).distinct()
    return render(request,'generales.html', {'posts':posts})


def programacion(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Programacion')
    )
    return render(request,'programacion.html', {'posts':posts})

def tutoriales(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales')
    )
    return render(request,'tutoriales.html', {'posts':posts})


def tecnologia(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre = 'Tecnologia')
    )
    return render(request,'tecnologia.html', {'posts':posts})


def videojuegos(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos')
    )
    return  render(request,'videojuegos.html', {'posts':posts})
