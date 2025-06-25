#Caleb Ngatuvai
#24 June 2025
#P1HW2
#Using math in a simple travel budget

print(" ")
print("Enter your travel budget:", end=" ")
budget = int(input())
print(" ")

print("Enter your travel destination:", end=" ")
dest = input()
print(" ")

print("How much will you spend on gas?", end=" ")
gas = int(input())
print(" ")

print("How much will you spend on hotels / accomodations?", end=" ")
hotel = int(input())
print(" ")

print("How much will spend on food?", end=" ")
food = int(input())
print (" ")

tot_exp = gas + hotel + food

rem_budget = budget - tot_exp

print("-----Travel Expenses-----")
print(" ")
print("Location:", dest)
print("Initial Budget:", budget)
print(" ")
print("Fuel:", gas)
print("Accomodation:", hotel)
print("Food:", food)
print(" ")
print("Remaining Balance:", rem_budget)
