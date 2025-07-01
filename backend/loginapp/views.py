from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Usamos POST, no JSON aquí
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, 'Inicio de sesión exitoso')
            return redirect('dashboard')  # Cambia por la vista que desees mostrar
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
            return redirect('login')  # Redirige para volver a intentar
    else:
        return render(request, 'loginapp/login.html')
    
@login_required
def dashboard_view(request):
    return render(request, 'loginapp/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al login después de cerrar sesión