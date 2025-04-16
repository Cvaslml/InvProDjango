from django import forms
from .models import Producto, Comentario

# Formulario para crear y editar productos
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad', 'categoria']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

# Formulario para agregar comentarios a un producto
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']  # Asegúrate de que tu modelo Comentario tenga este campo
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }
