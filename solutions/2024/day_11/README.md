# Day 11 (2024)

`Plutonian Pebbles` ([prompt](https://adventofcode.com/2024/day/11))

At first glance, they seem like normal stones: they're arranged in a perfectly straight line, and each stone has a number engraved on it.

The strange part is that every time you blink, the stones change.

Sometimes, the number engraved on a stone changes. Other times, a stone might split in two, causing all the other stones to shift over a bit to make room in their perfectly straight line.

As you observe them for a while, you find that the stones have a consistent behavior. Every time you blink, the stones each simultaneously change according to the first applicable rule in this list:

1. If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
2. If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
3. If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

No matter how the stones change, their order is preserved, and they stay on their perfectly straight line.

If you have an arrangement of five stones engraved with the numbers `0 1 10 99 999` and you blink once, the stones transform as follows:

The first stone, 0, becomes a stone marked 1.
The second stone, 1, is multiplied by 2024 to become 2024.
The third stone, 10, is split into a stone marked 1 followed by a stone marked 0.
The fourth stone, 99, is split into two stones marked 9.
The fifth stone, 999, is replaced by a stone marked 2021976.
So, after blinking once, your five stones would become an arrangement of seven stones engraved with the numbers `1 2024 1 0 9 9 2021976`.

## Part 1
Consider the arrangement of stones in front of you. How many stones will you have after blinking 25 times?

### Approach
- Use a linked list structure?
- allows in place changing

## Part 2
How many stones would you have after blinking a total of 75 times?

- same as above? might explode in complexity
- It did so instead note that order does not matter
- We can just solve it stone by stone
- Also note we can cache results using functools.cache