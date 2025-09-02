from django.shortcuts import render, redirect

from .models import Category, Photo
from .forms import PhotoForm

# Create your views here.

def gallery (request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    return render (request, 'photos/gallery.html', {'categories': categories, 'photos': photos})

def viewPhoto (request, pk):
    photos = Photo.objects.get(id=pk)
    return render (request, 'photos/photo.html', {'photos': photos})

def addPhoto (request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/gallery/')
        return render(request, 'photos/add.html', {'form': form})
    else:
        form = PhotoForm()
        return render (request, 'photos/add.html', {'form': form})

