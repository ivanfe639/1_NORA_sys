from django import forms
from django.forms.widgets import NumberInput


class authForm(forms.Form):
    
    usuario = forms.CharField()
    contrasena = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

class noraVerPedidos(forms.Form):

    fechaPedidos = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))


class noraForm(forms.Form):

    fecha = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    opcion1 = forms.CharField()
    opcion2 = forms.CharField()
    opcion3 = forms.CharField()
    opcion4 = forms.CharField()


CHOICES =(
    ("1", "Opcion 1"),
    ("2", "Opcion 2"),
    ("3", "Opcion 3"),
    ("4", "Opcion 4"),
)    

class clientsForm(forms.Form):
 
    nombre = forms.CharField(max_length=30, required=True)
    opciones = forms.ChoiceField( choices=CHOICES, required=True, label='Seleccione la opción')
    comentarios = forms.CharField(max_length=150, required=False)
