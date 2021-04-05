from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from .models import Event
from .forms import EventForm, GuestForm
from .tasks import send_email
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

def events_view(request, *args, **kwargs):
    events = User.objects.get(id = request.user.id).event_set.all();
    search = request.GET.get('search')
    if search:
        events = events.filter(title__icontains=search)
    return render(request, "events.html", {'events' : events})

def addEvent_view(request, *args, **kwargs):
    form = EventForm(data = request.POST)
    if form.is_valid():
        form.save(id = request.user.id)
        return redirect('events')
    else:
        form = EventForm(data = request.POST)
    return render(request, "addevent.html", {'form' : form})

def addGuest_view(request, *args, **kwargs):
    form = GuestForm(data = request.POST)
    if form.is_valid():
        form.save()
        send_email(form.get_email())
        return redirect('events')
    else:
        form = GuestForm(data = request.POST)
    return render(request, "addguest.html", {'form' : form})
    
class EventDetailView(DetailView):
    model = Event
# Create your views here.