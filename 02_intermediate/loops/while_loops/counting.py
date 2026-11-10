"""While-loop exercises for counting."""

# Exercise 1: Print Numbers
# Print every integer from 1 to 20, inclusive.
# number = 1
# while number <= 20:
#     print(number)
#     number += 1

# Exercise 2: Even Numbers
# Print all even numbers between 1 and 50, inclusive.
# even = 2
# while even <= 50:
#     print(even)
#     even += 2

# Exercise 3 of 25 – Countdown
# Write a Python program that uses a while loop to print numbers from 30 down to 1.

# count = 30

# while count >= 1:
#     print(count)
#     count -= 1

# Exercise 4 of 25 – Sum of Numbers

# Write a Python program that calculates the sum of all integers from 1 to 100, inclusive, using a while loop.

# total = 0
# count = 1


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

# while count <= 12:
#     result = number * count
#     print(f"{number} x {count} = {result}")
#     count += 1

# Exercise 6 of 25 – Divisible by 3

# Task: Write a Python program that prints all numbers between 1 and 100 that are divisible by 3.

# numbers = 1

# while numbers <= 100:
#     if numbers % 3 == 0:
#         print(numbers)
#     numbers+=1


# Exercise 7 of 25 – Count Even Numbers

# Write a Python program that counts how many even numbers exist between 1 and 100.
# count = 0
# even = 1

# while even <= 100:
#     if even % 2 ==0:
#         count+=1
#     even+=1
# print(count)

# Exercise 8 of 25 – Positive Number Validator

# Now we're moving into a slightly different application of while loops.

# Task: Write a Python program that continuously asks the user to enter a number until they enter a positive number.

# positive_number = int(input("Enter positive number: "))

# while positive_number <= 0:
#     print("Invalid number. Try again.")
#     positive_number = int(input("Enter positive number: "))

# Exercise 9 of 25 – Sum of Odd Numbers

# Let's combine two concepts you've already learned: conditional checking and accumulators.

# Task: Write a Python program that calculates the sum of all odd numbers between 1 and 50, inclusive.

# odd = 1
# total = 0

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