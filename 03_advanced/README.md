# Advanced Python Learning Roadmap

Use this roadmap after completing the beginner and intermediate exercises in
the [main learning path](../README.md). Some topics below are not implemented
as lessons in this repository yet. Study them in sequence, write small
examples, and build the suggested projects as practice.

## 1. Functions

Learn to divide a program into reusable, understandable steps.

1. Define functions with `def` and call them by name.
2. Pass information with parameters and arguments.
3. Return results with `return` and use default argument values.
4. Understand local variables and scope.
5. After the basics, explore recursion and higher-order functions such as
   `map()` and `filter()`.

**Practice project:** build an inventory manager that adds items, updates
quantities, searches products, and reports stock. Store the data in a
dictionary and put each operation in a function.

## 2. Collections and sequence processing

Learn to store and process groups of values.

1. **Lists** — create ordered collections, access items by index, update
   values, and use methods such as `append()`, `remove()`, and `sort()`.
2. **Tuples** — work with ordered collections that cannot be changed after
   creation.
3. **Iteration and strings** — loop through collections and text, use
   `enumerate()`, check whether a value exists, and use indexing and slicing.

**Practice project:** create an expense tracker that stores expenses in a
list and calculates the total and average.

## 3. Dictionaries and applications

Learn to store related information as key/value pairs.

1. Create dictionaries and look up values by key.
2. Add, change, and remove entries; check whether a key exists.
3. Loop through keys and values, including nested dictionaries.

**Practice projects:** recipe manager, contact book, and student records
manager.

## 4. Sets, aggregation, and comprehensions

1. Use sets to keep unique values and compare groups with union,
   intersection, and difference.
2. Summarize data with `sum()`, `min()`, `max()`, and `sorted()`.
3. Use list comprehensions to build a new list from existing values, with or
   without a condition.

**Practice challenge:** take a list of names or scores, remove duplicates,
sort the results, and report useful totals.

## 5. Error handling

Learn to handle expected failures without abruptly stopping the program.

1. Read a traceback to identify where and why an error occurred.
2. Use `try` and `except` for errors such as invalid numeric input.
3. Handle different expected errors separately; use `else` and `finally` when
   they make the flow clearer.
4. Keep the `try` block focused on the operation that may fail.

**Practice challenge:** update a calculator to ask again when a user enters
invalid numbers or chooses an unsupported operation.

## 6. Files and modules

Learn to preserve information and organize larger programs.

1. Read and write text files; use `with open(...)` to manage them safely.
2. Understand file paths and common file modes.
3. Split related code into modules and import functions where needed.
4. Explore JSON for storing structured data.

**Practice project:** build a contact book that saves contacts to a file and
loads them when it starts.

## 7. Testing and debugging

Learn to check that your program behaves as expected.

1. Reproduce a problem with a small example.
2. Test functions with normal, boundary, and invalid inputs.
3. Start with Python's built-in `unittest` module.
4. Separate program logic from input and output where practical.

**Practice task:** write tests for the calculations and decisions in a student
grade calculator.

## 8. Object-oriented programming

Learn to model related data and behavior with classes and objects.

1. Create classes and instantiate objects.
2. Understand `self`, attributes, methods, and `__init__`.
3. Distinguish instance attributes from class attributes; use properties when
   controlled attribute access is useful.
4. Learn inheritance and method overriding after you can design simple
   classes. Understand composition and when it is preferable to inheritance.

**Practice project:** create a library manager with `Book` and `Member`
classes, including borrow and return operations.

## Adding lessons to this repository

When adding a lesson, use a descriptive filename, keep it focused on one main
learning objective, explain unfamiliar ideas with short comments, and include
a small challenge. Update the [main learning path](../README.md) so learners
can find it in the right order.
