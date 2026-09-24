# Student Name: Miguel Garcia
# Course Number: CMP 131
# Week Number: 4
# Lab Number: 2
# Assignment Title: Calculation
# Date: 09/23/26

first_number = int(input("Enter a numnber: "))
second_number = int(input("Enter another numnber: "))

addition_result = first_number + second_number
subtraction_result = first_number - second_number
multiplication_result = first_number * second_number
division_result = first_number / second_number
power_result = first_number ** second_number
average_result = (first_number + second_number) / 2

print()
print("---------------------------------")
print("           ADDITION")
print("---------------------------------")
print(f"The sum of {first_number} and {second_number} is: {addition_result}")
print()
print("--------------   -------------------")
print("          SUBTRACTION")
print("---------------------------------")
print(f"The difference of {first_number} and {second_number} is: {subtraction_result}")
print()
print("---------------------------------")
print("        Multiplication")
print("---------------------------------")
print(f"The product of {first_number} and {second_number} is: {multiplication_result}")
print()
print("---------------------------------")
print("           DIVISION")
print("---------------------------------")
print(f"The quotient of {first_number} and {second_number} is: {division_result:.2f}")
print()
print("---------------------------------")
print("            POWER")
print("---------------------------------")
print(f"The power of {first_number} and {second_number} is: {power_result}")
print()
print("---------------------------------")
print("           AVERAGE")
print("---------------------------------")
print(f"The average of {first_number} and {second_number} is: {average_result}")