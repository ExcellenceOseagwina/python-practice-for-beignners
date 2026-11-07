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
