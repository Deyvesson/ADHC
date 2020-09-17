from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Socio
from .forms import SocioForm
from django.contrib import messages

def listaSocios(request):
    socios = Socio.objects.all().order_by('socio_nome')
    return render(request, 'socios/lista.html', {'socios':socios})

def socioView(request, id):
    socio = get_object_or_404(Socio, pk=id)
    return render(request, 'socios/socio.html', {'socio':socio})

def novoSocio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            socio = form.save()
            return redirect('/')
    else:
        form = SocioForm()
        return render(request, 'socios/addsocio.html', {'form': form})

def editSocio(request, id):
    socio = get_object_or_404(Socio, pk=id)
    form = SocioForm(instance=socio)

    if(request.method == 'POST'):
        form = SocioForm(request.POST, instance=socio)

        if(form.is_valid()):
            socio.save()
            return redirect('/')
        else:
            return render(request, 'socios/editSocio.html', {'form':form, 'socio':socio})

    else:
        return render(request, 'socios/editSocio.html', {'form':form, 'socio':socio})

def deleteSocio(request, id):
    socio = get_object_or_404(Socio, pk=id)
    socio.delete()

    messages.info(request, 'Socio deletado com sucesso')

    return redirect('/')