from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import logout, login
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def login_view(request, *args, **kwargs):
    form = AuthenticationForm(data = request.POST)
    if form.is_valid():
        login(request, form.get_user())
        return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form' : form})

def register_view(request, *args, **kwargs):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form' : form})

def logout_view(request, *args, **kwargs):
    logout(request)
    return render(request, "home.html", {})

def settings_view(request, *args, **kwargs):
    form = PasswordChangeForm(data = request.POST, user = request.user)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        form = PasswordChangeForm(data = request.POST, user = request.user)
    return render(request, "settings.html", {'form' : form})

# Create your views here.