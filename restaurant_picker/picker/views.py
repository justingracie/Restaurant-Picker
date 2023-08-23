from django.http import HttpResponse

# Create your views here.

# change this page to return list of all records in the database/start with just restaurant names
from django.shortcuts import render

from picker.models import Restaurant


def index(request):
    return HttpResponse("Yummy choices coming soon!")


# function to return list of all restaurants in database

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return render(request, 'picker/restaurant_list.html', context)