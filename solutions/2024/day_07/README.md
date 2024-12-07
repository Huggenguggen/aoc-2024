# Day 7 (2024)

`TITLE` ([prompt](https://adventofcode.com/2024/day/7))

If only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).

For example:
```
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
```

Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.

Operators are always evaluated **left-to-right**, not according to precedence rules. Furthermore, **numbers in the equations cannot be rearranged**. Glancing into the jungle, you can see elephants holding two different types of operators: add (+) and multiply (*).

The engineers just need the total calibration result, which is the sum of the test values from just the equations that could possibly be true. In the above example, the sum of the test values for the three equations listed above is 3749.

## Part 1
Determine which equations could possibly be true. What is their total calibration result?

- normal BFS


## Part 2
Add another operator '||' which concatenates the 2 numbers

- Add another branch

Optimization:
- Only explore what failed in part 1