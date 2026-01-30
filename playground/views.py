from django.shortcuts import render
from django.conf import settings
from django.apps import apps
from django.shortcuts import render, get_object_or_404, redirect
from foods.models import Food,FoodCategory
from rooms.models import Room, RoomCategory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from .models import FoodOrderRecord, RoomBookingRecord, Profile
from django.contrib import messages
# --- Authentication Views ---

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in after registration
            return redirect('food_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# --- Protected Booking/Order Views ---
@login_required
def profile_view(request):
    if request.method == 'POST':
        # Update personal information
        profile = request.user.profile
        profile.phone = request.POST.get('phone')
        profile.address = request.POST.get('address')
        profile.save()
        messages.success(request, "Information updated!")
        return redirect('profile')

    # Get history from database
    food_history = FoodOrderRecord.objects.filter(user=request.user).order_by('-order_date')
    room_history = RoomBookingRecord.objects.filter(user=request.user).order_by('-booking_date')

    return render(request, 'registration/profile.html', {
        'food_history': food_history,
        'room_history': room_history
    })


@login_required
def checkout_food(request):
    # ... logic ...
    return redirect('profile')

@login_required
def checkout_room(request):
    # ... logic ...
    return redirect('profile')

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
    categories = FoodCategory.objects.prefetch_related('foods').all()
    
    return render(request, "foods/index.html", {'foods_list': categories}) # Renders the food.html from the templates directory 
def food_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    return render(request, 'foods/details.html', {'food': food})


def order_food(request, food_id):
    if request.method == 'POST':
        food = get_object_or_404(Food, id=food_id)
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity', 1))
        
        # Determine price based on selection
        price = food.medium_price if size == 'medium' else food.large_price
        
        # Get current order from session or create new
        order_cart = request.session.get('food_order', {})
        
        # Unique key for item + size
        item_key = f"{food_id}_{size}"
        
        order_cart[item_key] = {
            'name': f"{food.name} ({size.capitalize()})",
            'price': float(price),
            'quantity': quantity,
            'total': float(price * quantity)
        }
        
        request.session['food_order'] = order_cart
        return redirect('booking_summary') # Redirect to your cart/summary page
    return redirect('foods_list')


def rooms_page(request):

    room_list = Room.objects.all()
    return render(request, 'rooms/index.html', {'room_list': room_list})  # Renders the rooms.html from the templates directory  


def room_detail(request, room_id):
    # Fetch specific room for the "View" button
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'rooms/detail.html', {'room': room})
@login_required
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
    return render(request, 'summary.html', {'cart': cart, 'total': total})