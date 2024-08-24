""" PerfectParking URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("boxes", views.boxes, name='boxes')
    #path('boxes/<int:box_id>', views.box, name='box'),
]