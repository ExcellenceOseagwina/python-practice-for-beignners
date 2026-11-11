"""For-loop exercises for counting, ranges, and number patterns."""

# A for loop repeats its indented lines for each number in a group. range()
# makes the numbers. It stops before its last value, so use 21 to include 20.

# Exercise 1: Print Numbers
# Print every number from 1 to 20, inclusive.
# range(1, 21) starts at 1 and stops before 21. It gives us 1 through 20.
for number in range(1, 21):
    print(number)

# Exercise 2: Countdown
# Print numbers from 20 down to 1.
# The last value, -1, tells range() to count down by one. It stops before 0.
for number in range(20, 0, -1):
    print(number)

# Exercise 3: Multiplication Table
# Print the multiplication table of 7, from 1 to 12.
# multiplier gets the next number each time around the loop. The f-string
# puts the numbers and their answer into the printed line.
for multiplier in range(1, 13):
    print(f"7 x {multiplier} = {7 * multiplier}")

# Exercise 4: Even Numbers
# Print all even numbers between 1 and 50, inclusive.
# % gives the remainder after division. Even numbers have a remainder of 0
# when divided by 2.
for number in range(1, 51):
    if number % 2 == 0:
        print(number)

# Exercise 5: Odd Numbers
# Print all odd numbers between 1 and 50, inclusive.
# Odd numbers have a remainder other than 0 when divided by 2.
for number in range(1, 51):
    if number % 2 != 0:
        print(number)

# Exercise 6: Even or Odd Classification
# Classify every number between 1 and 30.
# else runs when the even-number condition is false; the two categories cover
# every integer in this range.
for number in range(1, 31):
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")

# Exercise 7: Positive, Negative, or Zero
# Classify every number from -10 to 10, inclusive.
# elif checks positive values only after the negative case fails; else therefore
# represents the one remaining value, zero.
for number in range(-10, 11):
    if number < 0:
        print(f"{number} is a negative number")
    elif number > 0:
        print(f"{number} is a positive number")
    else:
        print(f"{number} is zero")
