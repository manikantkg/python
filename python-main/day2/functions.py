# Quick Exercise:
# Write a program that:

# Creates a function calculate(a, b, operation="add")
# If operation is "add" → return a + b
# If operation is "subtract" → return a - b
# If operation is "multiply" → return a * b
# Call the function with different operations and print results


def Cal(a, b, operation = 'add'):
    if operation == "add":
        return a+b
    elif operation == "subtract":
        return a-b
    elif operation == "multiply":
        return a*b
    else:
        return "Mal operation"


print(Cal(2,3))
print(Cal(5,3, "subtract"))
print(Cal(5,4, "multiply"))
print(Cal(5,4, "div"))
