from django import forms
    
class ArticulosForm(forms.Form):
    titulo =forms.CharField(max_length=100, label= "Indique nombre del establecimiento")
    subtitulo =forms.CharField(max_length=140, label= "Indique en breve palabras el rubro")
    ubicacion =forms.CharField(max_length=100, label= "Indique ubicacion, a modo de: Ciudad, Provincia, País")
    cuerpo =forms.CharField(widget=forms.Textarea, label="Inserte su propia reseña")
    autor =forms.CharField(max_length=100)
    fecha = forms.DateTimeField()

