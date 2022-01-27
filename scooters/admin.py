from django.contrib import admin

from .models import Category, Scooter

class ScooterAdmin(admin.ModelAdmin):
    list_display = ('category', 'name')

admin.site.register(Scooter, ScooterAdmin)
admin.site.register(Category)
