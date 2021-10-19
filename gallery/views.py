from django.shortcuts import render
from .models import *

def index(request):
  title = 'Nyota Gallery'
  photos = Image.objects.all()
  categories = Category.objects.all()
  locations = Location.objects.all()

  context={
    'title':title,
    'photos': photos,
    'categories':categories,
    'locations': locations
  }
  return render(request, 'index.html', context)