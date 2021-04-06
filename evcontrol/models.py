from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

class Guest(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
# Create your models here.