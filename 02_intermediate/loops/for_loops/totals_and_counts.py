"""For-loop exercises for accumulating totals and counting matches."""

# Exercise 11: Sum of Even Numbers
# Calculate the sum of even numbers between 1 and 50.
total = 0
for number in range(1, 51):
    if number % 2 == 0:
        total += number
print(total)

# Exercise 12: Count Odd Numbers
# Count the odd numbers between 1 and 100.
count_odd = 0
for number in range(1, 101):
    if number % 2 != 0:
        count_odd += 1
print(count_odd)

# Exercise 13: Sum of Multiples of 3
# Sum multiples of 3 between 1 and 100.
total = 0
for number in range(1, 101):
    if number % 3 == 0:
        total += number
print(total)

# Exercise 14: Conditional Accumulator
# For numbers 1-10, add even numbers to total and add 1 for each odd number.
total = 0
for number in range(1, 11):
    if number % 2 == 0:
        total += number
    else:
        total += 1
print(total)

# Exercise 15: Multiple Accumulators
# Count even numbers, odd numbers, and numbers divisible by 5 from 1 to 50.
even_count = 0
odd_count = 0
divisible_by_five_count = 0
for number in range(1, 51):
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    if number % 5 == 0:
        divisible_by_five_count += 1
print(f"{even_count} even numbers")
print(f"{odd_count} odd numbers")
print(f"{divisible_by_five_count} numbers divisible by 5")

# Exercise 20: Conditional Sum
# For numbers 1-20, add even numbers, add 3 for odd multiples of 3,
# and add 1 for all other odd numbers.
total = 0
for number in range(1, 21):
    if number % 2 == 0:
        total += number
    elif number % 3 == 0:
        total += 3
    else:
        total += 1
print(total)
