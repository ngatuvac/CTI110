#Caleb Ngatuvai
#27 June 2025
#P2HW1
#Edit and enhance an existing program (Original is P1HW2)

#changed original programs int inputs to float
print("This program calculates and displays travel expenses")
print(" ")
print("Enter Budget:", end=" $")
budget = float(input())
print(" ")

print("Enter your travel destination:", end=" ")
dest = input()
print(" ")

print("How much do you think you will spend on gas?", end=" $")
gas = float(input())
print(" ")

print("Approximately, how much will you spend on accomodation/hotel?", end=" $")
hotel = float(input())
print(" ")

print("Last, how much do you need for food?", end=" $")
food = float(input())
print (" ")

tot_exp = gas + hotel + food

rem_budget = budget - tot_exp

#altered print functions with variables in original program from print() to print(f)
print("--------------Travel Expenses--------------")
print(f"Location: \t\t{dest}") #using tabs (\t) to line up the columns
print(f"Initial Budget: \t${budget:.2f}")
print(f"Fuel: \t\t\t${gas:.2f}")
print(f"Accomodation: \t\t${hotel:.2f}")
print(f"Food: \t\t\t${food:.2f}")
print("-------------------------------------------")
print(" ")
print(f"Remaining Balance: \t${rem_budget:.2f}")
