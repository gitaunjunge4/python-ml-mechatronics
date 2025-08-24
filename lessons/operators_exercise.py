#Compute kinetic energy for a list of mass/velocity pairs

#steps
#create a function that maps thru the data and changes it to float & returns it 
#pass it thru a for loop to calculate the KE 
# KE= 0.5 * m * v**2 
#print to the terminal
#"Mass -> {mass} Velocity -> {velocity} KE ->{KE}"
#using re.sub(r[^0-9.\-], "", text)

import re

#data
masses = ["50kg", "70", "100 kg", "ten", "85.5kg"]
velocities = ["10m/s", "15", "20.0 m/s", "five", "0"]

