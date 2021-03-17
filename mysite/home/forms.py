from django.contrib.auth.forms import UserCreationForm
from django import forms 
from .models import *
from crispy_forms.helper import FormHelper
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
import datetime

class StudentForm(UserCreationForm):
    escuela = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'El nombre de tu escuela'}))
    first_name = forms.CharField(label = "Nombre(s)", widget=forms.TextInput(attrs={'placeholder': 'Tu(s) Nombre(s)'}))
    last_name = forms.CharField(label = "Apellido(s)", widget=forms.TextInput(attrs={'placeholder': 'Tu(s) Apellido(s)'}))
    estado = forms.CharField(label="Estado de residencia", widget=forms.TextInput(attrs={'placeholder': '¿En qué estado resides?'}))
    municipio = forms.CharField(label = "Municipo de residencia", widget=forms.TextInput(attrs={'placeholder': '¿En qué municipio vives?'}))
    fecha_de_nacimiento = forms.DateField(label="Fecha de nacimiento (aaaa-mm-dd)", widget=forms.DateInput(attrs={"placeholder": f"{datetime.date.today()}"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Estudiante
        fields = ('first_name','last_name', 'password1' ,'password2', "escuela", "grado", "estado", "municipio", "fecha_de_nacimiento")
 
# Datos de tutor: (que por favor sea el mismo que realiza el pago)
# -Nombre completo  +
# -Parentesco
# -Contacto correo
# -Contacto wa

class TutorForm(forms.ModelForm):
    correo = forms.EmailField(
            label = "Correo de tu padre o tutor", 
            widget=forms.TextInput(
                attrs={'placeholder': 'correo@email.com'}
            )
    )
    nombre_completo = forms.CharField(
            label = "Nombre completo de un padre o tutor", 
            widget=forms.TextInput(
                attrs={'placeholder': 'Nombre completo de un padre o tutor'}
            )
    )
    parentesco = forms.CharField(
            label = "Parentesco", 
            widget=forms.TextInput(
                attrs={'placeholder': 'Padre, Madre, Tio, Tutor, etc.'}
            )
    )

    celular = PhoneNumberField(
            label = "Celular", 
            widget=forms.TextInput(
                attrs={'placeholder': '+523333445567'}
            )
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Tutor
        fields = ("nombre_completo", "parentesco", "correo", "celular")