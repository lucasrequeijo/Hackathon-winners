import math

coordinates = [(1, 2), (3, 4), (5, 6)]

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

user_x = float(input("Enter your x coordinate: "))
user_y = float(input("Enter your y coordinate: "))

distances = [calculate_distance(user_x, user_y, coord[0], coord[1]) for coord in coordinates]

min_distance_index = distances.index(min(distances))

print(f"The closest coordinate is: {coordinates[min_distance_index]}")