from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect
from . import forms
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from .forms import VehiculoForm
# Create your views here.
def index(request):
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesion como: {username}")
                return HttpResponseRedirect("/filtrar")
            else:
                messages.error(request,"Invalido username o password")
                return HttpResponseRedirect("/")
    else:
        messages.error(request,"Invalido username o password")
        form = AuthenticationForm()
    return render(request=request, template_name="login.html",context={"login_form":form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def vehiculo(request):
    return render(request, 'vehiculo.html', context={})


def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')  # Redirige a la lista de vehículos
    else:
        form = VehiculoForm()
    return render(request, 'agregar_vehiculo.html', {'form': form})