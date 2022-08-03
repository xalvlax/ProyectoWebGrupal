from django.contrib import admin 
from .models import Empleados, Tareas, Herramientas

# Register your models here.

class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'nombre', 'edad', 'ocupacion']
    search_fields = ['apellido', 'nombre']

# Register your models here.
admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(Tareas)
admin.site.register(Herramientas)
