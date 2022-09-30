from django.shortcuts import render, redirect
from .models import Board
# Create your views here.

def index(request):
    boards = Board.objects.all()

    return render(request,'board/index.html', {'boards': boards})

def new(request):
    return render(request,'board/new.html')

def create(request):
    boards = request.GET.get('board')
    title = request.GET.get('title')
    user = request.GET.get('user')
    content = request.GET.get('content')

    Board.objects.create(boards=boards, title=title, user=user, content=content)

    return redirect('board:index')