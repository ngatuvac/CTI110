# Caleb Ngatuvai
# 30 June 2025
# P3HW2
# Create an employee paysheet

#create variables and define them with user input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
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
    

