# Caleb Ngatuvai
# 11 July 2025
# P5LAB
# Functions lab to disburse change


import random #used to generate random amount that customer must pay
import math #allows math functions to be used

#convert P3LAB into a function
def disburse_change(money):

    # convert money into an integer. Round rounds to nearest integer. Multiply by 100 to get rid of cents.  
    money = round(money * 100)

    #convert money into bills.  Remaining cents are saved in the variable money.
    dollar_bills = money // 100
    money = money - (dollar_bills * 100)

    #prints dollar output
    if dollar_bills > 0:
        if dollar_bills == 1:
            print(f"{dollar_bills} Dollar")
        else:
            print(f"{dollar_bills} Dollars")

    #divides cents into quarters if possible. Remainder saved in variable money.
    quarters = money // 25
    money = money - (quarters * 25)

    #prints quarter output
    if quarters > 0:
        if quarters == 1:
            print(f"{quarters} Quarter")
        else:
            print(f"{quarters} Quarters")

    #divides cents into dimes if possible. Remainder saved in variable money.
    dimes = money // 10
    money = money - (dimes * 10)

    #prints dimes output
    if dimes > 0:
        if dimes == 1:
            print(f"{dimes} Dime")
        else:
            print(f"{dimes} Dimes")

    #divides cents into nickels if possible. Remainder saved in variable money.
    nickels = money // 5
    money = money - (nickels * 5)

    #prints nickels output
    if nickels > 0:
        if nickels == 1:
            print(f"{nickels} Nickel")
        else:
            print(f"{nickels} Nickels")# I'll never have two nickels because they make a dime

    #only pennies remain. prints pennies output
    if money > 0:
        if money == 1:
            print(f"{money} Penny")
        else:
            print(f"{money} Pennies")        

   #print(money) #this line used in testing.  remove # from in front of print to verify money variable

#create main function to store program logic
def main():
    #customer is required to pay an amount that is randomly generated and output to screen
    customer_owes = round(random.uniform(0.10, 100.00), 2)#this line of code provided in the lab instructions
    print(f"You owe ${customer_owes:.2f}")

    #customer inputs how much cash they'll use to pay their bill
    customer_pays = float(input("How much cash will you put in the self-checkout? $"))

    #while loop keeps track of balance due if customer inputs less than the amount owed
    while customer_pays < customer_owes:
        money = math.fabs(customer_pays - customer_owes)
        print(f"The amount owed is ${customer_owes:.2f} \nYou paid ${customer_pays:.2f} \nRemaining balance due is ${money:.2f}")
        customer_owes = money
        customer_pays = float(input("\nHow much cash will you put in the self-checkout? $"))

    #store change due to customer in variable 'money'
    money = customer_pays - customer_owes
    print(f"Change is: ${money:.2f}")

    disburse_change(money)

main()


