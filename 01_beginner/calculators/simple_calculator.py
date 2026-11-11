# LESSON: Input, numeric types, and branching
# input() gives us text. float() changes that text into a number, including
# numbers with decimals. The user must enter a valid number for this example.

# Variables to store the numbers
number1 = float(input("Enter Number: "))

# Collect the operation
operation = input("Choose an operation (+, -, *, /): ")

number2 = float(input("Enter Number: "))
# None means “no value yet.” One of the choices below replaces it with an
# answer or an error message.
result = None

# if/elif/else chooses what to do. == checks whether two values are equal.
if operation == "+":
    result = number1 + number2

# Subtraction
elif operation == "-":
    result = number1 - number2

# For Division   
elif operation == "/":
    # A number cannot be divided by zero. Check for zero first so we can show
    # a helpful message instead of letting the program stop with an error.
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
    
# An f-string puts the value of result into the message inside the braces.
print(f"Result: {result}")
