from django.urls import path

from . import views

urlpatterns = [
    path('scooters/', views.list_of_scooters, name = 'scooters_list'),
    path('scooters/<scooter_id>', views.scooter_detail, name = 'details'),
    path('', views.homepage, name = 'homepage'),
]