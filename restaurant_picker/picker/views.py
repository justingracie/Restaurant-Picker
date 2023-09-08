from django.http import HttpResponse
import random
import logging

# Create your views here.

# change this page to return list of all records in the database/start with just restaurant names
from django.shortcuts import render

from picker.models import Restaurant

LOGGER = logging.getLogger()


def index(request):
    LOGGER.info("reaching index view method")
    return HttpResponse("Yummy choices coming soon!")


# function to return list of all restaurants in database

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return render(request, 'picker/restaurant_list.html', context)


def choose_for_me(request):
    if request.method == 'POST':
        choices = Restaurant.objects.count()
        choose = random.randint(0, choices - 1)
        the_choice = Restaurant.objects.all()[choose]

        print(the_choice.name)

        context = {'the_choice': the_choice}
        return render(request, 'picker/choose_for_me.html', context)

    return render(request, 'picker/choose_for_me.html')
