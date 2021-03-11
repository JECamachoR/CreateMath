from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .models import GRUPO_POR_GRADO, Actividad, Estudiante
from .forms import *

# Create your views here.
def home(request):
    return render(request, "home/falta.html")

def info(request):
    return render(request, "home/falta.html")

def patrocinadores(request):
    return render(request, "home/falta.html")

def preparacion(request):
    return render(request, "home/falta.html")

def lookup(request):
    template_name="home/lookup.html"
    if not request.user.is_staff:
        return redirect("home:home")
    if request.method == "POST":
        try:
            ctx = {
                "estudiante": Estudiante.objects.get(matricula=request.POST["matricula"])
            }
        except Estudiante.DoesNotExist:
            ctx = {
                "estudiante": False,
                "no_registrado": True
            }
        return render(request, template_name, ctx)
    else:
        return render(request, template_name)

    
def agenda(request):
    template_name="home/agenda.html" # Remplazar cuando sepamos
    if request.user.is_authenticated:
        actividades = list()
        for group in request.user.groups.all():
            actividades.append(
                list(group.actividad_set.all())
            )
        
        return render(request, template_name, context={
            "actividades": actividades
        })
    else:
        group = Group.objects.get(name="PUBLICO")
        actividades = [group.actividad_set.all()]
        return render(request, "home/home.html", context={
            "actividades": actividades
        })

def log_user_out(request):
    logout(request)
    return redirect("home:home")

def sign_up(request):

    if request.user.is_authenticated:
        return redirect("home:home")
    
    form = UserCreationForm_custom(request.POST or None)
    studentForm = StudentForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid() and studentForm.is_valid():
            user = form.save()
            student = studentForm.save(commit=False)
            student.user = user
            student.save()
            grupo, b = Group.objects.get_or_create(name=GRUPO_POR_GRADO[student.grado])
            grupo.user_set.add(user)
            login(request,user)
            return redirect('home:home')
    
    context = {"form": form, "studentForm": studentForm}
    return render(request,'registration/sign_up.html',context)