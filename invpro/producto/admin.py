from django.contrib import admin
from .models import Producto, Categoria, Comentario

# Administración del modelo Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad', 'autor', 'categoria', 'created_at')
    list_filter = ('categoria', 'created_at')
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

# Administración del modelo Categoria
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

# Administración del modelo Comentario
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'autor', 'created_at')
    search_fields = ('producto__nombre', 'autor__username', 'contenido')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

# Registro de modelos en el panel de administración
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Comentario, ComentarioAdmin)

# Personalización del panel de administración
admin.site.site_header = "Administración del Inventario"
admin.site.site_title = "Panel de Inventario"
admin.site.index_title = "Gestión de Productos, Categorías y Comentarios"
