import re

pattern = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'

text = input()

match = re.findall(pattern, text)

destinations = []
travel_points = 0
if match:
    for i in range(len(match)):
        destinations.append(match[i][1])
        travel_points += len(match[i][1])

    print(f"Destinations: " + ', '.join(destinations))
    print(f"Travel Points: {travel_points}")
else:
    print(f"Destinations: ")
    print(f"Travel Points: 0")
