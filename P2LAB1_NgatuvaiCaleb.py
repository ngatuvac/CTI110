# Caleb Ngatuvai
# 27 June 2025
# P2LAB1
# Math for Circles

# import math module for use in calculations
import math

# define variables: radius is from input, everything else is calculated from radius

radius = float(input("What is the radius of the circle? "))
diameter = 2 * radius
circumference = math.pi * 2 * radius
area = math.pi * (radius ** 2)

#print calculations

print() #create new line
print(f"The diameter of the circle is {diameter:.1f}")
print()
print(f"The circumference of the circle is {circumference:.2f}")
print(f"\nThe area of the circle is {area:.3f}") #trying \n to create new line

