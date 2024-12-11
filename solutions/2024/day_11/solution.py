# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/11

from ...base import IntSplitSolution, answer
from ...utils.linkedlist import ListNode
from functools import cache
from typing import List

class Solution(IntSplitSolution):
    _year = 2024
    _day = 11
    separator = " "

    @answer(217443)
    def part_1(self) -> int:
        self.stones = ListNode() # default -1 is invalid
        curr = self.stones
        for num in self.input:
            curr.next = ListNode(num)
            curr = curr.next 
        
        # hard code the number of iterations
        for _ in range(25):
            # print(self.stones)
            curr = self.stones.next
            while curr != None:
                if curr.data == 0:
                    curr.data = 1
                elif len(str(curr.data)) % 2 == 0:
                    num = str(curr.data)
                    numLength = len(num)
                    first = num[:(numLength // 2)]
                    second = num[(numLength // 2):]
                    curr.data = int(first)
                    tmp = curr.next 
                    curr.next = ListNode(int(second))
                    curr = curr.next 
                    curr.next = tmp 
                else:
                    curr.data = curr.data * 2024
                curr = curr.next
        
        count = 0
        curr = self.stones.next 
        while curr != None:
            count += 1
            curr = curr.next 
        return count

    def expand_value(self, value: int) -> List[int]:
        if value == 0:
            return [1]
        
        text = str(value)
        length = len(text)
        if length % 2 == 0:
            i = length // 2
            a = int(text[:i])
            b = int(text[i:])
            return [a, b]
        
        return [value * 2024]

    @cache
    def count_stones(self, value: int, count: int) -> int:
        if count == 0:
            return 1
        values = self.expand_value(value)
        return sum(self.count_stones(x, count - 1) for x in values)

    # @answer(1234)
    def part_2(self) -> int:
        return sum(self.count_stones(x, 75) for x in self.input)
    


    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
