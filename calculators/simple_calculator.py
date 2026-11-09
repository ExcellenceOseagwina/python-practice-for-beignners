# Basic Calculator

# Variables to store the numbers
number1 = float(input("Enter Number: "))

# Collect the operation
operation = input("Choose an operation (+, -, *, /): ")

number2 = float(input("Enter Number: "))
result = None

# Addition
if operation == "+":
    result = number1 + number2

# Subtraction
elif operation == "-":
    result = number1 - number2

# For Division   
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
    # For ZeroDivision
    else:
        result = "Error: Cannot divide by zero." 

# Multiplication
elif operation == "*":
    result = number1 * number2

# For Unsupported Operator  
else:
    result = f"Error: Unsupported operator '{operation}'."
    
print(f"Result: {result}")