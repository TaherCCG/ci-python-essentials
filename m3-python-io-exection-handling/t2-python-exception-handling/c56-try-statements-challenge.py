# Try Statements Challenge

cars = {'ford': 10, 'opel': 5 }
def get_val(key):
    try:
        return cars[key]
    except KeyError:
        return None
        
ford = get_val('ford')
print(ford)

hyundai = get_val('hyundai')
print(hyundai)

