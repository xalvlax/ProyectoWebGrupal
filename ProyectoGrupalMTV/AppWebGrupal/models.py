from django.db import models

# Create your models here.
class Empleados(models.Model):
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    ocupacion = models.CharField(max_length=30)
    class Meta():
        ordering = ('apellido', 'nombre') # Ordena.
        unique_together = ('apellido', 'nombre', 'edad') # No permite que se repitan.
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self) -> str:
       return f'{self.apellido} {self.nombre}'
    # Muestra en la pagina del Admin "apellido, nombre"


class Tareas(models.Model):
    responsable = models.ForeignKey(Empleados, on_delete=models.CASCADE, default=True, blank=True)
    nombre = models.CharField(max_length=30) 
    dia_de_creacion = models.DateField(auto_now_add=True)

    class Meta():
        ordering = ('dia_de_creacion', '-nombre', 'responsable') # Ordena.
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self) -> str:
       return f'{self.nombre} - {self.dia_de_creacion}'
    # Muestra en la pagina del Admin "apellido, nombre"


class Herramientas(models.Model):
    tipo_de_tarea = models.ForeignKey(Tareas, on_delete=models.CASCADE, default=True, blank=True)
    nombre = models.CharField(max_length=30)
    disponible =  models.BooleanField(default=False)

    class Meta():
        ordering = ('nombre', 'disponible') # Ordena.
        verbose_name = 'Herramienta'
        verbose_name_plural = 'Herramientas'

    def __str__(self) -> str:
       return f'{self.nombre}'
    # Muestra en la pagina del Admin "apellido, nombre"
