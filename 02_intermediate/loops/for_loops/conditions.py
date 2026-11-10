"""For-loop exercises using divisibility and conditional logic."""

# Exercise 8: Divisibility Checker (FizzBuzz)
# Check every number from 1 to 50.
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
for number in range(1, 31):
    if number <= 10:
        print(f"{number} is Small")
    elif number <= 20:
        print(f"{number} is Medium")
    else:
        print(f"{number} is Large")

# Exercise 10: Multiples of Different Numbers
# Check every number from 1 to 100.
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
for number in range(1, 101):
    if number % 2 == 0 and number % 3 == 0:
        print("Divisible by both 2 and 3")
    elif number % 2 == 0 or number % 3 == 0:
        print("Divisible by 2 or 3")
    else:
        print("Neither")

# Exercise 19: Nested and Compound Conditions
# For numbers 1-25, check divisibility by 5. For 26-50, check parity.
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
