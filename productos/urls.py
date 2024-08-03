from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from productos import views

router = routers.DefaultRouter()
router.register(r'productos',views.ProductosView,'productos')

urlpatterns= [
    path('',views.home),
    path('registrarProducto/', views.registrarProducto),
    path('edicionProducto/<id>', views.edicionProducto),
    path('editarProducto/', views.editarProducto),
    path('eliminarProducto/<id>', views.eliminarProducto),
    path("api/crud/",include(router.urls)),
    path('documentacion/',include_docs_urls(title="Productos API"))
]