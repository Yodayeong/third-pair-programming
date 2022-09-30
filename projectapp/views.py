from django.shortcuts import render
from .models import Board
# Create your views here.

def index(request):
    return render(request,'board/index.html')

def new(request):
    return render(request,'board/new.html')