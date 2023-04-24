from django.shortcuts import render, get_object_or_404 
from core.models import Articulos
from core.forms import ArticulosForm
# Create your views here.

def inicio(request):
    return render(request, 'core/index.html')

def agregar(request):

    if request.method == "POST":
        articulo_form = ArticulosForm(request.POST)
        if articulo_form.is_valid():
            data = articulo_form.cleaned_data
            articulo = Articulos(titulo=data["titulo"],subtitulo=data["subtitulo"], ubicacion=data["ubicacion"], cuerpo =data["cuerpo"], autor=data["autor"],fecha=data["fecha"])
            articulo.save()
            return render(request, 'core/mostrar_articulo.html')
        
    articulo_form = ArticulosForm()
    return render(request, 'core/agregar_articulo.html', {"form": articulo_form})

def mostrar(request):

    articulosx = Articulos.objects.all()

    return render(request, 'core/mostrar_articulo.html', {"articulos" : articulosx } )

def editar(request, id_articulo):
        
    articulo = Articulos.objects.get(id= id_articulo)

    if request.method == "POST":
        articulo_form = ArticulosForm(request.POST)
        if articulo_form.is_valid(): 
                data = articulo_form.cleaned_data
                articulo.titulo = data["titulo"]
                articulo.subtitulo= data["subtitulo"]
                articulo.ubicacion= data["ubicacion"]
                articulo.cuerpo= data["cuerpo"]
                articulo.imagen = data ['imagen']
                articulo.fecha= data["fecha"]
                articulo.save()
                return render(request, 'core/mostrar_articulo.html')
    else: 
        articulo_form = ArticulosForm(initial= {'titulo' : articulo.titulo, 'subtitulo' : articulo.subtitulo, 'ubicacion': articulo.ubicacion, 'cuerpo' : articulo.cuerpo,'imagen' : articulo.imagen, 'autor' : articulo.autor, 'fecha' : articulo.fecha})
        return render(request, 'core/editar_articulo.html', {'form' : articulo_form },)

def eliminar(request, id_articulo):

    articulo = Articulos.objects.get(id=id_articulo)
    name = articulo.titulo
    articulo.delete()


    return render(request, 'core/eliminar_articulo.html', {"articulo_eliminado" : name})

def mostrar_miinfo(request):
    return render(request, 'core/miinfo.html')

def leermas(request, id_articulo):
    articulo = get_object_or_404(Articulos, id=id_articulo)
    return render(request, 'core/leermas.html', {'articulo': articulo})



