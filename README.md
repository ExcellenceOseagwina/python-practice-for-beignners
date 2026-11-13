# Python Practice for Beginners

A step-by-step Python course made from small programs you can read, run, and
change. Lessons use Python 3 and the standard library; no extra packages are
needed.

## How to use this course

For each lesson, read the comments, predict what the program will do, then run
it from the project root. Change a value or try different answers and observe
what changes. For prompt-based exercises, try solving the task before looking
at the working code. Keep notes on new terms and errors you encounter.

Run a lesson like this:

```bash
python 01_beginner/basics/print_variables.py
```

Some scripts ask for input. Enter the kind of value requested (for example, a
number when prompted for a score). Invalid text may cause an error; input
validation is introduced later in the course.

## Learning path

Follow the stages in order. Within a stage, the numbered sequence introduces
ideas gradually; you can revisit any program as practice.

### 1. Beginner: values, decisions, and repetition

**Start with basics**

1. [`print_variables.py`](01_beginner/basics/print_variables.py) — names,
   strings, integers, and printing.
2. [`bool.py`](01_beginner/basics/bool.py) — `True` and `False` values.
3. [`movie_rating.py`](01_beginner/basics/movie_rating.py) — storing different
   kinds of values and displaying them.
4. [`personal_profile_generator.py`](01_beginner/basics/personal_profile_generator.py)
   — build a report from variables and convert numbers to text.
5. [`worker_details.py`](01_beginner/basics/worker_details.py) — reuse values
   and calculate with them.

**Use input and make choices**

6. [`simple_calculator.py`](01_beginner/calculators/simple_calculator.py) —
   read numbers, convert input, and choose an operation with `if` statements.
7. [`simple_guessing_game.py`](01_beginner/games/simple_guessing_game.py) —
   compare values and combine conditions.

**Repeat steps**

8. [`number_ranges.py`](01_beginner/loops/for_loops/number_ranges.py) — use
   `for` and `range()` to count, make patterns, and classify numbers.

### 2. Intermediate: build useful programs

These lessons assume you can use variables, conditionals, and basic loops.

**Practice conditions and validation**

1. [`student_grade_calculator.py`](02_intermediate/conditionals/student_grade_calculator.py)
   — validate scores, calculate an average, and select a grade.
2. [`simple_student_result_mang_system.py`](02_intermediate/conditionals/simple_student_result_mang_system.py)
   — apply ordered grade bands and format a report.
3. [`login_access_simulator.py`](02_intermediate/conditionals/login_access_simulator.py)
   — use nested decisions and handle empty input.

**Build loop skills**

4. [`totals_and_counts.py`](02_intermediate/loops/for_loops/totals_and_counts.py)
   — accumulate totals and count matching values.
5. [`conditions.py`](02_intermediate/loops/for_loops/conditions.py) — combine
   loops with nested and compound conditions.
6. [`counting.py`](02_intermediate/loops/while_loops/counting.py) — use
   `while`, counters, `break`, `continue`, and nested loops. This file contains
   interactive exercises; run it in a terminal and answer its prompts.

**Apply the ideas to projects**

7. [`bill_split_calc.py`](02_intermediate/calculators/bill_split_calc.py) and
   [`electricity_bill_calculator.py`](02_intermediate/calculators/electricity_bill_calculator.py)
   — calculate costs and split amounts.
8. [`game_profile.py`](02_intermediate/games/game_profile.py) — collect and
   present related information.
9. [`cyber_profile_gen.py`](02_intermediate/cybersecurity/cyber_profile_gen.py),
   [`cyber_access_checker.py`](02_intermediate/cybersecurity/cyber_access_checker.py),
   and [`cybersecurity_risk_classifier.py`](02_intermediate/cybersecurity/cybersecurity_risk_classifier.py)
   — use familiar Python concepts in cybersecurity-themed examples.
10. [`simple_atm_simulator.py`](02_intermediate/simulations/simple_atm_simulator.py)
    — bring conditionals and user choices together in a small simulation.

### 3. Advanced: next topics to learn

There are no advanced exercises yet. The [advanced roadmap](03_advanced/README.md)
suggests what to study next: functions, lists and dictionaries, error handling,
files and modules, classes, and tests. Move on when you are comfortable
combining input, conditions, and loops in the intermediate projects.

## Safety note

The login and access-checking examples use sample credentials in source code.
They demonstrate conditionals only; do not use them to protect real accounts
or information.
