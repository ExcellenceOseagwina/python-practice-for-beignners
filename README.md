# Python Practice for Beginners

A hands-on collection of beginner-friendly Python exercises and small console projects. This repository is designed to help you move from your first `print()` statement to solving practical problems with variables, user input, calculations, conditionals, and loops.

The examples use **Python 3** and the **Python standard library**. You do not need to install third-party packages to run the exercises.

> **Learning principle:** Read a small example, predict what it will do, run it, change it, and then try to recreate the solution without looking.

## Contents

- [Who this repository is for](#who-this-repository-is-for)
- [Learning objectives](#learning-objectives)
- [Prerequisites](#prerequisites)
- [Getting started](#getting-started)
- [Learning path](#learning-path)
- [How to practise](#how-to-practise)
- [Repository structure](#repository-structure)
- [Running the examples](#running-the-examples)
- [Important notes about simulations](#important-notes-about-simulations)
- [What's next](#whats-next)
- [Contributing](#contributing)
- [License](#license)

## Who this repository is for

This repository is for:

- People who are new to Python or programming.
- Learners who want short examples they can run and modify.
- Students practising problem-solving with small console applications.
- Beginners interested in seeing programming concepts applied to everyday and cybersecurity-themed scenarios.

You can work through the material in order or revisit individual files when practising a specific concept.

## Learning objectives

By working through the current exercises, you will practise how to:

- Create variables and work with strings, integers, floats, and booleans.
- Display output and collect input from a user.
- Convert input into numeric values and perform calculations.
- Use comparison and logical operators.
- Make decisions with `if`, `elif`, and `else`.
- Repeat instructions with `for` and `while` loops.
- Use counters and accumulators to keep track of results.
- Combine conditions and loops to solve small problems.
- Organize several basic concepts into console-based projects.

The advanced roadmap introduces topics that can be studied next; those topics are not all implemented as exercises yet.

## Prerequisites

- A computer running Windows, macOS, or Linux.
- Python 3 installed. Download it from [python.org](https://www.python.org/downloads/).
- A code editor, such as [Visual Studio Code](https://code.visualstudio.com/), or another editor you prefer.
- A terminal or command prompt.

Check that Python is available:

```bash
python --version
```

On some systems, use `python3 --version` (macOS/Linux) or `py --version` (Windows).

## Getting started

### 1. Get the repository

Clone it with Git:

```bash
git clone https://github.com/ExcellenceOseagwina/python-practice-for-beignners.git
cd python-practice-for-beignners
```

Alternatively, use GitHub's **Code → Download ZIP** option and extract the downloaded archive.

### 2. Choose a lesson

Start with the first beginner example:

```bash
python 01_beginner/basics/print_variables.py
```

If your system uses `python3`, run:

```bash
python3 01_beginner/basics/print_variables.py
```

### 3. Practise in your editor

Open the repository folder in your editor. Read the file, run it in a terminal, and experiment with the values and input.

**No virtual environment or dependency installation is required** for the current exercises because they use the Python standard library.

## Learning path

Follow the stages in order if you are learning Python for the first time. Each stage builds on concepts introduced earlier.

### Stage 1 — First steps: values and output

Learn how to run a Python file, assign values to variables, and display information.

| Exercise | Concepts |
| --- | --- |
| [`print_variables.py`](01_beginner/basics/print_variables.py) | Variables, strings, integers, and `print()` |
| [`bool.py`](01_beginner/basics/bool.py) | Boolean values: `True` and `False` |
| [`movie_rating.py`](01_beginner/basics/movie_rating.py) | Strings, integers, floats, and output |
| [`personal_profile_generator.py`](01_beginner/basics/personal_profile_generator.py) | Building a report and converting values to text |
| [`worker_details.py`](01_beginner/basics/worker_details.py) | Reusing variables in calculations and output |

**You are ready to move on when you can:** explain what a variable is, recognize the basic data types, and display a calculated value.

### Stage 2 — Input, arithmetic, and decisions

Learn to accept information from a user, convert input into numbers, perform calculations, and choose what a program does.

| Exercise | Concepts |
| --- | --- |
| [`simple_calculator.py`](01_beginner/calculators/simple_calculator.py) | `input()`, type conversion, arithmetic, and conditionals |
| [`simple_guessing_game.py`](01_beginner/games/simple_guessing_game.py) | Comparisons, ranges, and combined conditions |

**You are ready to move on when you can:** write a program that asks a question and produces different responses depending on the answer.

### Stage 3 — Loops and repetition

Learn how to repeat instructions, process ranges of numbers, count matching values, and calculate running totals.

| Exercise | Concepts |
| --- | --- |
| [`number_ranges.py`](01_beginner/loops/for_loops/number_ranges.py) | `for` loops, `range()`, and number sequences |
| [`totals_and_counts.py`](02_intermediate/loops/for_loops/totals_and_counts.py) | Counters, accumulators, and conditions inside loops |
| [`conditions.py`](02_intermediate/loops/for_loops/conditions.py) | Nested and combined conditions inside loops |
| [`counting.py`](02_intermediate/loops/while_loops/counting.py) | `while` loops, repeated input, and nested loops |

Some loop examples demonstrate `break` and `continue`. Run interactive examples in a terminal so you can provide input when prompted.

**You are ready to move on when you can:** use a loop to process a range of values and produce a count, total, or other result.

### Stage 4 — Small practical projects

Combine variables, input, calculations, conditionals, and loops in programs that model simple tasks.

| Exercise | Concepts |
| --- | --- |
| [`student_grade_calculator.py`](02_intermediate/conditionals/student_grade_calculator.py) | Scores, averages, and grade decisions |
| [`simple_student_result_mang_system.py`](02_intermediate/conditionals/simple_student_result_mang_system.py) | Ordered grade ranges and formatted results |
| [`login_access_simulator.py`](02_intermediate/conditionals/login_access_simulator.py) | Nested decisions and empty input |
| [`bill_split_calc.py`](02_intermediate/calculators/bill_split_calc.py) | Arithmetic and splitting costs |
| [`electricity_bill_calculator.py`](02_intermediate/calculators/electricity_bill_calculator.py) | Calculations and rate selection |
| [`game_profile.py`](02_intermediate/games/game_profile.py) | Collecting and presenting related information |
| [`cyber_profile_gen.py`](02_intermediate/cybersecurity/cyber_profile_gen.py) | A cybersecurity-themed profile |
| [`cyber_access_checker.py`](02_intermediate/cybersecurity/cyber_access_checker.py) | Conditional access decisions |
| [`cybersecurity_risk_classifier.py`](02_intermediate/cybersecurity/cybersecurity_risk_classifier.py) | Basic risk classification logic |
| [`simple_atm_simulator.py`](02_intermediate/simulations/simple_atm_simulator.py) | Menus, decisions, and calculations |

**Project challenge:** Choose one project and extend it. For example, allow the user to perform multiple operations, handle invalid menu choices, and display a clear result after each operation.

## How to practise

For each exercise, use this workflow:

1. **Read:** Identify the problem the program is trying to solve.
2. **Predict:** Before running it, write down what you expect the output to be.
3. **Run:** Execute the file from the repository root.
4. **Experiment:** Change values and try different inputs.
5. **Explain:** Describe what each important line does in your own words.
6. **Rebuild:** Close the example and try to write a similar program from memory.
7. **Extend:** Add one small feature without copying a complete solution.

When an exercise asks for input, enter the kind of value it expects. Some early examples assume valid input; input validation is introduced later. If a program behaves unexpectedly, read the error message and check the line number before changing the code.

## Repository structure

```text
python-practice-for-beignners/
├── 01_beginner/
│   ├── basics/
│   ├── calculators/
│   ├── games/
│   └── loops/
├── 02_intermediate/
│   ├── calculators/
│   ├── conditionals/
│   ├── cybersecurity/
│   ├── games/
│   ├── loops/
│   └── simulations/
├── 03_advanced/
│   └── README.md
└── README.md
```

The folders are grouped by learning stage and topic. Individual filenames describe the exercise or program they contain.

## Running the examples

Run commands from the **repository root** so the relative file paths in the examples work.

General form:

```bash
python path/to/file.py
```

Examples:

```bash
python 01_beginner/basics/bool.py
python 01_beginner/calculators/simple_calculator.py
python 02_intermediate/loops/for_loops/totals_and_counts.py
```

If `python` is not recognized, try `python3` or `py`, depending on your operating system and Python installation.

## Important notes about simulations

The login, access-checking, ATM, and cybersecurity-themed programs are **educational console simulations**. They demonstrate programming logic; they are not production security tools.

- Do not use sample credentials as real credentials.
- Do not enter real passwords, personal information, banking details, or other secrets.
- The access-checking examples do not implement secure authentication or authorization.
- The risk classifier is a simplified learning exercise, not a formal risk assessment framework.
- The ATM simulator does not connect to a bank or handle real money.

Real security systems require appropriate authentication, authorization, secure secret storage, input validation, logging, testing, and other controls that are outside the scope of these beginner exercises.

## What's next

The [advanced learning roadmap](03_advanced/README.md) outlines topics to study after the current beginner and intermediate exercises:

1. Collections: lists, tuples, dictionaries, and sets.
2. Functions and error handling.
3. Files and modules.
4. Automated testing.
5. Object-oriented programming.

These are roadmap topics, not a claim that every topic already has a completed exercise in this repository. Add practice files as you learn them.

## Contributing

Suggestions, corrections, and beginner-friendly exercises are welcome. Before submitting a change, read the [contribution guidelines](CONTRIBUTING.md).

## License

No license file is currently included in this repository. Unless a license is added, the default copyright rules apply; you should not assume that the code may be reused, modified, or redistributed under an open-source license.
