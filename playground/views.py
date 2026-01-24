from django.shortcuts import render
from django.conf import settings
from django.apps import apps

def home_view(request,):
    context = {
        'project_name': settings.PROJECT_NAME
    }
    
    return render(request, "index.html", context) # Renders the index.html from the templates directory
def contact_page(request,):
    return render(request, "contact.html", {}) # Renders the contact.html from the templates directory  
def about_page(request,):
    return render(request, "about.html", {}) # Renders the about.html from the templates directory  
     
def food_page(request,):
    return render(request, "foods.html", {}) # Renders the food.html from the templates directory 


def rooms_page(request,list):

    room_list = Rooms.objects.all()
    context = {
        'rooms': room_list,
    }
    return render(request, 'rooms.html',context)  # Renders the rooms.html from the templates directory