from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from irabbit.usuarios.forms import UserModelForm



# Create your views here.

def db_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'pages-login.html')

def db_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    form = UserModelForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')


    return render(request, "pages-register.html" , {'form': form})
