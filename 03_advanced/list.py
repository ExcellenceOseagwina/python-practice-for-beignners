# LESSON: Lists — keep several related values in one ordered collection
#
# This file is a set of study notes. Every example stays commented out so
# running the file does not change the behavior of the existing course files.
# Copy one small example into a scratch file, remove its leading # marks, and
# predict the result before you run it.

# A list stores multiple values in order. Square brackets create a list, and
# commas separate its items. A list can hold text, numbers, or mixed values.
# fruits = ["apple", "banana", "orange"]
# scores = [85, 92, 78]

# Each item has an index: the first index is 0, the next is 1, and so on.
# Negative indexes count from the end, so -1 means the last item.
# print(fruits[0])   # apple
# print(fruits[-1])  # orange

# Lists can be changed after creation. Assigning to an index replaces an item.
# fruits[1] = "pear"
# print(fruits)  # ['apple', 'pear', 'orange']

# append() adds one item at the end. len() tells us how many items are present.
# fruits.append("grape")
# print(len(fruits))

# A for loop visits every item in order. The loop variable holds the current
# item while the indented body runs once for each item.
# for fruit in fruits:
#     print(fruit)

# To keep a running total, start at zero and add each number as the loop sees
# it. sum(scores) is a built-in shortcut for this particular calculation.
# total = 0
# for score in scores:
#     total += score
# print(total)
# print(sum(scores))

# Slicing selects part of a list. The start index is included and the stop
# index is excluded, so this gets items at indexes 0 and 1.
# first_two_fruits = fruits[0:2]
# print(first_two_fruits)

# `in` checks whether a value is present and returns True or False.
# if "apple" in fruits:
#     print("Apple is in the list")

# CHALLENGE: Make a list of five expenses. Print each one, calculate the total,
# and find the average. The average is the total divided by the number of items.
# Try adding one expense and changing one existing value before calculating.
