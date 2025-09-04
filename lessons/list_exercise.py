# Asks the user to enter 7 daily temperature readings (one for each day of the week).
# Stores them in a list.
# Prints out:
# The list of temperatures entered
# The average temperature (use statistics.mean)
# The minimum and maximum temperatures (with min() and max())
# The median temperature (with statistics.median)
# Prints a sorted version of the list (from coldest to hottest).

# Hints
# Use a for loop with range(7) to get input 7 times.
# Convert user input with float() because inputs come as strings.
# Import the statistics module.

# STEPS
# import statistics
# create lst var
# ask user for input
# print that lst
# calculate: average temperature, minimum and maximum temperatures,median temperature,  sorted version of the list

#to validate input it needs a helper function
#function takes prompt as input and evaliuates if it is valid 


import statistics

# main function
def temp_readings():
    temp_list = []

    for x in range(7):
        day_temp = val_prompt(f'Enter day {x+1} temperature: ')
        # print(day_temp)
        temp_list.append(day_temp)    
    print(f"Temp list: {temp_list}")

    avg_temp = statistics.mean(temp_list)
    print(f"Average temp: {avg_temp:.2f}°C")
    min_temp = min(temp_list)
    max_temp = max(temp_list)
    print(f"Min temp: {min_temp}°C, Max temp:{max_temp}°C")
    median_temp = statistics.median(temp_list)
    print(f"Median temp: {median_temp}°C")
    sorted_temp_list = sorted(temp_list)
    print(f"Sorted temp list: {sorted_temp_list}")


# helper function
def val_prompt(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value 
        
        except ValueError:
            print("Please enter valid input.")

temp_readings()




    

