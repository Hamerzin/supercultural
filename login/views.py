from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login_request(request):
    
      if request.method == "POST":
          
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username = usuario , password = contra)
                  print(1)
                  if user is not None:
                        login(request, user)

                        return redirect('index')
                  else:
                        print(2)
                        return render (request, "index.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "login.html", {'form': form,"mensaje":"Login incorrecto , Reintente"})
      
      form = AuthenticationForm()
      print(3)
      return render(request, "login.html", {'form': form})




def register(request):
      
      if request.method == "POST":

            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()

                  return render(request, "register.html", {"mensaje": "usuario creado con exito. Dirijase al login"})

      else: 
            form = UserRegisterForm()

      return render(request, "register.html", {"form": form})