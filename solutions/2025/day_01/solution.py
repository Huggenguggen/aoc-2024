# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 1

    @answer(980)
    def part_1(self) -> int:
        curr = 50
        total = 100
        res = 0
        for line in self.input:
            d, x = line[0], int(line[1:])
            if d == 'R':
                curr += x
            else: # d == 'L'
                if curr > x:
                    curr -= x
                else:
                    curr = total - (x - curr)
            curr %= total
            print("Curr:", curr)
            if curr == 0:
                res += 1
        return res

    # @answer(1234)
    def part_2(self) -> int:
        steps = [int(i[1:]) * (2 * (i[0] == "R") - 1) for i in self.input]
        pos = 50
        res = 0
        for step in steps:
            div, pos, prev = *divmod(pos + step, 100), pos
            res += abs(div) - (prev == 0 and div < 0) + (pos == 0 and step < 0)
        return res 
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
