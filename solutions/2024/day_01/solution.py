# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer(2113135)
    def part_1(self) -> int:
        l1 = []
        l2 = []
        for line in self.input:
            x1, x2 = map(lambda x: int(x), line.split())
            l1.append(x1)
            l2.append(x2)
        
        l1.sort()
        l2.sort()
        total = 0
        for i, v in enumerate(l1):
            total += abs(v - l2[i])
        return total

    # @answer(1234)
    def part_2(self) -> int:
        l1 = set()
        l2 = []
        for line in self.input:
            x1, x2 = map(lambda x: int(x), line.split())
            l1.add(x1)
            l2.append(x2)
        total = 0
        for num in l2:
            if num not in l1:
                total -= num
            total += num
        return total
    
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
