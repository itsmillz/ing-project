from django.shortcuts import render, redirect
from .forms import FormPropiedad
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import Propietario, Propiedad

# Create your views here.
def index(request):
    listado_propiedades = Propiedad.objects.all().order_by("-id")
    
    # Buscador
    busqueda = request.GET.get("buscar")
    propiedades = Propiedad.objects.all()
    if busqueda:
        propiedades = Propiedad.objects.filter(
            Q(universidades_cercanas__icontains = busqueda)
        ).distinct().order_by("-id")
    return render(request, 'arriendos.html', {'filtrar_lista':propiedades, 'listado_propiedades':listado_propiedades})

def agregar_propiedad(request):
    propietario_defecto = get_object_or_404(Propietario, pk=1)
    request.propietario = propietario_defecto
    casa_imagen = request.FILES.get('txtImagen')
    if request.method == 'POST':
        form = FormPropiedad(request.POST)
        if form.is_valid():
            nueva_propiedad = form.save(commit=False)
            nueva_propiedad.save()
            return redirect('index')
        else:
            form = FormPropiedad()
    else:
        form = FormPropiedad()
    return render(request, 'agregar_propiedad.html', {'nueva_propiedad':form})

def filtro_universidad(request, value):
    universidades=""
    if value == 1:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Universidad del Bio Bio")
    if value == 2:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Universidad De La Santisima Concepcion")
    if value == 3:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Universidad San Sebastián")
    if value == 4:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Advance Universidad San Sebastián")
    if value == 5:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Universidad Diego Portales")
    if value == 6:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Universidad del Desarrollo")
    if value == 7:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Universidad del Pacífico")
    if value == 8:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Universidad Técnica Federico Santa María")
    if value == 9:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="INACAP - Universidad Tecnológica de Chile")
    if value == 10:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="INACAP - Universidad Andrés Bello")
    if value == 11:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Universidad Andrés Bello Postgrados")
    if value == 12:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Universidad Arcis - Concepción")
    if value == 13:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Universidad Santo Tomás")
    if value == 14:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="DUOC UC")
    if value == 15:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Instituto Profesional DUOC UC")
    if value == 16:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Universidad del Desarrollo")
    if value == 17:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Educacion Ejecutiva - Facultad de Economía y Negocios - UDD (Universidad del Desarrollo)")
    if value == 18:
        universidades = Propiedad.objects.filter(universidades_cercanas__contains="Universidad de Concepcion")
    return render(request, "propiedades_list.html", {'universidades':universidades})

def filtro_precio(request, value2):
    if value2 == 20:
        universidades = Propiedad.objects.filter(precio_arriendo__range=(80000, 150000))
    return render(request, "propiedades_list.html", {'universidades':universidades})

def filtro_dormitorios(request, value3):
    if value3 == 30:
        universidades = Propiedad.objects.filter(cantidad_habitaciones__num=1)
    if value3 == 31:
        universidades = Propiedad.objects.filter(cantidad_habitaciones=2)
    if value3 == 32:
        universidades = Propiedad.objects.filter(cantidad_habitaciones__num=3)
    if value3 == 33:
        universidades = Propiedad.objects.filter(cantidad_habitaciones__num=4)
    if value3 == 34:
        universidades = Propiedad.objects.filter(cantidad_habitaciones__num=5)
    return render(request, "propiedades_list.html", {'universidades':universidades})



