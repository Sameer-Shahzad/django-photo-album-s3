from django.shortcuts import render, redirect

from .models import Category, Photo
from .forms import PhotoForm, CategoryForm

# Create your views here.

def gallery (request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    return render (request, 'photos/gallery.html', {'categories': categories, 'photos': photos})

def viewPhoto (request, pk):
    photos = Photo.objects.get(id=pk)
    return render (request, 'photos/photo.html', {'photos': photos})

def addPhoto(request):
    if request.method == 'POST':
        photo_form = PhotoForm(request.POST, request.FILES)
        category_form = CategoryForm(request.POST)

        if photo_form.is_valid() and category_form.is_valid():
            category_name = category_form.cleaned_data.get('name')
            if category_name:
                category, created = Category.objects.get_or_create(name=category_name)
            else:
                category = photo_form.cleaned_data['category']
                
            photo = photo_form.save(commit=False)
            photo.category = category
            photo.save()
            return redirect('gallery')
    else:
        photo_form = PhotoForm()
        category_form = CategoryForm()

    return render(request, 'photos/add.html', {
        'form': photo_form,
        'category_form': category_form
    })