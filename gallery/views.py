from django.shortcuts import render
from .models import *

def index(request):
  title = 'Nyota Gallery'
  photos = Image.objects.all()

  context={
    'title':title,
    'photos': photos,
  }
  return render(request, 'index.html', context)