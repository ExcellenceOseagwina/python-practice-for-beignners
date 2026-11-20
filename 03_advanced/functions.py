# FUNCTIONS
# A function is a named group of instructions. It lets you write steps once
# and run them whenever you need them.
# The examples below are comments. Remove the # marks from one example to run it.

# ======== Defining and calling a function ========
# def starts a function definition. The indented print line is its body.
# Defining a function saves the steps; calling greet() runs those steps.
# def greet():
#     print("Hello World!")

# Calling greet() runs the function. Each call prints the greeting again.
# greet()
# print("New Session")
# greet()
# print("Another Session")

# ======== A function with an input value ========
# The name inside the parentheses is a parameter. It receives a value each
# time the function is called. Here, even is the number the function checks.
# def is_even(even):
#     # % gives the remainder. Even numbers have no remainder after division by 2.
#     if even % 2 == 0:
#         print(f"{even} is even")
#     else:
#         print(f"{even} is odd")

# These loops call is_even() with many different numbers. Each supplied number
# is an argument, and it becomes the value of the even parameter for that call.
# for i in range(1, 10):
#     is_even(i)
# for i in range(100, 250):
#     is_even(i)

# ====== Returning a value ========
# return sends a value back to the place that called the function. The caller
# can save that value in a variable or use it in another calculation.
# def function_name():
#     return 100

# This call gets 100 back, then stores it in number.
# number = function_name()


# CHALLENGE 1: Make a greeting function
# Define a function that prints a greeting, then call it to see the result.
# Create a function that needs to greet someone.

# def greet():
#       print("Hello, Excellence!")
# greet()

# CHALLENGE 2: Make a goodbye function
# A function can contain any instructions. Call this one twice to print goodbye
# two times.
# Create a function that say's goodbye.

# def say_goodbye():
#     print("Goodbye!")
# say_goodbye()
# say_goodbye()

# CHALLENGE 3: Introduce yourself twice
# Put both print instructions in the function body. Calling the function twice
# repeats both lines.
# Write a Python program that lets to introduce yourself, not just once, but twice.

# What your program should do
# Define a function called introduce.
# Inside the function, print these two lines, one after the other:
# My name is Python Robot.
# I am learning functions!
# Call the function two times so the introduction appears twice.

# Output

# My name is Python Robot.
# I am learning functions!
# My name is Python Robot.
# I am learning functions!

# def introduce():
#     print("My name is Python Excellence")
#     print("I am learning functions!")

# introduce()
# introduce()
# introduce()

# ======== Parameters and arguments ========
# A parameter is the name in a function definition. An argument is the actual
# value you give that parameter when calling the function.
# CHALLENGE 4: Greet a person by name
# Use a name parameter so the function can greet different people.

# Your task:
# Create a Python function named greet that:
# 1. Accepts one parameter called name.
# 2. Prints Hello, followed by the person's name.
# 3. Call the function with the any argument.
# Expected output:
# Hello, Excellence

# def greet(name):
#     print("Hello,", name)

# greet("Excellence")

# CHALLENGE 5: Try different names
# Call the same function with a different argument each time. The function code
# stays the same, while the name in the message changes.
# Create a function named introduce that:
# 1. Accepts one parameter called name.
# 2. Prints My name is followed by the person's name.
# 3. Call the function three times using these arguments:
#    - "Excellence"
#    - "David"
#    - "Sarah"

# Output:
# My name is Excellence
# My name is David
# My name is Sarah

# def intro(name):
#     print("My name is", name)

# intro("Excellence")
# intro("David")
# intro("Sarah")

# CHALLENGE 6: Welcome students
# The student_name parameter receives each name supplied by the calls below.

# Create a function named student_info that:
# 1. Accepts one parameter called student.
# 2. Prints Welcome to Python, followed by the student's name.
# 3. Calls the function twice using these arguments:
#    - "Excellence"
#    - "Michael"
# Expected output:
# Welcome to Python, Excellence
# Welcome to Python, Michael

# def student_info(student_name):
#     print("Welcome to Python,", student_name)

# student_info("Excellence")
# student_info("Michael")

# CHALLENGE 7: Use more than one parameter
# A function can have several parameters. Give one matching argument for each
# parameter when you call it, in the same order.
# Create a Python function named student_info that accepts three parameters:
# 1. name
# 2. age
# 3. course
# Inside the function, use print() to display:
# - The student's name.
# - The student's age.
# - The student's course.

# Then call the function with these arguments:
# - Name: "Excellence"
# - Age: 100
# - Course: "Cyber Security"

# Output
# Your program should produce:
# Student Name: Excellence
# Student Age: 100
# Student Course: Cyber Security

# def student_info(name, age, course):
#     print(f'''
# Student Name: {name}
# Student Age: {age}
# Student Course: {course}
#           ''')
# student_info("Excellence", 100, "Cyber Security")


# CHALLENGE 8: Add a sequence of numbers
# This function should add every whole number from 1 through n. The loop uses
# n + 1 because range() stops before its ending value.
# Write a function called sigma

# What you need to do:

# Create a function named sigma that takes one number (called n) as input.What the function should do:

# Add up all the whole numbers from 1 all the way to n (including both 1 and n), and return that total.Example:

# If someone calls sigma(5), your function should return 15

# because: 1 + 2 + 3 + 4 + 5 = 15

# int() changes the text from input() into a whole number for the function.
# get_number = int(input("Enter number: "))

# n is the parameter: it receives the last number to add. total keeps the
# running sum, and return sends the finished sum back to the caller.
# def sigma(n):
#     total = 0
#     for i in range(1, n + 1):
#         total+=i
#     return total # print(total)  ----> since you are getting input from user

# Call the function with the number entered above. Use print() to show the
# returned answer on the screen.
# print(sigma(get_number))

# because: 1 + 2 + 3 + 4 + 5 = 15

# CHALLENGE 9:
# Write a Python function called track_volunteer_hours that calculates the total number of volunteer hours after a health campaign.

# The function should accept two parameters:
# - initial_hours: An integer representing the volunteer's previously recorded hours.
# - additional_hours: An integer representing the new hours contributed during the health campaign.
# Add the additional hours to the initial hours and return the updated total.

# initial_hours_data = int(input("Enter Number: "))
# additional_hours_data = int(input("Enter Number: "))

# def track_volunteer_hours(initial_hours, additional_hours):
#    
#     total = initial_hours + additional_hours
#     return total   # print(total) 
# track_volunteer_hours(initial_hours_data, additional_hours_data)

# CHALLENGE 10:
# Create a Python function named generate_login_string that accepts two parameters: username and day_of_week.

# The function should combine the employee's username and the current day of the week to generate a login string.

# Requirements:
# 1. The function must be named generate_login_string.
# 2. It must accept two parameters:
#    - username (string): The employee's username.
#    - day_of_week (string): The current day of the week (e.g., "Monday").

# get_username = str(input("Enter Username: "))
# get_day_of_week = str(input("Enter day of the week: "))

# def generate_login_string(username, day_of_week):
#     
#     login = username + " " + day_of_week
#     return login # print(login)
    
# generate_login_string(get_username, get_day_of_week)

# CHALLENGE 11:
# You are given two numbers, num1 and num2, as input.

# Your task is to multiply these two numbers, calculate their product, and store the result in a variable named product.

# What value should be stored in product after multiplying num1 by num2?

# num1 = int(input()) 
# num2 = int(input()) 
# product = 0

# def get_product(product_one, product_two):
#     product = product_one * product_two
#     print("product =", product) 
# get_product(num1, num2)

# Challenge 12 — Greeting Function

# Objective: Create a function that returns a person's name as a greeting.
# Instructions
# Write a Python function called greet that:
# 1. Accepts one parameter called name.
# 2. Uses return to send back the greeting "Hello, " followed by the person's name.
# 3. Calls the function with the argument "Excellence".
# 4. Stores the returned value in a variable called message.
# 5. Uses print() to display the value stored in message.

# def greet(name):
#     return "Hello, " + name

# message = greet("Excellence")
# print(message)

# Challenge 13 — Calculator Function

# Objective: Create a function that accepts two numbers, adds them together, and returns the result.
# Instructions
# Write a Python function called add_numbers that:
# 1. Accepts two parameters: a and b.
# 2. Uses return to send back the sum of both parameters.
# 3. Calls the function with the arguments 15 and 25.
# 4. Stores the returned value in a variable called result.
# 5. Displays the result using print().

# Output
# 40

# def add_numbers(a, b):
#     return a + b
# total = add_numbers(15, 25)
# print(total)    

# Challenge 14 — Product Information Calculator

# Objective: Create a function that calculates the total cost of purchasing multiple units of a product and returns the calculated value.
# Instructions
# Write a Python function called calculate_total that:
# 1. Accepts two parameters: price and quantity.
# 2. Uses return to calculate and send back the total cost (price × quantity).
# 3. Calls the function with:
#    - price = 2500
#    - quantity = 4
# 4. Stores the returned value in a variable called total_cost.
# 5. Displays the result using print().

# Output
# 10000

# def calculate_total(price, quantity):
#     return price * quantity

# total_cost = calculate_total(2500, 4)
# print(total_cost)

# ----------------Default Parameters, Keyword Arguments and their rules-------------------
# Challenge 15 — Default Greeting Function

# Objective
# Create a Python function named greet() that uses a default parameter.
# Requirements
# 1. Define a function named greet.
# 2. Give it one parameter named name.
# 3. Set the default value of name to "Excellence".
# 4. Inside the function, print a greeting using the person's name.
# 5. Call the function twice:
#    - First, without providing an argument.
#    - Second, providing "David" as the argument.
# Expected output
# Hello, Excellence!
# Hello, David!

# def greet(name="Excellence"):
#     return 'Hello, ' + name + "!"
# print(greet())
# print(greet("David"))

# Challenge 16: Student Information Function

# Objective
# Create a function named student_info() that uses multiple default parameters.
# Requirements
# 1. Define a function named student_info.
# 2. Give it three parameters:
#    - name with default value "Excellence".
#    - age with default value 22.
#    - country with default value "Nigeria".
# 3. The function must return a sentence containing the student's name, age, and country.
# 4. Call the function three times:
#    - Without providing any arguments.
#    - Providing only "David" as the argument.
#    - Providing "Michael", 25, and "Ghana" as arguments.
# Output
# My name is Excellence, I am 28 years old, and I live in Nigeria.
# My name is David, I am 28 years old, and I live in Nigeria.
# My name is Michael, I am 25 years old, and I live in Ghana.

# def student_info(name="Excellence", age=28, country="Nigeria"):
#     return f"My name is {name}, I am {age} years old, and I live in {country}."

# print(student_info())
# print(student_info(name="David"))
# print(student_info(name="Michael", age=25, country="Ghana"))

# Challenge 17: Product Price Calculator

# Objective
# Build a product price calculator using multiple default parameters.
# Requirements
# Create a function named calculate_price() with these parameters:
# Parameter	Default value
# price	Required — no default
# quantity	1
# discount	0

# Your function must:
# 1. Multiply price by quantity.
# 2. Subtract discount from the total.
# 3. Return the final price.
# 4. Call the function three times:
#    - calculate_price(5000)
#    - calculate_price(5000, 3)
#    - calculate_price(5000, 3, 2000)
   
# Output
# 5000
# 15000
# 13000

# This is the first live function in this file, so running the file demonstrates
# default parameter values. `price` is required; if omitted, Python reports an
# error. `quantity` and `discount` are optional because they have defaults.
def calculate_price(price, quantity=1, discount=0):
    # Multiply the price of one item by the number of items bought.
    total = price * quantity
    # Reduce the amount due by the discount, which is a fixed amount here.
    total -= discount
    # return sends the answer back to the caller; it does not display it.
    return total
# These calls use the default values, then override quantity, then override
# both optional values. print() displays each answer returned by the function.
print(calculate_price(5000))
print(calculate_price(5000, 3))
print(calculate_price(5000, 3, 2000))

# -----------------FizzBuzz----------------------
# FizzBuzz is a classic programming exercise used to practice loops, conditional statements, and divisibility in Python.

# The task is to write a Python program that iterates through numbers from 1 up to a specified limit and follows these rules:
# 1. If a number is divisible by 3, output "Fizz".
# 2. If a number is divisible by 7, output "Buzz".
# 3. If a number is divisible by both 3 and 7, output "FizzBuzz".
# 4. Otherwise, output the number itself.

# Your First Task:

# Before implementing the FizzBuzz logic, simply write a Python program that displays the following welcome message:

# Output:
# Welcome to FizzBuzz!
# print('Welcome to FizzBuzz!')

# Second Task
# Create a Python function named fizzbuzz that accepts one integer (int) as an argument and checks whether the number is divisible by 3, 7, or both.

# Your function must follow these rules:
# 1. If the number is divisible by 3, return "Fizz".
# 2. If the number is divisible by 7, return "Buzz".
# 3. If the number is divisible by both 3 and 7, return "FizzBuzz".
# 4. If none of these conditions are met, return the original number converted into a string (str).
# Additional Requirements:

# After defining your function:
# 1. Get input from the user using input().
# 2. Convert the input into an integer using int().
# 3. Call the fizzbuzz() function, passing the input number as its argument.
# 4. Print the function's returned value using print().

# print('Welcome to FizzBuzz!')
# get_number = int(input())

# def fizzbuzz(num):
#     if num % 3 == 0 and num % 7 == 0:
#         return "FizzBuzz"
#     if num % 3 == 0:
#         return "Fizz"
#     if num % 7 == 0:
#         return "Buzz"
#     else:
#         return f"{num}"

# fizz_buzz = fizzbuzz(get_number)
# print(fizz_buzz)

# Third Task
# Extend your existing FizzBuzz program by introducing a loop that iterates through numbers starting from 1 up to the number entered by the user.

# For each number in the loop, call your previously created fizzbuzz() function to determine the appropriate FizzBuzz result and display it.

# Requirements:
# 1. Get a number from the user.
# 2. Convert the input into an integer using int().
# 3. Use a for loop to iterate through numbers from 1 up to and including the user's input.
# 4. For each number, call the fizzbuzz() function.
# 5. Print the result returned by the function.
# Example:

# For an input of 7, the expected output is:
# Welcome to FizzBuzz!
# 1
# 2
# Fizz
# 4
# 5
# Fizz
# Buzz


# print('Welcome to FizzBuzz!')
# get_number = int(input())

# for i in range(1, get_number + 1):
#     def fizzbuzz(num):
#         if num % 3 == 0 and num % 7 == 0:
#             return "FizzBuzz"
#         if num % 3 == 0:
#             return "Fizz"
#         if num % 7 == 0:
#             return "Buzz"
#         else:
#             return f"{num}"

#     fizz_buzz = fizzbuzz(i)
#     print(fizz_buzz)

# Final Task
# Extend your existing FizzBuzz program by introducing a new condition called "Almost Fizz".

# The new rule states that any number containing the digit 3, but not divisible by either 3 or 7, should return "Almost Fizz".

# Your updated FizzBuzz function must follow these rules:
# 1. If the number is divisible by both 3 and 7, return "FizzBuzz".
# 2. If the number is divisible by 3, return "Fizz".
# 3. If the number is divisible by 7, return "Buzz".
# 4. If the number contains the digit 3, but is not divisible by 3 or 7, return "Almost Fizz".
# 5. If none of these conditions are met, return the original number as a string (str).
# Important Concepts:

# To check whether a number contains the digit 3, you must:
# - Convert the number into a string using str(num).
# - Use Python's membership operator in to check whether "3" exists inside that string.
# For example:
# "3" in str(num)

# This expression returns True if the digit 3 appears anywhere in the number.

# Additional Note:

# The in operator has different uses:
# - In a for loop, it helps iterate through a sequence.
# - With strings, it checks whether a particular character or substring exists inside another string.
# Your Goal: Practice Python conditional statements, the membership operator (in), string conversion (str()), and combining multiple conditions within a function.


# print('Welcome to FizzBuzz!')
# get_number = int(input())

# for i in range(1, get_number + 1):
#     def fizzbuzz(num):
#         if num % 3 == 0 and num % 7 == 0:
#             return "FizzBuzz"
#         if num % 3 == 0:
#             return "Fizz"
#         if num % 7 == 0:
#             return "Buzz"
#         if "3" in str(num):
#             return "Almost Fizz"
#         else:
#             return f"{num}"

#     fizz_buzz = fizzbuzz(i)
#     print(fizz_buzz)
    
    
#     # or
    
# print('Welcome to FizzBuzz!')

# def fizzbuzz(num):
#     if num % 3 == 0 and num % 7 == 0:
#         return "FizzBuzz"
#     if num % 3 == 0:
#         return "Fizz"
#     if num % 7 == 0:
#         return "Buzz"
#     if "3" in str(num):
#         return "Almost Fizz"
#     else:
#         return f"{num}"

# get_number = int(input())

# for i in range(1, get_number + 1):
#     fizz_buzz = fizzbuzz(i)
#     print(fizz_buzz)

# ---------------Arbitrary Arguments------------------
