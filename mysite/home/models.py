from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

GRADOS = [
    "1° de Primaria",
    "2° de Primaria",
    "3° de Primaria",
    "4° de Primaria",
    "5° de Primaria",
    "6° de Primaria",
    "1° de Secundaria",
    "2° de Secundaria",
    "3° de Secundaria"
]

GRUPOS = [
    "ESTUDIANTES 1",
    "ESTUDIANTES 2",
    "ESTUDIANTES 3",
    "ESTUDIANTES 4"
]

GRUPO_POR_GRADO = [
    "ESTUDIANTES 1",
    "ESTUDIANTES 1",
    "ESTUDIANTES 1",
    "ESTUDIANTES 2",
    "ESTUDIANTES 2",
    "ESTUDIANTES 3",
    "ESTUDIANTES 3",
    "ESTUDIANTES 4",
    "ESTUDIANTES 4"
]

# Datos del alumno:
# -Nombre (s)   +
# -Apellidos    +
# -Escuela      +
# -Grado (que cursa actualmente el alumno)  +
# -Estado       +
# -Municipio    +
# -Fecha de nacimiento  +
# Datos de tutor: (que por favor sea el mismo que realiza el pago)
# -Nombre completo  +
# -Parentesco
# -Contacto correo
# -Contacto wa

class Estudiante(AbstractUser):
    """
    Modelo que representa al estudiante en la base de datos
    """
    escuela = models.CharField(max_length=128, blank=True, null=True)
    grado = models.IntegerField(choices=[
        (i, GRADOS[i])
        for i in range(9)
    ], blank=True, null=True)
    estatus_de_inscripcion = models.IntegerField(default=0, null=True)
    estado = models.CharField(max_length=128, blank=True, null=True)
    municipio = models.CharField(max_length=128, blank=True, null=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)


    def __str__(self):
        if self.is_staff:
            return f"{self.username} - STAFF"
        return f"{self.first_name} de {self.grado}"

class Tutor(models.Model):
    hijo = models.OneToOneField(Estudiante, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=128)
    parentesco = models.CharField(max_length=128)
    correo = models.EmailField()
    celular = PhoneNumberField()

class Actividad(models.Model):
    nombre = models.CharField(max_length=128)
    tiempo = models.DateTimeField()
    dura = models.DurationField()
    link = models.URLField(default="www.google.com")
    invitados = models.ManyToManyField(Group)
    
    class Meta:
        verbose_name_plural = "Actividades"
        ordering = ['tiempo', 'nombre']

    def __str__(self):
        return self.nombre