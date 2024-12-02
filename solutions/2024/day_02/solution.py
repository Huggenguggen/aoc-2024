# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from ...base import StrSplitSolution, answer
from typing import List

class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    @answer(279)
    def part_1(self) -> int:
        safe = 0
        for line in self.input:
            line = [int(x) for x in line.split(" ")]
            # first check if inc or dec
            isIncreasing = None
            if line[0] < line[1]:
                isIncreasing = True 
            elif line[1] < line[0]:
                isIncreasing = False 
            else:
                # unsafe
                continue
            if self.part1Safe(line, isIncreasing):
                safe += 1
        return safe 

    def part1Safe(self, line: List[int], isIncrease: bool) -> bool:
        if isIncrease:
            for i in range(len(line) - 1):
                if line[i] >= line[i + 1] or \
                    line[i] < (line[i + 1] - 3):
                    return False
        
            return True 
        else: # decreasing
            for i in range(len(line) - 1):
                if line[i] <= line[i + 1] or \
                    line[i + 1] < (line[i] - 3):
                    return False
        
            return True

    @answer(343)
    def part_2(self) -> int:
        safe = 0
        for line in self.input:
            line = [int(x) for x in line.split(" ")]
            if self.part2Safe(line) or \
                any(self.part2Safe(line[:i] + line[i + 1:]) \
                    for i in range(len(line))):
                safe += 1
        return safe 

    def part2Safe(self, line: List[int]) -> bool:
        diffs = [abs(curr - prev) for prev, curr in zip(line[:-1], line[1:])]
        isInc = all(i < j for i,j in zip(line[:-1], line[1:]))
        isDec = all(i > j for i,j in zip(line[:-1], line[1:]))

        isDiff = all(d in (1,2,3) for d in diffs)
        return (isDec or isInc) and isDiff

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
