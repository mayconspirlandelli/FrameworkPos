from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),   
 path('pagina0', views.pagina0, name='pagina0')
]