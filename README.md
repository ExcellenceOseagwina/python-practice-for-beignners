# Python Practice for Beginners

A guided path from your first Python statements to small console projects. The
lessons use Python 3 and its standard library; no extra packages are required.

This path is organized around the **Coddy (Coddy.tech) Python course**: its
fundamentals lead into collections and functions, followed by error handling
and object-oriented programming. This repository supplies its own practice
programs and does not copy Coddy's lesson content.

- [Coddy Python course and syllabus](https://coddy.tech/landing/python)
- [Coddy curriculum roadmap](https://github.com/coddytech/curriculum)

## How to study

Work through the stages in order. For each file, read the comments, predict
the output, run it, then change the values or inputs and run it again. Before
moving on, try to recreate the main idea in a fresh file without copying.

Run commands from the repository root:

```bash
python 01_beginner/basics/print_variables.py
```

Some lessons ask for input and expect a valid number. Input validation is
introduced later. Run interactive programs in a terminal.

## Learning path

### Stage 1 — Fundamentals: values, operators, and decisions

Start with these beginner lessons:

1. [`print_variables.py`](01_beginner/basics/print_variables.py) — variables,
   strings, integers, and output.
2. [`bool.py`](01_beginner/basics/bool.py) — Boolean values.
3. [`movie_rating.py`](01_beginner/basics/movie_rating.py) — strings, numbers,
   and displaying related values.
4. [`personal_profile_generator.py`](01_beginner/basics/personal_profile_generator.py)
   — build a report and convert numbers to strings.
5. [`worker_details.py`](01_beginner/basics/worker_details.py) — reuse values
   and calculate with them.
6. [`simple_calculator.py`](01_beginner/calculators/simple_calculator.py) —
   input, number conversion, arithmetic, and `if`/`elif`/`else`.
7. [`simple_guessing_game.py`](01_beginner/games/simple_guessing_game.py) —
   comparisons and combined conditions.

**Ready to continue when:** you can explain the difference between text and a
number, use arithmetic and comparisons, and write a short conditional program.

### Stage 2 — Repetition and small programs

1. [`number_ranges.py`](01_beginner/loops/for_loops/number_ranges.py) —
   `for`, `range()`, and simple number patterns.
2. [`totals_and_counts.py`](02_intermediate/loops/for_loops/totals_and_counts.py)
   — counters, running totals, and conditions inside loops.
3. [`conditions.py`](02_intermediate/loops/for_loops/conditions.py) — nested
   and compound checks in loops.
4. [`counting.py`](02_intermediate/loops/while_loops/counting.py) — `while`,
   `break`, `continue`, input repetition, and nested loops. It contains
   interactive examples; run it in a terminal.
5. [`student_grade_calculator.py`](02_intermediate/conditionals/student_grade_calculator.py)
   — validate scores, calculate an average, and choose a grade.
6. [`simple_student_result_mang_system.py`](02_intermediate/conditionals/simple_student_result_mang_system.py)
   — ordered grade bands and a formatted report.
7. [`login_access_simulator.py`](02_intermediate/conditionals/login_access_simulator.py)
   — nested decisions and empty input.

**Ready to continue when:** you can repeat an action with a loop, keep a
counter or total, and handle several possible user choices.

### Stage 3 — Apply fundamentals in projects

Try these after the matching lessons above:

1. [`bill_split_calc.py`](02_intermediate/calculators/bill_split_calc.py) and
   [`electricity_bill_calculator.py`](02_intermediate/calculators/electricity_bill_calculator.py)
   — percentages, arithmetic, and tiered decisions.
2. [`game_profile.py`](02_intermediate/games/game_profile.py) — gather and
   present related information.
3. [`cyber_profile_gen.py`](02_intermediate/cybersecurity/cyber_profile_gen.py),
   [`cyber_access_checker.py`](02_intermediate/cybersecurity/cyber_access_checker.py),
   and
   [`cybersecurity_risk_classifier.py`](02_intermediate/cybersecurity/cybersecurity_risk_classifier.py)
   — practice familiar Python ideas with cybersecurity examples.
4. [`simple_atm_simulator.py`](02_intermediate/simulations/simple_atm_simulator.py)
   — combine a menu, conditions, and calculations.

**Project challenge:** improve one program so it accepts input repeatedly,
rejects invalid choices, and gives a clear result. The login and access
examples use sample credentials for practice only; they do not protect real
accounts or information.

### Stage 4 — Collections, functions, and errors

The next topics follow Coddy's progression beyond the fundamentals. There are
not exercises for these topics in the repository yet; use the linked course
for instruction and add a small practice program for each topic.

1. Lists and tuples: store ordered values, access and change items.
2. Iterating over collections and strings; use `enumerate()` and slicing.
3. Dictionaries: store related key/value data and loop through it.
4. Sets: represent unique values and compare groups.
5. Functions: define reusable steps, accept parameters, and return results.
6. Error handling: use `try` and `except` for expected input errors.

Suggested practice projects: expense tracker, contact book, and inventory
manager.

### Stage 5 — Object-oriented Python and beyond

Continue with classes, objects, attributes, methods, and `__init__`, then
practice inheritance and properties. Suggested project: a library manager
with book and user objects. The repository's [advanced roadmap](03_advanced/README.md)
tracks these topics and the follow-on skills of files, modules, and tests.

## Repository layout

- `01_beginner/` — first concepts, calculator, guessing game, and `for` loops.
- `02_intermediate/` — longer loop practice and console projects.
- `03_advanced/` — roadmap for topics not yet implemented as exercises.
