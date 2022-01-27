from itertools import product
from django.shortcuts import get_object_or_404, render

from django.shortcuts import render

from .models import Category
from .models import Scooter

def list_of_scooters(request, category_slug = None):
    scooters = Scooter.objects.all()
    return render(request, 'scooters/scooter_list.html', {'scooters': scooters,})

def scooter_detail(request, scooter_id):
    scooters = Scooter.objects.filter(pk=scooter_id)
    return render(request, 'scooters/scooter_detail.html', {'scooters': scooters,})

def homepage(request):
    return render(request, 'scooters/homepage.html', {})