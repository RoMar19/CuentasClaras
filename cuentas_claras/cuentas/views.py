from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cuenta

def cuentas(request):
  miscuentas = Cuenta.objects.all().values()
  template = loader.get_template('todas_cuentas.html')
  context = {
    'miscuentas': miscuentas,
  }
  return HttpResponse(template.render(context, request))

def datos(request, id):
  micuenta = Cuenta.objects.get(id=id)
  template = loader.get_template('datos.html')
  context = {
    'micuenta': micuenta,
  }
  return HttpResponse(template.render(context, request))

def signup(request):

  if request.method == 'GET':
    return render (request, 'signup.html', {
    'form':  UserCreationForm
  })
  
  else:
    if request.POST['password1'] == request.POST['password2']:
      try:
        user = User.objects.create_user(username=request.POST['username'],
        password=request.POST['password1'])
        user.save()
        return HttpResponse('Usuario creado correctamente')
      except:
        return render (request, 'signup.html', {
          'form':  UserCreationForm,
          "error": 'El usuario ya existe'
        })
        return render (request, 'signup.html', {
          'form':  UserCreationForm,
          "error": 'El password no coincide'
         })

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())




