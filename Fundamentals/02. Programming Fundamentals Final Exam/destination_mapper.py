import re

pattern = r"(=|\/)([A-Z][A-Za-z]+)\1"

text = input()

destinations = re.findall(pattern, text)

valid_destinations = []
travel_points = 0
for item in destinations:
    for destination in item:
        if len(destination) >= 3:
            valid_destinations.append(destination)
            travel_points += len(destination)
print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")
