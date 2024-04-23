from django.shortcuts import redirect, render

from .forms import ContactFormModelForm
from .models import Flan, ContactForm

# Create your views here.

def indice(request):
    flanes_publicos = Flan.objects.filter(is_private = False)
    return render(request, 'index.html', {'flanes_publicos': flanes_publicos})

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    return render(request, 'welcome.html', {})

def exito(request):
    return render(request, 'exito.html', {})

def contacto(request):
    if request.method == 'POST':
        #Crea una instancia llamada form y la llena con la data del request
        form = ContactFormModelForm(request.POST)
        #Revisa si es valido
        if form.is_valid():
            #Procesa la data en form.cleaned_data como se requiere.
            form.save()
            #Redirige a una nueva URL de si serlo.
            return redirect('exito')
    #De no cumplir con estas condiciones, creara un form en blanco.
    else:
        form = ContactFormModelForm()     

    return render(request, 'contacto.html',{'form': form})
