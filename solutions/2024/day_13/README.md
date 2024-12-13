# Day 13 (2024)

`Claw Contraption` ([prompt](https://adventofcode.com/2024/day/13))

The claw machines here are a little unusual. Instead of a joystick or directional buttons to control the claw, these machines have two buttons labeled A and B. Worse, you can't just put in a token and play; it costs 3 tokens to push the A button and 1 token to push the B button.

ith a little experimentation, you figure out that each machine's buttons are configured to move the claw a specific amount to the right (along the X axis) and a specific amount forward (along the Y axis) each time that button is pressed.

Each machine contains one prize; to win the prize, the claw must be positioned exactly above the prize on both the X and Y axes.

You wonder: what is the smallest number of tokens you would have to spend to win as many prizes as possible? You assemble a list of every machine's button behavior and prize location (your puzzle input). For example:
```
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
```

## Part 1
You estimate that each button would need to be pressed no more than 100 times to win a prize. How else would someone be expected to play?

Figure out how to win as many prizes as possible. What is the fewest tokens you would have to spend to win all possible prizes?
### Approach
For each prize, you do a BFS with pq (djikstra) noting that pushing B is 1 and pushing A is 3. If any of the 2 axis are more than the target, can stop adding since it only goes up

## Part 2
Ok now with the larger input we cannot use BFS
### Approach
- note that this is a SLE
- number of A presses is x and number of B presses is y
- So we can say that for the first example:

```
94x + 22y = X
34x + 67y = Y
```

We can now solve explicitly for x and y using [Cramer's rule](https://en.wikipedia.org/wiki/Cramer%27s_rule#Applications)

Cramer's rule states
```
For a system with 
a_1 x + b_1 y = c_1
a_2 x + b_2 y = c_2

Assuming that a_1*b_2 - b_1*a_2 is nonzero (i.e. not symmetrical)
```
x = $\frac{c_1b_2 - b_1c_2}{a_1b_2 - b_1a_2}$  
and 
y = $\frac{a_1c_2 - c_1a_2}{a_1b_2 - b_1a_2}$