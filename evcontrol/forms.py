from django import forms
from django.db import models
from .models import Event, Guest
from django.contrib.auth.models import User


from urllib.request import Request, urlopen

class EventForm(forms.ModelForm):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    date = models.DateField()

    class Meta:
        model = Event
        fields = ['title','slug' , 'description', 'date',]

    def save(self, commit=True, *args, **kwargs):
        event = Event(
            title = self.cleaned_data['title'],
            slug = self.cleaned_data['slug'],
            description = self.cleaned_data['description'],
            date = self.cleaned_data['date'],
            user = User.objects.get(id = kwargs['id'])
        )
        if commit:
            event.save()
class GuestForm(forms.ModelForm):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete = models.CASCADE)

    class Meta:
        model = Guest
        fields = ['name', 'email', 'event']

    def save(self, commit = True, *args, **kwargs):
        guest = Guest(
            name = self.cleaned_data['name'],
            email = self.cleaned_data['email'],
            event = self.cleaned_data['event']
        )
        if commit:
            guest.save()