from django.shortcuts import render, redirect
from productoApp.forms import ProductoForm
from productoApp.models import Producto

def index(request):
    return render(request, 'productoApp/index.html')

def listadoProducto(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'productoApp/productos.html', data)

def agregarProductos(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productos')
        else:
            return render(request, 'productoApp/agregarProducto.html', {'form': form})
    data = {'form': form}
    return render(request, 'productoApp/agregarProducto.html', data)

def actualizarProductos(request, id):
    producto = Producto.objects.get(id=id)
    form = ProductoForm(instance=producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/productos')
    data = {'form': form}
    return render(request, 'productoApp/agregarProducto.html', data)

def eliminarProductos(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/productos')