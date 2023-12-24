from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import FoodTruck
import math

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Radius of Earth in kilometers
    radius = 6371.0

    # Calculate the distance
    distance = radius * c
    return distance

def find_foodtrucks(request):
    user_latitude = 0.0
    user_longitude = 0.0
    nearby_foodtrucks = []
    error_message = None

    page = request.GET.get('page', 1)  # Get the current page from the query parameters

    if request.method == 'POST':
        try:
            user_latitude = float(request.POST.get('latitude', 0.0))
            user_longitude = float(request.POST.get('longitude', 0.0))

            user_location = (user_latitude, user_longitude)

            # Store user's search query in the session
            request.session['user_location'] = user_location

            # Find food trucks within a certain distance (1 kilometer using Haversine for demonstration)
            foodtrucks = FoodTruck.objects.all()

            for foodtruck in foodtrucks:
                foodtruck_location = (foodtruck.latitude, foodtruck.longitude)
                distance = haversine(user_location[0], user_location[1], foodtruck_location[0], foodtruck_location[1])

                # Check if the distance is within 1 kilometer (adjust as needed)
                if distance <= 1.8:
                    nearby_foodtrucks.append(foodtruck)

            if not nearby_foodtrucks:
                error_message = "No food trucks found near your location"

        except ValueError as e:
            error_message = f"Invalid latitude/longitude input: {e}"
    else:
        # If the request is not POST, retrieve user's search query from the session
        user_location = request.session.get('user_location', (0.0, 0.0))

        # Find food trucks within a certain distance based on user's search query
        foodtrucks = FoodTruck.objects.all()

        for foodtruck in foodtrucks:
            foodtruck_location = (foodtruck.latitude, foodtruck.longitude)
            distance = haversine(user_location[0], user_location[1], foodtruck_location[0], foodtruck_location[1])

            # Check if the distance is within 1 kilometer (adjust as needed)
            if distance <= 1.8:
                nearby_foodtrucks.append(foodtruck)

    # Implement pagination using Django Paginator
    items_per_page = 6
    paginator = Paginator(nearby_foodtrucks, items_per_page)

    try:
        current_page_items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        current_page_items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        current_page_items = paginator.page(paginator.num_pages)

    # Calculate the page numbers to display
    display_pages = paginator.page_range

    # Render the template with all relevant sections
    return render(request, 'find_foodtrucks.html', {
        'user_latitude': user_latitude,
        'user_longitude': user_longitude,
        'error_message': error_message,
        'foodtrucks': current_page_items,
        'current_page': int(page),
        'display_pages': display_pages,
        'last_page': paginator.num_pages,
    })
