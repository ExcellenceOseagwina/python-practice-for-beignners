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
