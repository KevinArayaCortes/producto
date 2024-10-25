from django.contrib import admin
from productoApp.models import Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['Tipo', 'Nombre', 'Descripcion', 'Stock', 'Precio']

admin.site.register(Producto, ProductoAdmin)