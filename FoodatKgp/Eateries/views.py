from django.shortcuts import render
from .models import Restaurants

# Create your views here.
def index(request):
    restaurants = Restaurants.objects.all()
    return render(request, 'index.html', {"restaurants": restaurants})

def restaurant_show(request, restaurant_id):
    restaurant = Restaurants.objects.get(id=restaurant_id)
    return render(request, 'restaurant.html', {'restaurant': restaurant})