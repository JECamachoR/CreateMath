from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

from .forms import *
# Create your views here.
class Home(TemplateView):
    template_name="home/home.html"

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
            login(request,user)
            return redirect('home:home')
    
    context = {"form": form, "studentForm": studentForm}
    return render(request,'registration/sign_up.html',context)

# def student_details(request):
#     context = dict()
#     form = StudentRegistrationForm(request.POST or None)
    
#     if request.method == "POST":
#         if form.is_valid():
#             user = request.user
#             form.save()
#             return redirect('home:home')
#     context['form']=form
#     return render(request,'registration/sign_up.html',context)
