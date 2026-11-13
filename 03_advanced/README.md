# Advanced Python Learning Roadmap

This roadmap is for learners who have completed the beginner and intermediate exercises in the [main learning path](../README.md).

The topics below are planned learning steps. They are **not all implemented as exercises in this repository yet**. Study one topic at a time, write small examples, and add practice projects as you progress.

## 1. Collections and data structures

Learn how to store, organize, and process groups of values.

1. **Lists** — create ordered collections, access items by index, update values, and use methods such as `append()`, `remove()`, and `sort()`.
2. **Tuples** — work with ordered collections that cannot be changed after creation.
3. **Strings and iteration** — loop through text, check whether a value exists, and use indexing and slicing.
4. **Dictionaries** — store related key/value pairs, look up values, add entries, and update existing data.
5. **Sets** — store unique values and perform union, intersection, and difference operations.
6. **Comprehensions and aggregation** — build collections with comprehensions and use `sum()`, `min()`, `max()`, and `sorted()`.

**Practice projects:** expense tracker, contact book, and student records manager.

## 2. Functions and error handling

Learn to divide a program into reusable, understandable pieces.

1. Define functions with `def`.
2. Pass information into functions using parameters and arguments.
3. Return results with `return`.
4. Use local variables and understand variable scope.
5. Handle expected errors with `try` and `except`.
6. Use `else` and `finally` in exception handling when appropriate.
7. Explore recursion, `map()`, and `filter()` after becoming comfortable with ordinary functions and loops.

**Practice project:** build an inventory manager that can add items, update quantities, search for products, and report available stock. Store the data in a dictionary and put each operation in a separate function.

## 3. Files and modules

Learn to preserve information and organize larger programs.

1. Read and write text files.
2. Use `with open(...)` to manage files safely.
3. Understand file paths and common file modes.
4. Split related code into modules.
5. Import functions and values from other modules.
6. Explore JSON for storing structured data.

**Practice project:** build a contact book that saves contacts to a file and loads them when the program starts.

## 4. Testing and debugging

Learn how to check that your program behaves as expected.

1. Reproduce a problem with a small test case.
2. Read tracebacks and use them to locate errors.
3. Test functions with normal, boundary, and invalid inputs.
4. Start with Python's built-in `unittest` module.
5. Separate program logic from user-interface input and output where practical.

**Practice task:** write tests for the calculations and decisions in your student grade calculator.

## 5. Object-oriented programming

Learn how to model related data and behavior with classes and objects.

1. Create classes and instantiate objects.
2. Understand `self`, attributes, methods, and `__init__`.
3. Distinguish instance attributes from class attributes.
4. Use properties when controlled attribute access is useful.
5. Learn inheritance and method overriding after you can design simple classes.
6. Understand composition and when it is preferable to inheritance.

**Practice project:** create a library manager with `Book` and `Member` classes, including borrow and return operations.

## Suggested order

If you are unsure what to study next, follow this sequence:

1. Collections
2. Functions
3. Error handling
4. Files and modules
5. Testing and debugging
6. Object-oriented programming

Build a small working program at each stage before moving to the next.

## Adding advanced lessons to this repository

When adding a new lesson:

- Use a descriptive filename in the relevant topic folder.
- Keep each exercise focused on one main learning objective.
- Explain unfamiliar concepts with short comments or a nearby README.
- Include a clear example of expected input and output when useful.
- Add a small task for the learner to attempt independently.
- Update the main [README learning path](../README.md) so the new lesson is discoverable.
