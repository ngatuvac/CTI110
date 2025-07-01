# Caleb Ngatuvai
# 30 June 2025 (1 July 2025 EST)
# P3LAB
# Money lab that uses branching

# user inputs amount of money to be received as change
money = float(input("Enter the amount of money as a float: $"))

#save original user input
original_input = money

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

#print(money) #used in testing.  remove # from in front of print to verify money variable
