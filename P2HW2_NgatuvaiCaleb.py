# Caleb Ngatuvai
# 28 June 2025
# P2HW2
# Work with lists

#value of each element is defined by user input
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))
print()

#create list named "module_grades" that contains the six elements defined above
module_grades = [mod1, mod2, mod3, mod4, mod5, mod6]

#create variables to hold requested data
low_grade = min(module_grades)
hi_grade = max(module_grades)
sum_grades = sum(module_grades)
grade_avg = sum_grades/len(module_grades)#sum of all the grades divided by the number of elements in the list

#print results
print("----------Results----------")
print(f"Lowest Grade: \t{low_grade:.1f}")
print(f"Highest Grade: \t{hi_grade:.1f}")
print(f"Sum of Grades: \t{sum_grades:.1f}")
print(f"Average: \t{grade_avg:.2f}")
print("--------------------------------------")

#print(module_grades) #(remove "#" from in front of print to check list's element values)
