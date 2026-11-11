# Python Course: Learn by Reading and Running

This repository is a Python course for learning by reading and trying small
programs. Comments explain what the code does in simple words. Read them,
guess what the program will show, then run it and check your guess.

## Requirements

- Python 3
- No third-party packages

## How to study each lesson

1. Read the comments before running the program.
2. Notice what information the program asks for and what it does with it.
3. Guess what the program will show. Write down sample answers if it asks questions.
4. Run the program from the project folder and check your guess.
5. Change a value or answer and see how the result changes.
6. For exercises with commented solutions, try solving the prompt first. Then
   uncomment one solution block, keeping its indentation, and run the file.

Some lessons expect you to enter a number when asked. If you enter words instead,
Python will show an error. The comments point out where this can happen.

## Course map

### 01 Beginner

- `01_beginner/basics/` - variables, text, numbers, True/False values, and printing
- `01_beginner/calculators/` - getting numbers, doing math, and choosing an operation
- `01_beginner/games/` - comparing numbers and choosing what to do
- `01_beginner/loops/for_loops/` - repeating steps and making number patterns

### 02 Intermediate

- `02_intermediate/calculators/` - tips, bill sharing, and electricity bills
- `02_intermediate/conditionals/` - checking scores and choosing a result
- `02_intermediate/cybersecurity/` - checking access and sorting risk levels
- `02_intermediate/games/` - saving information and printing a game profile
- `02_intermediate/loops/` - counting, adding totals, and repeating steps
- `02_intermediate/simulations/` - choosing an action in a pretend ATM

### 03 Advanced

There are no advanced exercises yet. The [advanced course roadmap](03_advanced/README.md)
lists topics to study next.

## Suggested order

Start with `01_beginner/basics/`, then try the calculator and guessing game.
Next, study the beginner `for` loops before moving to the intermediate lessons.
The intermediate loop lessons add more ways to count and repeat steps.

## Running an exercise

Run a script from the project root. For example:

```bash
python 01_beginner/calculators/simple_calculator.py
```

Some programs ask you to type answers in the terminal. Most scripts run all
their examples when started. In the `while` loop lesson, remove the # marks
from an answer to run it. `number_ranges.py` runs every example in the file.

## Safety note

The login and access-checking scripts contain sample passwords in the code.
They are only for learning if-statements. Do not use them to protect real
accounts or information.
