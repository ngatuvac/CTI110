# Caleb Ngatuvai
# 4 July 2025
# P4HW2
# Enhanced version of P3HW2

#create variables to store user requested info
employee_name = input("\nEnter employee's name or \"Done\" to terminate: ")
num_employees = 0
total_overtime_paid = 0
total_regpay_paid = 0
total_gross_paid = 0

while employee_name != "Done":
    hours_worked = float(input(f"\nHow many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    overtime_rate = pay_rate * 1.5

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
    else:
        overtime_hours = 0
    
    overtime_pay = overtime_hours * overtime_rate

    if hours_worked <= 40:
        pay = pay_rate * hours_worked

    else:
        pay = (hours_worked - overtime_hours) * pay_rate


    #pay calculation
    if hours_worked <= 40:
        gross_pay = hours_worked * pay_rate

    else:
        gross_pay = (40 * pay_rate) + (overtime_hours * overtime_rate)

    #print results
    print("----------------------------------")
    print(f"Employee name:\t {employee_name}")
    print()
    print("Hours worked     Pay Rate     OverTime     OverTime Pay     RegHour Pay     Gross Pay")
    print("-------------------------------------------------------------------------------------------")
    print(f"{hours_worked:<16.1f} {pay_rate:<12.1f} {overtime_hours:<12.1f} ${overtime_pay:<15.2f} ${pay:<14.2f} ${gross_pay:<15.2f}")
    print()

    #update variables
    num_employees += 1
    total_overtime_paid += overtime_pay
    total_regpay_paid += pay
    total_gross_paid += gross_pay

    employee_name = input("Enter employee's name or \"Done\" to terminate: ")

print(f"\nTotal number of employees entered: {num_employees}")
print(f"Total amount paid for overtime: ${total_overtime_paid:.2f}")
print(f"Total amount paid for regular hours: ${total_regpay_paid:.2f}")
print(f"Total amount paid in gross: ${total_gross_paid:.2f}")

'''
Added a little more to P3HW2.  Program uses a while loop to collect employee name and hours worked.  To exit the loop, user enters "Done"
'''
