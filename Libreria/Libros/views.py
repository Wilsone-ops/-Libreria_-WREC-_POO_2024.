from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm

# Listar libros
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})

# Crear un nuevo libro
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/formulario_libro.html', {'form': form})

# Editar un libro existente
def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/formulario_libro.html', {'form': form})

# Eliminar un libro
def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'libros/confirmar_eliminacion.html', {'libro': libro})
