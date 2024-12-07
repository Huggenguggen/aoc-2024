# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/7

from ...base import StrSplitSolution, answer
from typing import List
from collections import deque

class Solution(StrSplitSolution):
    _year = 2024
    _day = 7

    def isValid(self, equation: List, part: int) -> bool:
        total = equation[0]
        q = deque([(0, equation[1][0])]) #currIndex + currTotal
        while q:
            # print("currQ:", q)
            for _ in range(len(q)):
                currIdx, currTotal = q.popleft()
                if currTotal == total and currIdx == len(equation[1]) - 1:
                    return True 
                if currTotal > total:
                    continue
                if currIdx == len(equation[1]) - 1:
                    continue
                q.append((currIdx + 1, equation[1][currIdx + 1] * currTotal))
                q.append((currIdx + 1, equation[1][currIdx + 1] + currTotal))
                if part == 2:
                    q.append((currIdx + 1, int(f"{currTotal}{equation[1][currIdx + 1]}")))
        return False
    
    @answer(2299996598890)
    def part_1(self) -> int:
        total = 0
        self.part1Passed = set()
        self.equations = [x.split(":") for x in self.input]
        self.equations = [(int(x[0]), tuple(map(lambda num: int(num), x[1].split(" ")[1:]))) for x in self.equations]
        for equation in self.equations:
            if self.isValid(equation, 1):
                self.part1Passed.add(equation)
                # print("equation:", equation)
                total += equation[0]
        return total
    
    @answer(362646859298554)
    def part_2(self) -> int:
        total = 0
        for equation in self.equations:
            if equation in self.part1Passed:
                total += equation[0]
            elif self.isValid(equation, part=2):
                total += equation[0]
        return total

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
