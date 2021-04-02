from django.db import models
from django.contrib.auth.models import User

class Organizer(User):
    def __str__(self):
        return self.user

class Guest(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    date = models.DateField()
    organizer = models.ForeignKey(Organizer, on_delete = models.CASCADE)
    guestList = []
    
    def __str__(self):
        return self.title
# Create your models here.