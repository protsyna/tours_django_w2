from random import randrange

from django.shortcuts import render
from django.views import View

import tours.data as data
from stepik_tours.settings import NUMBER_OF_TOURS_ON_MAIN_PAGE


def get_night(id):
    if data.tours[id]['nights'] in [1, 21]:
        return 'ночь'
    elif data.tours[id]['nights'] in range(5, 21):
        return 'ночей'
    else:
        return 'ночи'


# Main page
class MainView(View):
    def get(self, request):
        # Get six random tours
        tours = {}
        while True:
            item = randrange(1, len(data.tours)+1)
            if item not in tours:
                tours[item] = data.tours[item]
            if len(tours) >= NUMBER_OF_TOURS_ON_MAIN_PAGE:
                break

        context = {'tours': tours,
                   'main_title': data.main_title,
                   'subtitle': data.subtitle,
                   'description': data.description,
                   'menu_departures': data.departures,
                   'menu_title': data.title}

        return render(request, "tours/index.html", context)


# Departure page
class DepartureView(View):
    def get(self, request, departure):
        # Checking on correct data
        if departure not in data.departures:
            # Debug message
            print('ERROR: departure is not valid')
            departure = list(data.departures)[1]

        tours = {}
        count_tours = 0
        prices, nights = [], []
        for tour in data.tours:
            if data.tours[tour]['departure'] == departure:
                tours[tour] = data.tours[tour]
                count_tours += 1
                prices.append(data.tours[tour]['price'])
                nights.append(data.tours[tour]['nights'])

        context = {'departure': data.departures_short[departure],
                   'tours': tours,
                   'count_tours': count_tours,
                   'price_min': min(prices),
                   'price_max': max(prices),
                   'nights_min': min(nights),
                   'nights_max': max(nights),
                   'menu_departures': data.departures,
                   'menu_title': data.title}

        return render(request, "tours/departure.html", context)


# Tour page
class TourView(View):

    def get(self, request, id):
        # Checking on correct data
        if not (id in data.tours):
            # Debug message
            print('ERROR: id is not valid, set id = 1')
            id = 1

        context = {'menu_departures': data.departures,
                   'menu_title': data.title,
                   'tour': data.tours[id],
                   'departure': data.departures_short[data.tours[id]['departure']],
                   'stars': data.stars[data.tours[id]['stars']],
                   'night': get_night(id)}

        return render(request, "tours/tour.html", context)
