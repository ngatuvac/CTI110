# Caleb Ngatuvai
# 27 June 2025
# P2LAB2
# Creating a Dictionary

#create dictionary named cars
cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

#create variable to hold keys
keys = cars.keys()

#print the variable that holds the keys
print(keys)

#create a variable to hold user's choice, then prompt user to choose a car
car_of_choice = input("\nEnter a vehicle to see it's mpg: " )

#create variable mpg (miles per gallon) and display mpg for the vehicle chosen
mpg = cars[car_of_choice]
print(f"\nThe {car_of_choice} gets {mpg} mpg.")

#prompt user to enter estimate of miles the vehicle will be driven
estimated_miles = float(input(f"\nHow many miles will you drive the {car_of_choice}? "))

#calculate how many gallons of gas are needed to drive the estimated distance
gas_needed = estimated_miles / mpg

#print gallons of gas needed
print(f"\n{gas_needed:.2f} gallon(s) of gas are needed to drive the {car_of_choice} {estimated_miles} miles.")
