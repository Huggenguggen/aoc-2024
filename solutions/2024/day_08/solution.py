# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/8

from ...base import CharSplitSolution, answer
from collections import defaultdict
from typing import Tuple

class Solution(CharSplitSolution):
    _year = 2024
    _day = 8

    def calculateAntiNodes(self, first: Tuple[int, int], second: Tuple[int, int])\
          -> Tuple[Tuple[int, int], Tuple[int, int]]:
        dx = first[0] - second[0]
        dy = first[1] - second[1]
        return ((first[0] + dx, first[1] + dy), (second[0] - dx, second[1] - dy))

    def calculateAntiNodes2(self, first: Tuple[int, int], second: Tuple[int, int]) -> None:
        dx = first[0] - second[0]
        dy = first[1] - second[1]

        self.antinodes.add(first)
        self.antinodes.add(second)

        currX, currY = first[0] + dx, first[1] + dy 
        while self.valid((currX, currY)):
            self.antinodes.add((currX, currY))
            currX += dx 
            currY += dy 
        
        currX, currY = second[0] - dx, second[1] - dy 
        while self.valid((currX, currY)):
            self.antinodes.add((currX, currY))
            currX -= dx 
            currY -= dy


    def valid(self, antinode: Tuple[int, int]):
        return antinode[0] in range(self.rowLen) and antinode[1] in range(self.colLen)
    # @answer(1234)
    def part_1(self) -> int:
        self.rowLen = len(self.input)
        self.colLen = len(self.input[0])
        self.antenna = defaultdict(list)
        for i in range(self.rowLen):
            for j in range(self.colLen):
                if self.input[i][j] == '.':
                    continue
                self.antenna[self.input[i][j]].append((i, j))
        
        self.antinodes = set()

        for k, positions in self.antenna.items():
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    first, second = self.calculateAntiNodes(positions[i], positions[j])
                    if self.valid(first):
                        self.antinodes.add(first)
                    if self.valid(second):
                        self.antinodes.add(second)
        return len(self.antinodes)
    
    # @answer(1234)
    def part_2(self) -> int:
        for k, positions in self.antenna.items():
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    self.calculateAntiNodes2(positions[i], positions[j])
        
        return len(self.antinodes)
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
