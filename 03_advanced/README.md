# Advanced learning roadmap

Use this roadmap after completing the beginner and intermediate lessons in the
main [learning path](../README.md). These topics do not yet have exercises in
the repository. Study one section at a time, write small examples, and build
the suggested projects as practice.

## 1. Collections

Learn to keep and organize groups of information:

1. **Lists and tuples** — create sequences, access items by index, update
   lists, use common methods, and understand immutable tuples.
2. **Iteration and strings** — loop through values and text, use
   `enumerate()`, check membership, and slice sequences.
3. **Dictionaries** — store key/value data, look up and update entries, and
   loop through keys and values.
4. **Sets** — keep unique values and compare groups with union and
   intersection.
5. **Comprehensions and aggregation** — build collections concisely and use
   `sum()`, `min()`, `max()`, and `sorted()`.

**Project ideas:** expense tracker, contact book, and student records manager.

## 2. Functions and error handling

1. Define functions with `def` and pass information through parameters.
2. Return results and split a long program into small, reusable steps.
3. Use `try` and `except` to handle expected errors such as invalid input.
4. Once comfortable with these basics, explore recursion and tools such as
   `map()` and `filter()`.

**Project:** build an inventory manager that adds items, updates quantities,
and reports available stock. Store items in a dictionary and put each action
in a function.

## 3. Files, modules, and tests

1. Read and write text files with `with open(...)` so information remains
   available after the program exits.
2. Move related functions into modules and import them where needed.
3. Write small tests for calculations and decisions so changes do not break
   earlier behavior.

**Project:** save contacts to a file, load them when the program starts, and
check the add, find, and delete operations.

## 4. Object-oriented programming

1. Create classes and objects; learn `self`, attributes, methods, and
   `__init__`.
2. Understand instance and class attributes. Use properties when they help
   control access to data.
3. Learn inheritance and method overriding after you can build a useful class
   without them.

**Project:** create a library manager with `Book` and `User` classes, plus
borrow and return operations.

## How to add lessons here

Create one clearly named Python file per small lesson. Explain new ideas with
beginner-friendly comments, show a working example, and end with a short task
for the learner to try.
