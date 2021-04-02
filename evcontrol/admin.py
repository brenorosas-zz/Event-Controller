from django.contrib import admin
from .models import Organizer
from .models import Event
# Register your models here.

admin.site.register(Organizer)
admin.site.register(Event)