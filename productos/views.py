from rest_framework import viewsets
from .serializer import ProductosSerializer
from .models import Productos
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

class ProductosView(viewsets.ModelViewSet):
    serializer_class = ProductosSerializer
    queryset = Productos.objects.all()

def home(request):
    productosListados = Productos.objects.all()
    return render(request, "admProductos.html",{"productos":productosListados})

def registrarProducto(request):
    producto = request.POST['txtProducto']
    precio = request.POST['txtPrecio']
    cantidad = request.POST['txtCantidad']

    productos = Productos.objects.create(Productos=producto, Precios=precio, Stock=cantidad)
    messages.success(request, '¡Producto registrado!')
    return redirect('/')

def eliminarProducto(request, id):
    productos = Productos.objects.get(id=id)
    productos.delete()

    messages.success(request, '¡Producto eliminado!')

    return redirect('/')

def edicionProducto(request, id):
    productos = Productos.objects.get(id=id)
    return render(request, "edicionProductos.html", {"productos": productos})

def editarProducto(request):
    id = request.POST['txtid']
    nombre = request.POST['txtProducto']
    precio = float(request.POST['txtPrecio'])  # Convertir a float
    stock = int(request.POST['txtCantidad'])  # Convertir a int

    producto = Productos.objects.get(id=id)
    producto.Productos = nombre
    producto.Precios = precio
    producto.Stock = stock
    producto.save()

    messages.success(request, '¡Curso actualizado!')

    return redirect('/')