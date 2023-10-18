from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('cuentas', views.cuentas, name='cuentas'),
    path('cuentas/datos/<int:id>', views.datos, name='datos'),
]