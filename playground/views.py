from django.shortcuts import render
from django.conf import settings
from django.apps import apps
from django.shortcuts import render, get_object_or_404, redirect
from foods.models import Food
from rooms.models import Room, RoomCategory

def home_view(request,):
    context = {
        'project_name': settings.PROJECT_NAME
    }    
    return render(request, "index.html", context) # Renders the index.html from the templates directory
def contact_page(request,):
    return render(request, "contact.html", {}) # Renders the contact.html from the templates directory  
def about_page(request,):
    return render(request, "about.html", {}) # Renders the about.html from the templates directory  
     
def food_page(request):
    food_list = Food.objects.all()
    return render(request, "foods/index.html", {'food_list': food_list}) # Renders the food.html from the templates directory 

def food_detail(request, food_id):
    # Fetch specific room for the "View" button
    food = get_object_or_404(Food, id=food_id)
    return render(request, 'foods/detail.html', {'food': food})



def rooms_page(request):

    room_list = Room.objects.all()
    return render(request, 'rooms/index.html', {'room_list': room_list})  # Renders the rooms.html from the templates directory  


def room_detail(request, room_id):
    # Fetch specific room for the "View" button
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'rooms/detail.html', {'room': room})

def buy_room(request, room_id):
    # Add room to session "cart"
    room = get_object_or_404(Room, id=room_id)
    booking_cart = request.session.get('booking_cart', {})

    # Store room details in session
    booking_cart[str(room.id)] = {
        'name': room.name,
        'price': float(room.price),
        'image': room.image.url
    }

    request.session['booking_cart'] = booking_cart
    return redirect('booking_summary')

def booking_summary(request):
    # Show what the user has "Bought"
    cart = request.session.get('booking_cart', {})
    total = sum(item['price'] for item in cart.values())
    return render(request, 'rooms/summary.html', {'cart': cart, 'total': total})