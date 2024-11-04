from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Si el usuario es un superusuario, redirige al panel de administración
            if user.is_superuser:
                return redirect('admin_page')  # Redirige al panel de administración

            # Redirecciona según el grupo del usuario
            if user.groups.filter(name='AuxAdmin').exists():
                return redirect('auxadmin_page')
            elif user.groups.filter(name='Dentista').exists():
                return redirect('dentista_page')
            elif user.groups.filter(name='Paciente').exists():
                return redirect('paciente_page')
            else:
                messages.error(request, 'No tienes un rol asignado')
                return redirect('login')
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'accounts/login.html')

def admin_page(request):
    return render(request, 'accounts/admin.html')

def auxadmin_page(request):
    return render(request, 'accounts/auxadmin.html')

def dentista_page(request):
    return render(request, 'accounts/dentista.html')

def paciente_page(request):
    return render(request, 'accounts/paciente.html')