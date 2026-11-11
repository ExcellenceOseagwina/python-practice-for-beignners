"""While-loop exercises for counting."""

# A while loop repeats as long as its check is True. Give the counter a starting
# value and change it in the loop so the loop can stop. These exercises are
# comments; remove the # marks from one answer to try it.

# Exercise 1: Print Numbers
# Print every integer from 1 to 20, inclusive.
# number = 1
# Start at 1. Add 1 after each print. The loop stops when number reaches 21.
# while number <= 20:
#     print(number)
#     number += 1

# Exercise 2: Even Numbers
# Print all even numbers between 1 and 50, inclusive.
# even = 2
# Start at 2 and add 2 each time to get the next even number.
# while even <= 50:
#     print(even)
#     even += 2

# Exercise 3 of 25 – Countdown
# Write a Python program that uses a while loop to print numbers from 30 down to 1.

# count = 30
# Subtract 1 each time to count down to 1.

# while count >= 1:
#     print(count)
#     count -= 1

# Exercise 4 of 25 – Sum of Numbers

# Write a Python program that calculates the sum of all integers from 1 to 100, inclusive, using a while loop.

# total = 0
# count = 1
# Add count to total each time, then increase count. This adds each number once.


# while count <= 100:
#     total += count
#     count+=1
# print(total)

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

# number = int(input("Enter Number: "))
# count = 1
# Ask for a number, then multiply it by count from 1 through 12.

# while count <= 12:
#     result = number * count
#     print(f"{number} x {count} = {result}")
#     count += 1

# Exercise 6 of 25 – Divisible by 3

# Task: Write a Python program that prints all numbers between 1 and 100 that are divisible by 3.

# numbers = 1
# % gives the remainder after division. A remainder of 0 means it divides evenly.

# while numbers <= 100:
#     if numbers % 3 == 0:
#         print(numbers)
#     numbers+=1


# Exercise 7 of 25 – Count Even Numbers

# Write a Python program that counts how many even numbers exist between 1 and 100.
# count = 0
# even = 1
# Check each number. Add 1 to count when the number is even.

# while even <= 100:
#     if even % 2 ==0:
#         count+=1
#     even+=1
# print(count)

# Exercise 8 of 25 – Positive Number Validator

# Now we're moving into a slightly different application of while loops.

# Task: Write a Python program that continuously asks the user to enter a number until they enter a positive number.

# positive_number = int(input("Enter positive number: "))
# Ask again while the number is zero or less. A new answer may stop the loop.

# while positive_number <= 0:
#     print("Invalid number. Try again.")
#     positive_number = int(input("Enter positive number: "))

# Exercise 9 of 25 – Sum of Odd Numbers

# Let's combine two concepts you've already learned: conditional checking and accumulators.

# Task: Write a Python program that calculates the sum of all odd numbers between 1 and 50, inclusive.

# odd = 1
# total = 0
# Odd numbers have a remainder other than 0 when divided by 2. Add each one to
# total, then check the next number.

# while odd <= 50:
#     if odd % 2 != 0:
#         total += odd
#     odd += 1
# print(total)

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

# count = 1
# total = 0
# Repeat five times to collect five numbers. Divide their total by 5 to get the
# average.

# while count <= 5:
#     number = int(input("Enter number: "))
#     total += number
#     avg = total / 5
#     count+=1        
# print(f'''
# Total: {total}
# Average: {avg}
# ''')

# Exercise 11 of 25 — Stop a Loop at 13
# Write a Python program that:
# 1. Uses a while loop.
# 2. Prints numbers from 1 to 20.
# 3. Stops printing when the number reaches 13.
# 4. Uses break to terminate the loop.

# count = 1
# break stops a loop right away. This attempt stops before count reaches 13,
# so think about how to change the check to make break run.

# while count < 13:
#     print(count)
#     if count == 13:
#         break
#     count+=1

# Exercise 12 of 25 — Skip Multiples of 3
# Write a Python program that:
# 1. Uses a while loop.
# 2. Prints numbers from 1 to 30.
# 3. Skips every number divisible by 3.
# 4. Uses continue to skip those numbers.

# Initialize the candidate before the loop. This is the active solution below.
count = 1

while count <= 30:
    # If count divides evenly by 3, add 1 before continuing. Otherwise the same
    # number would repeat forever. continue skips the print below.
    if count % 3 == 0:
        count += 1
        continue

    # Print numbers that are not multiples of 3, then check the next number.
    print(count)
    count += 1
