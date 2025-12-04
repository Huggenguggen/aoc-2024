# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 2
    
    def __init__(self, run_slow=False, is_debugging=False, use_test_data=False):
        self.separator = ','
        super().__init__(run_slow, is_debugging, use_test_data)
        

    @answer(40398804950)
    def part_1(self) -> int:
        res = 0
        for ran in self.input:
            start, end = list(map(int, ran.split('-')))
            for i in range(start, end + 1):
                i = str(i)
                if len(i) % 2 == 0:
                    if i[:(len(i) // 2)] == i[(len(i) // 2):]:
                        res += int(i)
        return res

    @answer(65794984339)
    def part_2(self) -> int:
        res = 0
        for ran in self.input:
            start, end = list(map(int, ran.split('-')))
            for i in range(start, end + 1):
                j = str(i)
                for length in range(1, (len(j) // 2) + 1):
                    if len(j) % length == 0:
                        if self.repeating(length, j):
                            print(i)
                            res += i
                            break 
        return res
    
    def repeating(self, length: int, i: str) -> bool:
        substr = i[:length]
        curr = length
        while curr + length <= len(i):
            if i[curr:curr+length] != substr:
                return False
            curr += length
        return True
    
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
