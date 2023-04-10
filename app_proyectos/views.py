from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_proyectos.models import Proyecto
from app_proyectos.forms import CreacionProyectoForm, BuscarProyectoForm

# Create your views here.

def inicio(request):
    return render(request, 'app_proyectos/inicio.html')

def crear_proyecto(request):
    
    if request.method == 'POST':
        formulario = CreacionProyectoForm(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
            proyecto = Proyecto(titulo=datos_correctos['titulo'], tipologia=datos_correctos['tipologia'], superficie=datos_correctos['superficie'], plantas=datos_correctos['plantas'], dormitorios=datos_correctos['dormitorios'], baños=datos_correctos['baños'])
            proyecto.save()
            return redirect('app_proyectos:inicio')
        
        else:
            print(formulario.errors)
            formulario = CreacionProyectoForm()
            return render(request, 'app_proyectos/crear_proyectos.html', {'formulario':formulario}) 
        
    else:
        formulario = CreacionProyectoForm()
        return render(request, 'app_proyectos/crear_proyectos.html', {'formulario':formulario}) 

   
def buscar_proyecto(request):
    titulo_a_buscar = request.GET.get('titulo', None)
    tipologia_a_buscar = request.GET.get('tipologia', None)
    
    if titulo_a_buscar:
        proyectos = Proyecto.objects.filter(titulo__icontains=titulo_a_buscar)
    else:
        proyectos = Proyecto.objects.all()
    
    if tipologia_a_buscar:
        proyectos = proyectos.filter(tipologia__icontains=tipologia_a_buscar)
        
    formulario_busqueda = BuscarProyectoForm()
    return render(request, 'app_proyectos/buscar_proyecto.html', {'proyectos': proyectos, 'formulario': formulario_busqueda})   


