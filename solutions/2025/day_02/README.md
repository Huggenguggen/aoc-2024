# Day 2 (2025)

`Gift Shop` ([prompt](https://adventofcode.com/2025/day/2))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1

Given a list of ranges, make sure that any number included in the ranges are not **invalid**

Invalid means number repeated twice like 55, 6464, 123123

Go through all the ranges,
Iterate through -> if num[:half] == num[half:] then add to sum

## Part 2

now an ID is invalid if it is made only of some sequence of digits repeated **at least** twice. 

e.g. 123411234, 123123123, 1212121212, 11111

brute force up to half the length of the digit if it is repeating

