from django.shortcuts import render
from projectapp.models import Board
from django.db.models import Q

# Create your views here.
def search(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        results = Board.objects.all().filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(user__icontains=query)
        )

        return render(request, 'search/search.html', {'query': query, 'results': results})

# 후기 : 좋은 팀원을 만나서 즐겁게 작업을 할수 있었던것 같습니다. 