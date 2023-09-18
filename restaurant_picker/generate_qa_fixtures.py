import json
import os
import random

from django.contrib.auth.hashers import make_password

users = [
    {
        "email": "justin@crafted.solutions",
        "password": "hydromelon",
        "is_superuser": True,
    },
    {
        "email": "ted@crafted.solutions",
        "password": "hearty_durian",
        "is_superuser": True,
    },
]

restaurants = [
    {
        "name": "Blue Agave Grill",
        "address": "1201 16th St Mall # 104, Denver, CO 80202",
        "phone_number": "+17205508389",
        "website": "http://denver.blueagavegrillcolorado.com/",
        "description": "Southwestern food",
        "menu": "https://denver.blueagavegrillcolorado.com/denver-lodo-blue-agave-grill-denver-food-menu",
    }, {
        "name": "CAVA",
        "address": "1460 16th St Mall, Denver, CO 80202",
        "phone_number": "+13038569692",
        "website": "http://cava.com/",
        "description": "Mediterranean",
        "menu": "https://cava.com/menu",
    }, {
        "name": "The Cheesecake Factory",
        "address": "1201 16th St Mall, Denver, CO 80202",
        "phone_number": "+13035950333",
        "website": "https://locations.thecheesecakefactory.com/co/denver-19.html?utm_source=Google&utm_medium=Maps&utm_campaign=Google+Places",
        "description": "American chain restaurant",
        "menu": "https://www.thecheesecakefactory.com/locations/denver-co/menu/?utm_source=SEARCH&utm_medium=GOOGLE&utm_content=MENU&utm_campaign=GOOGLE_SEARCH_MENU",
    }, {
        "name": "What the Pho?",
        "address": "1600 Champa St #110, Denver, CO 80202",
        "phone_number": "+13036232702",
        "website": "http://whatthepho.epipay.com/",
        "description": "Vietnamese food",
        "menu": "http://whatthepho.epipay.com/",
    }, {
        "name": "The Delectable Egg",
        "address": "1625 Court Pl, Denver, CO 80202",
        "phone_number": "+13038925720",
        "website": "http://www.delectableegg.com/",
        "description": "Brunch food",
        "menu": "http://www.delectableegg.com/",
    }
]


def create_user_fixtures(users):
    fixtures = []

    for index, user in enumerate(users):
        fixtures.append({
            "model": "auth.User",
            "pk": index + 1,
            "fields": {
                "username": user.get("email"),
                "email": user.get('email'),
                "password": make_password(user.get('password', "ted_is_the_best")),
                "is_staff": True,
                "is_superuser": user.get("is_superuser", False),
                "last_login": "2022-10-31T13:20:30+03:00",
                "user_permissions": user.get("user_permissions", []),
            }
        })
    return fixtures


def generate_restaurant_fixtures(restaurants):
    fixtures = []

    for index, restaurant in enumerate(restaurants):
        fixtures.append({
            "model": "picker.Restaurant",
            "pk": index + 1,
            "fields": {
                **restaurant,
                "rating": random.randint(1, 10),
                "service_speed": random.randint(1, 10),
                "price": random.randint(1, 10),
            }
        })

    return fixtures


user_fixtures = create_user_fixtures(users)
restaurant_fixtures = generate_restaurant_fixtures(restaurants)

file = './picker/fixtures/setup_qa.json'

all_fixtures = user_fixtures + restaurant_fixtures

if os.path.exists(file):
    os.remove(file)

with open(file, "x") as outfile:
    json.dump(all_fixtures, outfile)
