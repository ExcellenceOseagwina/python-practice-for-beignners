# Python Practice for Beginners

A step-by-step path from your first Python program to small console projects.
The lessons use Python 3 and its standard library; no extra packages are
needed.

## Start here

If you are new to programming, follow the stages in order. Read each file,
predict what it will do, and run it from the repository root. Then change a
value or try different input. When a program asks for a number, enter a valid
number; input validation comes later in the path.

```bash
python 01_beginner/basics/print_variables.py
```

Use a terminal for programs that ask questions. After each lesson, try to
write a small version yourself without copying.

## Learning path

### 1. First steps: values and output

Learn to run a Python file, assign values to names, and display results.

1. [`print_variables.py`](01_beginner/basics/print_variables.py) — variables,
   text, whole numbers, and `print()`.
2. [`bool.py`](01_beginner/basics/bool.py) — true and false values.
3. [`movie_rating.py`](01_beginner/basics/movie_rating.py) — text, integers,
   decimals, and displaying related information.
4. [`personal_profile_generator.py`](01_beginner/basics/personal_profile_generator.py)
   — build a report and convert numbers to text.
5. [`worker_details.py`](01_beginner/basics/worker_details.py) — reuse values
   in calculations and output.

**Check your understanding:** explain what a variable stores, name a few basic
value types, and combine text with a calculated value in printed output.

### 2. Input, arithmetic, and choices

Learn to read what a user types, convert text into numbers, calculate, and
choose a response with conditions.

1. [`simple_calculator.py`](01_beginner/calculators/simple_calculator.py) —
   input, number conversion, arithmetic, and `if`/`elif`/`else`.
2. [`simple_guessing_game.py`](01_beginner/games/simple_guessing_game.py) —
   comparisons, ranges, and combined conditions.

**Check your understanding:** write a program that asks a question, checks the
answer, and responds differently for at least two cases.

### 3. Repetition and problem solving

Learn to repeat actions, count, and keep a running total.

1. [`number_ranges.py`](01_beginner/loops/for_loops/number_ranges.py) — `for`,
   `range()`, counting, and number patterns.
2. [`totals_and_counts.py`](02_intermediate/loops/for_loops/totals_and_counts.py)
   — counters, running totals, and conditions inside loops.
3. [`conditions.py`](02_intermediate/loops/for_loops/conditions.py) — nested
   and combined checks inside loops.
4. [`counting.py`](02_intermediate/loops/while_loops/counting.py) — `while`,
   `break`, `continue`, repeated input, and nested loops. This file contains
   interactive examples; run it in a terminal.

**Check your understanding:** use a loop to process a range of numbers and
report a count or total.

### 4. Put the basics together

Use input, conditions, and loops to solve small practical problems.

1. [`student_grade_calculator.py`](02_intermediate/conditionals/student_grade_calculator.py)
   — check scores, calculate an average, and choose a grade.
2. [`simple_student_result_mang_system.py`](02_intermediate/conditionals/simple_student_result_mang_system.py)
   — apply ordered grade bands and format a report.
3. [`login_access_simulator.py`](02_intermediate/conditionals/login_access_simulator.py)
   — nested choices and empty input.
4. [`bill_split_calc.py`](02_intermediate/calculators/bill_split_calc.py) and
   [`electricity_bill_calculator.py`](02_intermediate/calculators/electricity_bill_calculator.py)
   — calculate amounts and select rates.
5. [`game_profile.py`](02_intermediate/games/game_profile.py) — gather and
   present related information.
6. [`cyber_profile_gen.py`](02_intermediate/cybersecurity/cyber_profile_gen.py),
   [`cyber_access_checker.py`](02_intermediate/cybersecurity/cyber_access_checker.py),
   and
   [`cybersecurity_risk_classifier.py`](02_intermediate/cybersecurity/cybersecurity_risk_classifier.py)
   — practice Python with cybersecurity examples.
7. [`simple_atm_simulator.py`](02_intermediate/simulations/simple_atm_simulator.py)
   — combine a menu, decisions, and calculations.

**Project challenge:** choose one program, let the user repeat actions, handle
invalid choices, and show a clear result. The login and access examples use
sample credentials for practice only; they do not protect real accounts or
information.

### 5. Next: collections, functions, and errors

These topics do not have practice files in this repository yet. Learn them in
order and add a small program of your own for each:

1. Lists and tuples: store ordered values and access or update items.
2. Loop through collections and text; use `enumerate()`, membership checks,
   and slicing.
3. Dictionaries: store related key/value data and look up or update entries.
4. Sets: store unique values and compare groups.
5. Functions: name reusable steps, accept parameters, and return results.
6. Error handling: respond to expected problems such as invalid input.

Project ideas: an expense tracker, a contact book, or an inventory manager.

### 6. Further study: files and object-oriented Python

Continue with saving and loading data from files, splitting code into modules,
and writing tests. Then learn classes, objects, attributes, methods, and
inheritance. Project idea: a library manager that tracks books and borrowers.
See the [advanced roadmap](03_advanced/README.md) for a topic-by-topic guide.

## Folder guide

- `01_beginner/` — first concepts, calculator, guessing game, and `for` loops.
- `02_intermediate/` — more loop practice and small console projects.
- `03_advanced/` — roadmap for topics to study and add next.
