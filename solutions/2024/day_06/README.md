# Day 6 (2024)

`Guard Gallivant` ([prompt](https://adventofcode.com/2024/day/6))

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
```
This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent)
By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path.


## Part 1
Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?

### Approach
- Simulate the guard's path one direction at a time until exit
  
## Part 2
Fortunately, they are pretty sure that adding a single new obstruction won't cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get stuck in a loop, making the rest of the lab safe to search.

To have the lowest chance of creating a time paradox, The Historians would like to know all of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

### Approach
- Intuition for brute force:
  - obstace has to be on the path
  - so we can just try each point on the path and add an obstacle there one by one,
  - if it hits a loop, we count it, else it should exit eventually


