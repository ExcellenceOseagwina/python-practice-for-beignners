# LESSON: Personal Profile Generator
# This exercise demonstrates variables, data types, arithmetic-free output,
# and converting numbers to text when joining them with the + operator.

# Task: Create a Python program that displays your personal profile.

# Your program should contain variables for:

# Name: John Doe
# Age: 29
# Country: Nigeria
# State: Edo
# University: Wellspring University
# Course: Cyber Security
# GPA: 4.25
# Height: 1.64m
# Favorite Language: Python

# Each assignment binds a name to a value. Quoted values are strings, age is
# an integer, and GPA/height are floating-point numbers (numbers with decimals).
name = 'Excellence Oseagwina'
age = 29
country = 'Nigeria'
state = 'Edo State'
university = 'Wellspring University'
course = 'Cyber Security'
g_p_a = 4.25
height = 1.64
favorite_lan = 'Python'

# String concatenation combines pieces into one string. str() converts numeric
# values because Python cannot concatenate a number directly to a string.
print('Name: ' + name)
print("Age: " + str(age))
print('Country: ' + country)
print('State: ' + state)
print("University: " + university)
print('Course: ' + course)
print("G.P.A: " + str(g_p_a))
print("Height: " + str(height))
print("Favorite Language: " + favorite_lan)



