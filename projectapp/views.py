from django.shortcuts import render, redirect
from .models import Board
# Create your views here.

def index(request):
    boards = Board.objects.all()

    return render(request,'board/index.html', {'boards': boards})

def new(request):
    return render(request,'board/new.html')

def create(request):
    new_board = Board()
    new_board.title = request.GET.get('title')
    new_board.user = request.GET.get('user')
    new_board.content = request.GET.get('content')
    new_board.boards = request.GET.get('board')
    new_board.save()
    
    return redirect('board:detail',new_board.id)

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board' : board,
    }
    return render(request,'board/detail.html', context)

def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('board:index')

def update(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board':board,
    }
    return render(request,'board/update.html',context)

def updateF(request,pk):
    content = request.GET.get('content')
    title = request.GET.get('title')
    user = request.GET.get('user')
    b = request.GET.get('board')

    board = Board.objects.get(pk=pk)
    board.content = content
    board.title = title
    board.user = user
    board.boards = b
    board.save()

    return redirect('board:detail',pk)