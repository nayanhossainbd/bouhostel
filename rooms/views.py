from django.shortcuts import render

# Create your views here.

def rooms_list(request):
    return render(request, 'rooms/rooms_list.html')
