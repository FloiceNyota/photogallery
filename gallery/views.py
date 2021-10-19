from django.shortcuts import render
from .models import *

def index(request):
  title = 'Nyota Gallery'
  context={

  }
  return render(request, 'index.html', context)