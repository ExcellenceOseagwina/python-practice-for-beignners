"""For-loop exercises using divisibility and conditional logic."""

# These examples repeat with for loops and make choices with if/elif/else.
# Python checks each choice from top to bottom and runs the first true one.

# Exercise 8: Divisibility Checker (FizzBuzz)
# Check every number from 1 to 50.
# Check for multiples of both 3 and 5 first. These numbers also match each
# separate check, so the combined case must come first.
for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Exercise 9: Number Classification
# Classify each number from 1 to 30 as Small (1-10), Medium (11-20),
# or Large (21-30).
# Because the ranges are consecutive, the final else means 21 through 30.
for number in range(1, 31):
    if number <= 10:
        print(f"{number} is Small")
    elif number <= 20:
        print(f"{number} is Medium")
    else:
        print(f"{number} is Large")

# Exercise 10: Multiples of Different Numbers
# Check every number from 1 to 100.
# Check numbers that divide evenly by both 2 and 3 first, then check each one.
# % gives the remainder; a remainder of 0 means it divides evenly.
for number in range(1, 101):
    if number % 2 == 0 and number % 3 == 0:
        print(f"{number} is a multiple of 2 and 3")
    elif number % 2 == 0:
        print(f"{number} is a multiple of 2")
    elif number % 3 == 0:
        print(f"{number} is a multiple of 3")
    else:
        print(number)

# Exercise 16: Nested If Statements
# Classify numbers from 1 to 50 as Odd, Even and divisible by 4, or
# Even but not divisible by 4.
# The second if runs only for even numbers. It checks whether the number also
# divides evenly by 4.
for number in range(1, 51):
    if number % 2 == 0:
        if number % 4 == 0:
            print("Even and divisible by 4")
        else:
            print("Even but not divisible by 4")
    else:
        print("Odd")

# Exercise 17: Nested Conditions with Different Ranges
# For 1-50, print Even or Odd. For 51-100, check divisibility by 5.
# First choose the rule for numbers up to 50. Numbers over 50 then get checked
# to see if they divide evenly by 5.
for number in range(1, 101):
    if number <= 50:
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")
    elif number % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")

# Exercise 18: Compound Conditions (and / or)
# Check numbers from 1 to 100 for divisibility by 2 and/or 3.
# `and` means both checks must be true. `or` means at least one must be true.
# Check for both first so those numbers get the more specific message.
for number in range(1, 101):
    if number % 2 == 0 and number % 3 == 0:
        print("Divisible by both 2 and 3")
    elif number % 2 == 0 or number % 3 == 0:
        print("Divisible by 2 or 3")
    else:
        print("Neither")

# Exercise 19: Nested and Compound Conditions
# For numbers 1-25, check divisibility by 5. For 26-50, check parity.
# Numbers over 25 are checked as even or odd. The others are checked for
# divisibility by 5. The order of the choices decides which check is used.
for number in range(1, 51):
    if number > 25:
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")
    elif number % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")
