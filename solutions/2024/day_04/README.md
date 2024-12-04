# Day 4 (2024)

`TITLE` ([prompt](https://adventofcode.com/2024/day/4))

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

```
..X...
.SAMX.
.A..A.
XMAS.S
.X....
```
The actual word search will be full of letters instead. For example:

```
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```


## Part 1
How many times does XMAS appear?
### Approach
- DFS? for every X just go all 8 directions and check


## Part 2
Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:
```
M.S
.A.
M.S
```
- there are 4 possible configurations
```
M.S
.A.
M.S
```
or 
```
S.M
.A.
S.M
```
or
```
M.M
.A.
S.S
```
or 
```
S.S
.A.
M.M
```
Now look for A's and check for this configuration (note you don't have to check the first line or last line)