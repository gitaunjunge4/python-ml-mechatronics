#Use the built-in input function to get first name, 
# last name,
#  country and 
# age from a user and 
# store the value to their corresponding variable names


def reg_system():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    country = input("Country of origin: ")
    age = input("Age: ")
    print(f"Hi {first_name + " " + last_name}from {country}. You are {age}yrs old.")

reg_system()