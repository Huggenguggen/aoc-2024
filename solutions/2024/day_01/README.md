# Day 1 (2024)

`Day 1: Historian Hysteria` ([prompt](https://adventofcode.com/2024/day/1))

Throughout the Chief's office, the historically significant locations are listed not by name but by a unique number called the location ID. To make sure they don't miss anything, The Historians split into two groups, each searching the office and trying to create their own complete list of location IDs.

There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?

For example:

```
3   4
4   3
2   5
1   3
3   9
3   3
```

Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

What is the total distance between your lists?

## Part 1
What is the total distance between your lists?
### Approach
- Sort both list1 and list2
- iterate through and find distance adding to total

## Part 2
a lot of location IDs appear in both lists! Maybe the other numbers aren't location IDs at all but rather misinterpreted handwriting.

This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

### Approach
NAIVE
- Process list1 first to make a frequency hashtable (default 0)
- increment for each appearence in list2
- go through hashtable to find similarity score

Optimal
- make a set for numbers that appear in list1
- if number doesn't appear in list2, don't add
- else add