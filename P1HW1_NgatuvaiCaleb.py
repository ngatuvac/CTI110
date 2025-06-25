# Caleb Ngatuvai
# 24 June 2025
# P1HW1
# Using math in Python in a Github Codespace

print()
print("-----Calculating Exponents-----")
print(" ")
print(" ")
print("Enter an integer as the base value:", end=" ")
base_value = int(input())
print("Enter an integer as the exponent:", end=" ")
exponent = int(input())
answer = pow(base_value, exponent)
print()
print()
print(base_value, "raised to the power of", exponent, "is", answer)

print()
print()
print("-----Addition and Subtraction-----")
print()
print()
print("Enter a starting integer:", end=" ")
num1 = int(input())
print("Enter an integer to add:", end=" ")
num2 = int(input())
print("Enter an integer to subtract:", end=" ")
num3 = int(input())
answer2 = num1 + num2 - num3
print()
print()
print(num1, "+", num2, "-", num3, "is equal to", answer2)