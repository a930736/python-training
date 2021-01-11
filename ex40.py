cities = {"CA": "San Francisco", "MI":"Detroit", "FL": "Jacksonville"}

cities["NY"] = "New York"

cities["OR"] = "Portland"

def find_city(themap, state):
    if state in themap:
        return themap[state]

    else:
        return "Not found."

cities["_find"] = find_city

while True:
    print("State ? (Enter to quit)")
    state = input(">")
    if not state:
        break
    x = find_city(cities, state)

    print(x)

print(cities)
