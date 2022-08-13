from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacto
from .forms import ContactoForm


def inicio(request, letra= NULL):
    if letra != NULL:
        contactos = Contacto.objects.filter(nombre__istartwhit= letra)
    else:
        contactos = Contacto.objects.filter(name__contains=request.GET.get('buscar', ''))

    return render(request, 'contacto/incio.html', {'contactos': contactos})


def vista(request, id):
    contacto = Contacto.objects.get(id=id)
    
    return render(request, 'contacto/detalles.html', {contacto})


def editar(request, id):
    contacto = Contacto.objects.get(id=id)
    
    if request.method == 'GET':
        formulario = ContactoForm(instance = contacto)

        return render(request, 'contacto/editar.html', {'formulario': formulario, 'id': id})

    if request.method == 'POST':
        formulario = ContactoForm(request.POST, instance= contacto)

        if formulario.is_valid():
            formulario.save()

        messages.success(request, '¡Contacto actualizado con exito!')

        return render(request, 'contacto/editar.html', {'formulario': formulario, 'id': id})


def crear(request):
    if request.method == 'GET':
        formulario = ContactoForm()

        return render(request, 'contacto/crear.html', {'formulario': formulario}) 

    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
        
        return redirect('contacto')


def borrar(request, id):
    contacto = Contacto.objects.get(id=id)
    contacto.delete()

    return render('contacto')

