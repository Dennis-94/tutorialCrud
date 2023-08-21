from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages
# Create your views here.
def home(request):
    cursosListados = Curso.objects.all()
    messages.success(request,'!Cursos listados¡')
    return render(request,"gestionCurso.html",{"cursos":cursosListados})
def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos =request.POST['numCreditos']
    messages.success(request,'!Cursos Registrado¡')
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos = creditos)
    return  redirect('/')
def edicionCurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request,"edicionCurso.html",{"curso":curso})
def editarCurso(request):
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        creditos =request.POST['numCreditos']
        curso = Curso.objects.get(codigo=codigo)
        curso.nombre = nombre
        curso.creditos=creditos
        curso.save()
        messages.success(request,'!Cursos actualizado¡')
        return redirect('/')


def eliminarCurso(request, codigo):
    curso= Curso.objects.get(codigo= codigo)
    curso.delete()
    messages.success(request,'!Cursos eliminado¡')
    return redirect('/')
