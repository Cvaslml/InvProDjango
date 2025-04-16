from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal con productos
    path('productos/', views.productos, name='productos'),  # Lista de productos (solo admin)
    path('producto/nuevo/', views.nuevo_producto, name='nuevo_producto'),  # Crear nuevo producto (solo admin)
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),  # Detalle de producto
    path('producto/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),  # Editar producto (solo admin)
    path('producto/<int:producto_id>/borrar/', views.borrar_producto, name='borrar_producto'),  # Borrar producto (solo admin)
    path('categorias/', views.categorias, name='categorias'),  # Lista de categorías (filtro de productos)
    path('perfil/', views.perfil, name='perfil'),
]
