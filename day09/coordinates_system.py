import math

# 1. Store city locations as (Name, Lat, Lon)
cities = [
    ("Lahore", 31.5204, 74.3587),
    ("Karachi", 24.8607, 67.0011),
    ("Islamabad", 33.6844, 73.0479)
]

def calculate_distance(coord1, coord2):
    # Tuple Unpacking: extract lat/lon from the tuples
    _, lat1, lon1 = coord1
    _, lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

# 2. Find closest city
my_location = ("User", 31.0, 74.0)
distances = [(city[0], calculate_distance(my_location, city)) for city in cities]
closest_city = min(distances, key=lambda x: x[1])

print(f"Closest City: {closest_city[0]} (Distance: {closest_city[1]:.2f})")

# 3. Demonstrate Immutability
try:
    cities[0][1] = 32.0  # Attempting to change latitude
except TypeError as e:
    print(f"\n❌ Immutability Proof: {e}")