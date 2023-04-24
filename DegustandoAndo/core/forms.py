from django import forms
from django.core.validators import FileExtensionValidator
    
class ArticulosForm(forms.Form):
    titulo =forms.CharField(max_length=100, label= "Indique nombre del establecimiento")
    subtitulo =forms.CharField(max_length=140, label= "Indique en breve palabras el rubro")
    ubicacion =forms.CharField(max_length=100, label= "Indique ubicacion, a modo de: Ciudad, Provincia, País")
    cuerpo =forms.CharField(widget=forms.Textarea, label="Inserte su propia reseña")
    imagen = forms.FileField(required=False, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])], label="Imagen")
    autor =forms.CharField(max_length=100)
    fecha = forms.DateTimeField()

