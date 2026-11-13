# Next steps: collections, reusable code, and object-oriented Python

This folder is a study roadmap. The repository does not yet contain exercises
for the topics below. The order follows the later sections of the
[Coddy Python syllabus](https://coddy.tech/landing/python) and adds files,
modules, and tests as practical skills to learn alongside it.

## 1. Collections

Learn to keep related values together and work through them:

1. **Lists and tuples** — create sequences, index and update lists, use common
   methods, and understand immutable tuples.
2. **Iteration and strings** — loop through values and text, use `enumerate()`,
   check membership, and slice sequences.
3. **Dictionaries** — store key/value data, look up and update entries, and
   loop over keys and values.
4. **Sets** — store unique values, remove duplicates, and compare groups with
   union and intersection.
5. **Comprehensions and aggregation** — build collections concisely and use
   `sum()`, `min()`, `max()`, and `sorted()`.

**Practice projects:** an expense tracker, contact book, and student records
manager.

## 2. Functions and error handling

1. Define functions with `def`; use parameters to pass information in.
2. Return results and split a long program into small steps.
3. Handle expected problems with `try` and `except`, especially invalid input.
4. After the basics, explore recursion and higher-order functions such as
   `map()` and `filter()`.

**Practice project:** an inventory manager that adds items, updates quantities,
and reports stock. Keep the data in dictionaries and put each operation in a
function.

## 3. Files, modules, and tests

These supporting topics help turn a one-file exercise into a maintainable
program:

1. Read and write text files with `with open(...)` so information survives
   after the program exits.
2. Move related functions into modules and import them where needed.
3. Write small tests for calculations and decisions so changes do not break
   earlier behavior.

**Practice project:** save contacts to a file, load them at startup, and test
the add, find, and delete operations.

## 4. Object-oriented programming

1. Create a class and make objects from it; learn `self`, attributes, methods,
   and `__init__`.
2. Understand instance and class attributes, then use properties where they
   help control access to data.
3. Learn inheritance and method overriding after you can build a useful class
   without them.

**Practice project:** a library manager with `Book` and `User` classes and
borrow/return operations.

## Study routine

For each topic, write one tiny example, change it, and explain what each part
does. Then build the suggested project in small steps. Add new exercises under
`03_advanced/`, with clear filenames, beginner-friendly comments, and a short
challenge for the learner.
