from django.contrib import admin
from .models import Event
from .models import Guest
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "user")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Guest)