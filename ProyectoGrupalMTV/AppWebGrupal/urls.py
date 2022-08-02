from AppWebGrupal.views import inicio
from django.urls import path

urlpatterns = [
    path('inicio/', inicio, name= 'inicio'),
]
