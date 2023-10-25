from django.contrib import admin
from .models import Cuenta

# Register your models here.

class CuentaAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "date",)
  
admin.site.register(Cuenta, CuentaAdmin)