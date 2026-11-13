"""While-loop exercises for counting."""

# A while loop repeats as long as its check is True. Give the counter a starting
# value and change it in the loop so the loop can stop. Run this file to see each
# example; interactive exercises prompt for input.

# Exercise 1: Print Numbers
# Print every integer from 1 to 20, inclusive.
number = 1
# Start at 1. Add 1 after each print. The loop stops when number reaches 21.
while number <= 20:
    print(number)
    number += 1

# Exercise 2: Even Numbers
# Print all even numbers between 1 and 50, inclusive.
even = 2
# Start at 2 and add 2 each time to get the next even number.
while even <= 50:
    print(even)
    even += 2

# Exercise 3 of 25 – Countdown
# Write a Python program that uses a while loop to print numbers from 30 down to 1.

count = 30
# Subtract 1 each time to count down to 1.

while count >= 1:
    print(count)
    count -= 1

# Exercise 4 of 25 – Sum of Numbers

# Write a Python program that calculates the sum of all integers from 1 to 100, inclusive, using a while loop.

total = 0
count = 1
# Add count to total each time, then increase count. This adds each number once.


while count <= 100:
    total += count
    count += 1

print(total)

# Exercise 5 of 25 – Multiplication Table
# Now let's apply your understanding of counters and accumulators to a slightly different problem.
# Task: Ask the user to enter a number and print its multiplication table from 1 to 12.
# For example, if the user enters 5:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
# 5 x 11 = 55
# 5 x 12 = 60

number = int(input("Enter Number: "))
count = 1
# Ask for a number, then multiply it by count from 1 through 12.

while count <= 12:
    result = number * count
    print(f"{number} x {count} = {result}")
    count += 1

# Exercise 6 of 25 – Divisible by 3

# Task: Write a Python program that prints all numbers between 1 and 100 that are divisible by 3.

numbers = 1
# % gives the remainder after division. A remainder of 0 means it divides evenly.

while numbers <= 100:
    if numbers % 3 == 0:
        print(numbers)
    numbers += 1


# Exercise 7 of 25 – Count Even Numbers

# Write a Python program that counts how many even numbers exist between 1 and 100.
count = 0
even = 1
# Check each number. Add 1 to count when the number is even.

while even <= 100:
    if even % 2 == 0:
        count += 1
    even += 1
print(count)

# Exercise 8 of 25 – Positive Number Validator

# Now we're moving into a slightly different application of while loops.

# Task: Write a Python program that continuously asks the user to enter a number until they enter a positive number.

positive_number = int(input("Enter positive number: "))
# Ask again while the number is zero or less. A new answer may stop the loop.

while positive_number <= 0:
    print("Invalid number. Try again.")
    positive_number = int(input("Enter positive number: "))

# Exercise 9 of 25 – Sum of Odd Numbers

# Let's combine two concepts you've already learned: conditional checking and accumulators.

# Task: Write a Python program that calculates the sum of all odd numbers between 1 and 50, inclusive.

odd = 1
total = 0
# Odd numbers have a remainder other than 0 when divided by 2. Add each one to
# total, then check the next number.

while odd <= 50:
    if odd % 2 != 0:
        total += odd
    odd += 1
print(total)

# Exercise 10 of 25 — Calculate the Average
# Write a Python program that:
# 1. Asks the user to enter five numbers.
# 2. Adds all five numbers together.
# 3. Calculates their average.
# 4. Prints the final average.

# Enter number: 10
# Enter number: 20
# Enter number: 30
# Enter number: 40
# Enter number: 50

# Total: 150
# Average: 30.0

count = 1
total = 0
# Repeat five times to collect five numbers. Divide their total by 5 to get the
# average.

while count <= 5:
    number = int(input("Enter number: "))
    total += number
    avg = total / 5
    count+=1
print(f"Total: {total}")
print(f"Average: {avg}")

# Exercise 11 of 25 — Stop a Loop at 13
# Write a Python program that:
# 1. Uses a while loop.
# 2. Prints numbers from 1 to 20.
# 3. Stops printing when the number reaches 13.
# 4. Uses break to terminate the loop.

count = 1
# Check for 13 before printing. break exits the loop as soon as the counter
# reaches the stopping value.

while count <= 20:
    if count == 13:
        break
    print(count)
    count += 1

# Exercise 12 of 25 — Skip Multiples of 3
# Write a Python program that:
# 1. Uses a while loop.
# 2. Prints numbers from 1 to 30.
# 3. Skips every number divisible by 3.
# 4. Uses continue to skip those numbers.

# Initialize the candidate before the loop. This is the active solution below.
count = 1

while count <= 30:
    # Advance before continuing so the loop cannot repeat the same number.
    if count % 3 == 0:
        count += 1
        continue

    # Print numbers that are not multiples of 3, then check the next number.
    print(count)
    count += 1

# Exercise 13 of 25 — Stop When the User Enters 0
# Write a Python program that:
# 1. Uses a while loop.
# 2. Repeatedly asks the user to enter a number.
# 3. Continues accepting numbers until the user enters 0.
# 4. Uses break to terminate the loop when 0 is entered.

# Example interaction:

# Enter a number: 5
# Enter a number: 12
# Enter a number: 8
# Enter a number: 3
# Enter a number: 0

# Program terminated.

number = int(input("Enter Number: "))

while number != 0:
    number = int(input("Enter Number: "))
    if number == 0:
        print("Program terminated.")
        break

# Exercise 14 of 25 — Skip Even Numbers and Stop at 35
# Write a Python program that:
# 1. Uses a while loop.
# 2. Iterates through numbers 1–50.
# 3. Skips all even numbers using continue.
# 4. Stops when it reaches 35 using break.
# 5. Prints only odd numbers before 35.

count = 0

while count <= 50:
    count += 1

    if count == 35:
        break

    if count % 2 == 0:
        continue

    print(count)

# Exercise 15 of 25 — Sum Positive Numbers Until a Negative Number
# Write a Python program that:
# 1. Uses a while loop.
# 2. Repeatedly asks the user to enter a number.
# 3. Adds positive numbers to a running total.
# 4. Terminates when the user enters a negative number.
# 5. Uses break to terminate the loop.
# 6. Displays the final sum after the loop.

total = 0

while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break

    total += number
print(f"Sum of positive numbers: {total}")


# Exercise 16 of 25 — Print a 5 × 5 Asterisk Grid
# Now we're moving into nested loops!
# Write a Python program that prints five rows, with five asterisks (*) on each row.
# Expected output:

# *****
# *****
# *****
# *****
# *****

row = 1

while row <= 5:
    col = 1
    while col <= 5:
        col += 1
        print("*", end='')
    print()
    row += 1


# Exercise 17 of 25 — Print an Asterisk Triangle
# Write a Python program using nested while loops to print the following pattern:
# Output
# *
# **
# ***
# ****
# *****

row = 1

while row <= 5:
    col = 1
    while col <= row:
        col += 1
        print("*", end='')
    print()
    row += 1


# Exercise 18 of 25 — Multiplication Tables (1–5)
# Write a Python program using nested while loops to print the multiplication tables from 1 to 5.

# Output:
# Multiplication Table of 1
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# # 1 x 5 = 5

# Multiplication Table of 2
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10


number = 1

while number <= 5:
    multiplier = 1

    while multiplier <= 5:
        total = number * multiplier
        print(f"{number} x {multiplier} = {total}")
        multiplier += 1

    print()
    number += 1

# Exercise 19 of 25 — Print all pairs

# Write a Python program using nested while loops to print every possible pair of numbers from 1 to 5.

# Output:
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 2 1
# 2 2
# 2 3
# ...
# 5 3
# 5 4
# 5 5


x = 1


while x <= 5:
    y = 1
    while y <= 5:

        print(x, y)
        y += 1
    x += 1

# Exercise 20 of 25 — Numeric triangle pattern
# Nested while loops

# Write a Python program using nested while loops to produce this pattern:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

outer_loop = 1

while outer_loop <= 5:
    inner_loop = 1
    while inner_loop <= outer_loop:
        print(inner_loop, end=' ')
        inner_loop += 1
    print()
    outer_loop += 1


# Exercise 21 of 25 — Factorial using a while loop

# Write a Python program that calculates the factorial of a number using a while loop.

factorial = 1
number = int(input("Enter a number: "))
count = 1

while count <= number:
    factorial *= count
    count += 1

print(f"The factorial of {number} is {factorial}")


# Exercise 22 of 25 — Prime Number Checker
# While loops + Conditional statements
number = int(input("Enter a number: "))
count = 2
is_prime = True

if number <= 1:
    is_prime = False

else:
    while count < number:
        if number % count == 0:
            is_prime = False
            break

        count += 1

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# Exercise 23 of 25 — Find the Largest of 10 Numbers
# While loops + Conditional statements

# For this exercise, you'll write a program that accepts 10 numbers from the user and identifies the largest number.

count = 1
largest = None

while count <= 10:
    number = int(input(f"Enter number {count}: "))

    if largest is None:
        largest = number

    elif number > largest:
        largest = number

    count += 1

print(f"The largest number is {largest}.")

# Exercise 24 of 25 — Count the Digits of an Integer

# Objective
# Write a Python program that asks the user to enter an integer and counts how many digits it contains using a while loop.
# Example 1
# Enter a number: 58392

# The number of digits is 5.

number = abs(int(input("Enter a number: ")))
count = 0

if number == 0:
    count = 1

else:
    while number != 0:
        number //= 10
        count += 1

print(f"The number of digits is {count}.")

# Exercise 25 of 25 — Print All Prime Numbers from 1 to 100
# Objective
# Write a Python program that uses nested while loops to identify and print every prime number between 1 and 100.

count = 1

while count <= 100:
    is_prime = True
    divisor = 2

    if count <= 1:
        is_prime = False

    else:
        while divisor < count:
            if count % divisor == 0:
                is_prime = False
                break

            divisor += 1

    if is_prime:
        print(count)

    count += 1
