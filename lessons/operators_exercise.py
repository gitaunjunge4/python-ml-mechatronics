#Compute kinetic energy for a list of mass/velocity pairs

#steps
# get the data
# create a function that maps thru the data and changes it to float & returns it 
# pass it thru a for loop to calculate the KE 
# KE= 0.5 * M * V ** 2 
# print to the terminal
#"Mass -> {mass} Velocity -> {velocity} KE ->{KE}"
#using re.sub(r[^0-9.\-], "", text)

import re

#data
masses = ["50kg", "70", "100 kg", "ten", "85.5kg"]
velocities = ["10m/s", "15", "20.0 m/s", "five", "0"]

def energy_calculator(value):
    cleaned_values = re.sub(r"[^0-9.\-]", "", value)
    # print(float(cleaned_values))
    try:
        return float(cleaned_values)
    except ValueError:
        return None

for m, v in zip(masses, velocities):
    Mass = energy_calculator(m)
    Velocity = energy_calculator(v)
    # print(m)
    # print(Velocity)
    
    if Mass is not None and Velocity is not None and Velocity != 0:
        ke = 0.5 * Mass * Velocity ** 2
        print(f"Mass-> {Mass} & Velocity-> {Velocity}m/s gives Kinetic Energy: {int(ke)}J")
    else:
        print(f"Skipping invalid data {Mass}kg, {Velocity}m/s")

