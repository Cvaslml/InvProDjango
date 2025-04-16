from django.db import models
from django.contrib.auth.models import User

# Modelo de la tabla Categoria (categorías de productos)
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre

# Modelo de la tabla Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con usuario (quién maneja el producto)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con categoría
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

# Modelo de la tabla Comentario (para productos)
class Comentario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="comentarios")  # Relación con producto
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con usuario (quién comenta)
    contenido = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.first_name} sobre {self.producto.nombre}"
