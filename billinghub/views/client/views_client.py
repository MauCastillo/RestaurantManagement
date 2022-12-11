from django.shortcuts import render
from .forms import ClientForm


def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return render(request, 'generic_form.html', {'form': form, 'title_form': "Crear un nuevo cliente", 'saved': True, 'message': "Nuevo Cliente Registrado", 'type': "success"})
        else:
            return render(request, 'generic_form.html', {'form': form, 'title_form': "Crear un nuevo cliente", 'saved': True, 'message': "No se registro la venta", 'type': "error"})
    
    form = ClientForm()
    return render(request, 'generic_form.html', {'form': form, 'title_form': "Crear un nuevo cliente",'saved': False, 'message': "", 'type': "success"})