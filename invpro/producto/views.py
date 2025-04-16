from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm, ComentarioForm
from django.contrib.auth.models import User
from .models import Producto, Categoria, Comentario
from django.contrib.auth.decorators import login_required

# Vista principal: muestra los productos recientes en la página de inicio
def index(request):
    productos_recientes = Producto.objects.all().order_by('-created_at')[:6]  # Últimos 6 productos
    return render(request, 'producto/index.html', {'productos_recientes': productos_recientes})

# Vista para filtrar productos por categoría
@login_required
def categorias(request):
    categorias = Categoria.objects.all()
    categoria_id = request.GET.get('categoria')  # Captura la categoría seleccionada
    productos = Producto.objects.all().order_by('-created_at')  # Asegúrate de que el modelo tenga 'created_at'

    if categoria_id:
        categoria = get_object_or_404(Categoria, id=categoria_id)
        productos = productos.filter(categoria=categoria)  # O ajusta según tu campo FK

    return render(request, 'producto/categorias.html', {
        'categorias': categorias,
        'productos': productos,
        'categoria_seleccionada': categoria_id
    })

# Vista para ver los productos (solo accesible para admin o staff)
@login_required
def productos(request):
    if not request.user.is_staff:
        return redirect('index')  # Redirige a la página de inicio si no es admin o staff

    productos = Producto.objects.all().order_by('-created_at')
    return render(request, 'producto/productos.html', {'productos': productos})

# Vista del perfil del usuario
@login_required
def perfil(request):
    return render(request, 'producto/perfil.html', {'usuario': request.user})

# Vista para agregar un nuevo producto (solo para admin)
@login_required
def nuevo_producto(request):
    if not request.user.is_staff:
        return redirect('index')  # Redirige a la página de inicio si no es admin o staff

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.autor = request.user
            producto.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'producto/nuevo_producto.html', {'form': form})

# Vista para editar un producto existente (solo para el autor o admin)
@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    # Protección de acceso
    if request.user != producto.autor and not request.user.is_staff:
        return redirect('productos')  # Redirige si no es el autor ni admin

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto/editar_producto.html', {'form': form})

# Vista para eliminar un producto (solo para el autor o admin)
@login_required
def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    # Protección de acceso
    if request.user != producto.autor and not request.user.is_staff:
        return redirect('productos')  # Redirige si no es el autor ni admin

    if request.method == 'POST':
        producto.delete()
        return redirect('productos')

    return render(request, 'producto/borrar_producto.html', {'producto': producto})

# Vista para ver el detalle de un producto y agregar comentario (solo accesible para admin o staff)
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    comentarios = producto.comentarios.all().order_by('-created_at')  # Trae todos los comentarios ordenados por fecha
    form = ComentarioForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.producto = producto
                comentario.autor = request.user
                comentario.save()
                return redirect('detalle_producto', producto_id=producto.id)
        else:
            return redirect('login')

    return render(request, 'producto/detalle_producto.html', {
        'producto': producto,
        'comentarios': comentarios,
        'form': form
    })
