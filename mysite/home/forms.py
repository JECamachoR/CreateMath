from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import *
from crispy_forms.helper import FormHelper

class UserCreationForm_custom(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label = "Nombre(s)", widget=forms.TextInput(attrs={'placeholder': 'Tu(s) Nombre(s)'}))
    last_name = forms.CharField(label = "Apellido(s)", widget=forms.TextInput(attrs={'placeholder': 'Tu(s) Apellido(s)'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # widget=forms.TextInput(attrs={'placeholder': 'Tu(s) Nombre(s)'})
        self.fields["username"].label = "Nombre de usuario"
        self.fields["username"].widget = forms.TextInput(attrs={'placeholder': 'Nombre de usuario'})
        self.fields["email"].widget = forms.TextInput(attrs={'placeholder': 'tu@email.com'})
        self.fields["password1"].label = "Contraseña"
        self.fields["password1"].widget = forms.TextInput(attrs={'placeholder': 'Contraseña'})
        self.fields["password2"].label = "Repite tu contraseña"
        self.fields["password2"].widget = forms.TextInput(attrs={'placeholder': 'Repite tu contraseña'})

    class Meta():
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1' ,'password2' )
    
class StudentForm(forms.ModelForm):
    escuela = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'El nombre de tu escuela'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Estudiante
        fields = ("escuela", "grado")
        # labels = {
        #     'name': _('Writer'),
        # }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }