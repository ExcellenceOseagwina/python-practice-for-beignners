# While-loop practice

This folder contains the current while-loop practice set in [counting.py](counting.py).

## How to use the exercises

The file contains 25 exercises arranged from basic counting to nested loops and number problems. Because the examples are currently kept in one script, running the whole file executes every exercise in order. Some exercises request keyboard input.

For focused practice:

1. Open `counting.py` in your editor.
2. Find the exercise number using the comments (for example, `Exercise 5 of 25`).
3. Temporarily select and run only that exercise, or copy the exercise into a separate scratch file.
4. Predict the output before running it.
5. Try the task yourself before looking at the example solution.
6. Test boundary cases, such as 0, 1, negative values, and values at the loop limit where they apply.

Do not run the complete file when you only want to practise one interactive exercise: later exercises may wait for additional input.

## Concepts covered

| Exercises | Main concepts |
| --- | --- |
| 1–4 | Counters, loop conditions, countdowns, and running totals |
| 5–10 | Multiplication tables, divisibility, validation, accumulators, and averages |
| 11–15 | Loop termination, skipping iterations, sentinel values, and conditional totals |
| 16–20 | Nested loops, grids, triangles, multiplication tables, and number pairs |
| 21–25 | Factorials, prime checking, maximum values, digit counting, and nested-loop search |

## Important learning notes

- A `while` loop needs a condition that can eventually become false.
- Update the loop-control variable on every path through the loop. Otherwise, an infinite loop may occur.
- Initialize counters and accumulators before the loop.
- In nested loops, reset the inner-loop counter each time the outer loop starts another iteration.
- `break` exits the nearest enclosing loop; `continue` skips to its next iteration.
- The examples are educational exercises, not production-ready input-processing utilities.

## Known scope

The file intentionally demonstrates several different approaches, including `break` and `continue`. If you have not studied a construct yet, skip that exercise and return to it later. The exercises do not require third-party packages.
