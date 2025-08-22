# The radius of a circle is 30 meters.
# Calculate the area of a circle 
# Calculate the circumference of a circle 
# Take radius as user input and calculate the area.

#steps
# take the input radius
# funtion that calculates area given int() input 
# pass it into the area calcultor function
# print result
#added features
#running until input is valid 
#pow() function takes two arguments: the base and the exponent
# \u00B2 for power 2(unicode superscript for 2) 

 
def area_calculator(radius):
    pi = 3.14
    area = pi * pow(radius, 2)
    return area

def circumference_calculator(radius):
    pi = 3.14
    circumference = pi * radius * 2
    return circumference

while True: #function runs endlessly until input is valid 
    try:
        radius_value = float(input("Enter radius: "))
        area = area_calculator(radius_value)
        circumference = circumference_calculator(radius_value)
        print(f"The area is {area:.2f}m\u00B2")
        print(f"The circumference is {circumference:.2f}m")
        break

    except ValueError:
        print("Please enter valid number")
    