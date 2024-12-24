# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/19

from ...base import TextSolution, answer
from functools import cache

class Solution(TextSolution):
    _year = 2024
    _day = 19

    # @answer(1234)
    def part_1(self) -> int:
        self.input = self.input.split("\n")
        self.towels = self.input[0].split(", ")
        self.towels = set(self.towels)
        self.patterns = self.input[2:]
        count = 0
        for i, pattern in enumerate(self.patterns):
            # print(f"{i + 1} out of {len(self.patterns)}")
            if self.canBeMade(pattern):
                count += 1

        return count
    
    @cache
    def canBeMade(self, pattern: str) -> bool:
        if pattern in self.towels:
            return True 
        else:
            for towel in self.towels:
                if pattern.startswith(towel):
                    if self.canBeMade(pattern[len(towel):]):
                        return True 
            return False
    
    @cache
    def howcanBeMade(self, pattern: str) -> int:
        if not pattern:
            return 1
        else:
            count = 0
            for towel in self.towels:
                if pattern.startswith(towel):
                    # print(f"current pattern: {pattern}")
                    count += self.howcanBeMade(pattern[len(towel):])
            return count

    # @answer(1234)
    def part_2(self) -> int:
        count = 0
        for i, pattern in enumerate(self.patterns):
            # print(f"{i + 1} out of {len(self.patterns)}")
            # print(f"{pattern} has {self.howcanBeMade(pattern)} ways to make")
            count += self.howcanBeMade(pattern)
        
        return count

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
