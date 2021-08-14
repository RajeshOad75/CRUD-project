
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('', views.index, name="index"),
    path('update/', views.update, name="update"),
    path('delete/', views.delete, name="delete"),
    path('show/', views.show, name="show"),

]
