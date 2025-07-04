# Caleb Ngatuvai
# 4 July 2025
# P4LAB2
# Using a for and while loop to create multiplication tables

#create list which holds integers 1 to 12
nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#create variable to hold yes or no and initialize with yes to start the loop
user_decision = "yes"

while user_decision == "yes":
    
    num_entered = int(input("\nEnter an integer: "))

    if num_entered < 0:
        print("\nThis program cannot accept negative values.\n")
        
    else:
        for nums in nums_list:
            print(f"{num_entered} * {nums} = {num_entered * nums}")

#give the user a chance to exit the while loop.  yes continues the loop.  no exits and completes the program.
    user_decision = input("\nWould you like to run the program again (Type yes or  no)? ")
print("\nThanks for playing! Happy 4th of July!\n")

