##################### For Loops ####################################

# Question 1: Print Numbers
# Write a Python program that prints every number from 1 to 20 (inclusive) using a for loop.

# for i in range(1, 21):
#     print(i)

# Question 2: Countdown
# Write a Python program that prints numbers from 20 down to 1.
# for i in range(20, 0, -1):
#     print(i)

# Question 3: Multiplication Table
# Write a Python program that prints the multiplication table of 7, from 1 to 12.
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# ...
# 7 x 12 = 84

# count = 0
# for i in range(1, 13):
#     if i > 0:
#         count += 1
#         i *= 7
#     print(f"7 x {count} = {i}")

#     # or

# for i in range(1, 13):
#     count = 7 * i                     # This version is easier
#     print(f"7 x {i} = {count}")


# Question 4: Even Numbers
# Write a Python program that prints all even numbers between 1 and 50 (inclusive).

# for even in range(1, 51):
#     if even % 2 == 0:
#         print(even)

# Question 5: Odd Numbers
# Write a Python program that prints all odd numbers between 1 and 50 (inclusive).
# for odd in range(1, 51):
#     if odd % 2 != 0:
#         print(odd)

# # or

# for odd in range(1, 51):
#     if odd % 2 == 1:
#         print(odd)

# Question 6: Even or Odd Classification
# Write a Python program that checks every number between 1 and 30 (inclusive).

# for certain_number in range(1, 31):
#     if certain_number % 2 == 0:
#         print(f"{certain_number} is an even number")
#     else:
#         print(f"{certain_number} is an odd number")

# Question 7: Positive, Negative, or Zero
# Write a Python program that checks every number from -10 to 10 (inclusive).

# for certain_number in range(-10, 11, 1):
#     if certain_number < 0:
#         print(f"{certain_number} is a negative number")
#     elif certain_number > 0:
#         print(f"{certain_number} is a positive number")
#     else:
#         print(f"{certain_number} is zero")

# Question 8: Divisibility Checker
# Write a Python program that checks every number from 1 to 50 (inclusive).

# Question 8: Divisibility Checker (FizzBuzz)
# Write a Python program that checks every number from 1 to 50 (inclusive).

# Your program must:
# 1. If a number is divisible by both 3 and 5, print "FizzBuzz".
# 2. If divisible by 3 only, print "Fizz".
# 3. If divisible by 5 only, print "Buzz".
# 4. Otherwise, print the number itself.

# for divide_number in range(1, 51):
#     if divide_number % 3 == 0 and divide_number % 5 == 0:
#         print('FizzBuzz')
#     elif divide_number % 3 == 0:
#         print('Fizz')
#     elif divide_number % 5 == 0:
#         print("Buzz")
#     else:
#         print(divide_number)

# Question 9: Number Classification
# Write a Python program that checks every number from 1 to 30 (inclusive).

# Your program must classify each number:
# - If the number is between 1 and 10, print "Small".
# - If the number is between 11 and 20, print "Medium".
# - If the number is between 21 and 30, print "Large".

# for number in range(1, 31):
#     if number >= 1 and number <= 10:
#         print(f'{number} is Small')
#     elif number >= 11 and number <= 20:
#         print(f"{number} is Medium")
#     else:
#         print(f"{number} is Large")

# Question 10: Multiples of Different Numbers
# Write a Python program that checks every number from 1 to 100 (inclusive).

# Your program must:
# 1. If a number is divisible by both 2 and 3, print "Multiple of 2 and 3".
# 2. If divisible by 2 only, print "Multiple of 2".
# 3. If divisible by 3 only, print "Multiple of 3".
# 4. Otherwise, print the number itself.

# for every_number in range(1, 101):
#     if every_number % 2 == 0 and every_number % 3 == 0:
#         print(f"{every_number} is a multiple of 2 and 3")
#     elif every_number % 2 == 0:
#         print(f"{every_number} is a multiple of 2")
#     elif every_number % 3 == 0:
#         print(f"{every_number} is a multiple of 3")
#     else:
#         print(every_number)

# Question 11: Sum of Even Numbers
# Write a Python program that calculates the sum of all even numbers between 1 and 50 (inclusive).

# Requirements:
# 1. Create a variable called total and initialise it to 0.
# 2. Use a for loop.
# 3. Use an if statement to identify even numbers.
# 4. Add each even number to total.
# 5. Print the final value of total after the loop finishes.
# 650

# total = 0

# for even in range(1, 51):
#     if even % 2 == 0:
#         total += even
#         print(total)

# Question 12: Count Odd Numbers
# Write a Python program that counts the number of odd numbers between 1 and 100 (inclusive).

# Requirements:
# 1. Create a variable called count_odd and initialise it to 0.
# 2. Use a for loop.
# 3. Use an if statement to identify odd numbers.
# 4. Increase count_odd by 1 whenever an odd number is found.
# 5. Print the final count outside the loop.


# count_odd = 0
# for odd_number in range(1, 101):
#     if odd_number  % 2!= 0:
#         count_odd += 1

# print(count_odd)

# Question 13 of 20 — Sum of Multiples of 3
# Write a Python program that calculates the sum of all multiples of 3 between 1 and 100 (inclusive).

# Requirements:
# 1. Create a variable called total and set it to 0.
# 2. Use a for loop to iterate through numbers from 1 to 100.
# 3. Use an if statement to check whether each number is divisible by 3.
# 4. Add each multiple of 3 to total.
# 5. Print the final total outside the loop.

# total = 0

# for multiples_of_three in range(1, 101):
#     if multiples_of_three % 3 == 0:
#         total += multiples_of_three

# print(total)

# Question 14 of 20 — Conditional Accumulator
# Write a Python program that loops through numbers 1 to 10.

# Your program must:
# 1. Create a variable called total and set it to 0.
# 2. Use a for loop to iterate from 1 to 10.
# 3. If the number is even, add the number itself to total.
# 4. Otherwise, if the number is odd, add 1 to total.
# 5. Print the final total outside the loop.

# total = 0

# for number in range(1, 11):
#     if number % 2 == 0:
#         even = number
#         total += even
#     else:
#         total += 1
# print(total)

# # or

# total = 0
# for number in range(1, 11):
#     if number % 2 == 0:
#         total += number    #  This one is the shorter one
#     else:
#         total += 1
# print(total)

# Question 15 of 20 — Multiple Accumulators
# Write a Python program that loops through numbers 1 to 50 (inclusive) and counts:
# 1. How many numbers are even.
# 2. How many numbers are odd.
# 3. How many numbers are divisible by 5.

# even = 0
# odd = 0
# divide_by_five = 0

# for numbers in range(1, 51):
#     if numbers % 2 == 0:
#         even += 1
#     elif numbers % 2 != 0:
#         odd += 1
#     if numbers % 5 == 0:
#         divide_by_five += 1

# print(f"{even} even numbers")
# print(f"{odd} odd numbers")
# print(f"{divide_by_five} numbers divisible by 5")

# Question 16 of 20 — Nested If Statements

# Write a Python program that loops through numbers 1 to 50 (inclusive).

# Your program must:
# 1. Use a for loop to iterate through numbers 1–50.
# 2. Check whether each number is even or odd.
# 3. If the number is even, perform another check:
#    - If divisible by 4, print "Even and divisible by 4".
#    - Otherwise, print "Even but not divisible by 4".
# 4. If the number is odd, print "Odd".

# for number in range(1, 51):
#     if number % 2 == 0:
#         if number % 4 == 0:
#             print("Even and divisible by 4")
#         else:
#             print("Even but not divisible by 4")
#     else:
#         print("Odd")

# Question 17 of 20 — Nested Conditions with Different Ranges
# Write a Python program that loops through numbers 1 to 100 (inclusive).

# Your program must follow these rules:
# 1. For numbers 1–50:
#    - Check whether each number is even or odd.
#    - Print "Even" or "Odd" accordingly.
# 2. For numbers 51–100:
#    - Check whether each number is divisible by 5.
#    - If divisible by 5, print "Divisible by 5".
#    - Otherwise, print "Not divisible by 5".

# for number in range(1, 101):
#     if  number <= 50:
#         if number % 2 == 0:
#             print("Even")
#         else:
#             print("Odd")
#     if number >= 51 and number <= 100:
#         if number % 5 == 0:
#             print("Divisible by 5")
#         else:
#             print("Not divisible by 5")
            
#             # or
            
# for number in range(1, 101):
#     if  number <= 50:
#         if number % 2 == 0:
#             print("Even")
#         else:
#             print("Odd")
#     else:
#         if number % 5 == 0:
#             print("Divisible by 5")
#         else:
#             print("Not divisible by 5")


# Question 18 of 20 — Compound Conditions (and / or)
# Write a Python program that loops through numbers 1 to 100 (inclusive).

# Your program must:
# 1. If a number is divisible by both 2 and 3, print "Divisible by both 2 and 3".
# 2. Otherwise, if a number is divisible by either 2 or 3, print "Divisible by 2 or 3".
# 3. Otherwise, print "Neither".

# for number in range(1,101):
#     if number % 2 == 0 and number % 3 == 0:
#         print("Divisible by both 2 and 3")
#     else:
#         if number % 2 == 0 or number % 3 == 0:
#             print("Divisible by 2 or 3")
#         else:
#             print("Neither")

# Question 19 of 20 — Nested and Compound Conditions
# Write a Python program that loops through numbers 1 to 50 (inclusive).

# Your program must follow these rules:
# 1. If the number is greater than 25:
#    - Check whether it is even or odd.
#    - Print "Even" or "Odd".
# 2. Otherwise (25 or below):
#    - Check whether it is divisible by 5.
#    - If it is, print "Divisible by 5".
#    - Otherwise, print "Not divisible by 5".

# for number in range(1, 51):
#     if number > 25:
#         if number % 2 ==0:
#             print("Even")
#         else:
#             print("Odd")
#     if number <= 25:
#         if number % 5 == 0:
#             print("Divisible by 5")
#         else:
#             print("Not divisible by 5")
            
#             # or
            
# for number in range(1, 51):
#     if number > 25:
#         if number % 2 == 0:
#             print('''"Even"''')
#         else:
#             print("Odd")
#     if number <= 25:
#         if number % 5 == 0:
#             print("Divisible by 5")
#         else:
#             print("Not divisible by 5")

# Question 20 of 20
# Write a Python program that loops through numbers 1 to 20 (inclusive).

# Your program must follow these rules:
# 1. Create a variable called total and initialize it to 0.
# 2. Use a for loop to iterate through numbers 1–20.
# 3. If the number is even, add the number itself to total.
# 4. Otherwise, if the number is odd and divisible by 3, add 3 to total.
# 5. Otherwise, if the number is odd and NOT divisible by 3, add 1 to total.
# 6. Print the final total outside the loop.

# total = 0

# for number in range(1, 21):
#     if number % 2 == 0:
#         total += number
#     if number % 2 != 0 and number % 3 == 0:
#         total += 3
#     if number % 2 != 0 and number % 3 != 0:
#         total+=1
# print(total)


##################### While Loops ####################################
