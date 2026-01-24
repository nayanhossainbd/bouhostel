from django.shortcuts import render

# Create your views here.
def foods_list(request):
    return render(request, 'foods/foods_list.html')
