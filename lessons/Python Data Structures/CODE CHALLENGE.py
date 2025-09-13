#CODE CHALLENGE 

# challenge 1
def create_tractor(model, colour, horsepower, fuel_capacity):
    tractor = {
        'model' : model, 
        'colour' : colour, 
        'horsepower' : horsepower, 
        'fuel_capacity' : fuel_capacity
    }
    return tractor
create_tractor('rex', 'blue', 40 , '80L')

# challenge 2
def plant_row(field, row_to_plant):
    field[row_to_plant] = [1] * len(field[row_to_plant])
    print(field)
    return field
plant_row([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 0)

# challenge 3
existing_vehicles = [
    {'model': 'TX-240', 'colour': 'Green', 'horsepower': 150, 'fuel_capacity': 60},
    {'model': 'RX-1500', 'colour': 'Red', 'horsepower': 120, 'fuel_capacity': 45}
]
def add_vehicle(vehicles, new_vehicle_params):
    # existing_vehicles.extend(vehicles)
    new_vehicle = dict(
        model = new_vehicle_params[0], 
        colour = new_vehicle_params[1],
        horsepower = new_vehicle_params[2],
        fuel_capacity = new_vehicle_params[3],
    )
    vehicles.append(new_vehicle)
    print(vehicles)
    return vehicles
new_vehicle =  ('SX-750', 'White', 180, 80)
add_vehicle(existing_vehicles, new_vehicle)