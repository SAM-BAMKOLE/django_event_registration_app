from django.contrib import admin
from .models import Category, Event

# Register your models here.
admin.site.register(Event)
admin.site.register(Category)