# Else & Finally Statements Challenge

cars = {'ford': 5, 'hyundai': 6}

def update_cars(data, key, val):
    try:
        data[key]
    except KeyError as e:
        print(f"No key {e} in dictionary")
    else:
        data[key] = val
    finally:
        return data


result = update_cars(cars, "mazda", 8)


# Do Not Place Code Below This Line 
# This will print out the cars dictionary after the update_cars function is called
print(cars)


