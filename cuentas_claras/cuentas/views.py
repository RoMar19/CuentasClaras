from django.http import HttpResponse
from django.template import loader
from .models import Cuenta

def cuentas(request):
  miscuentas = Cuenta.objects.all().values()
  template = loader.get_template('todas_cuentas.html')
  context = {
    'miscuentas': miscuentas,
  }
  return HttpResponse(template.render(context, request))

def datos(request, id):
  micuenta = Cuentas.objects.get(id=id)
  template = loader.get_template('datos.html')
  context = {
    'miscuentas': miscuentas,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
