import math
from geopy.geocoders import Nominatim

coordinates = [(1, 2), (3, 4), (5, 6)]

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_device_location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode("Your IP Address")  # Replace with actual IP address or use a service to get it
    return location.longitude, location.latitude

def convert_to_xy(longitude, latitude):
    return longitude, latitude

user_longitude, user_latitude = get_device_location()
user_x, user_y = convert_to_xy(user_longitude, user_latitude)

distances = [calculate_distance(user_x, user_y, coord[0], coord[1]) for coord in coordinates]

min_distance_index = distances.index(min(distances))

print(f"The closest coordinate is: {coordinates[min_distance_index]}")