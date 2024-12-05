# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/5

from ...base import StrSplitSolution, answer
from collections import defaultdict
from typing import List

class Solution(StrSplitSolution):
    _year = 2024
    _day = 5

    # @answer(1234)
    def part_1(self) -> int:
        pageBreak = self.input.index('')
        self.rules = self.input[:pageBreak]
        self.updates = self.input[pageBreak + 1:]
        self.ruleBook = defaultdict(list)
        for rule in self.rules:
            k, v = rule.split("|")
            self.ruleBook[k].append(v)
        total = 0
        for update in self.updates:
            update = update.split(",")
            if self.isValid(update):
                total += int(update[(len(update) // 2)])
        

        return total

    def isValid(self, update: List[str]) -> bool:
        seen = set()
        for page in update:
            rules = self.ruleBook[page]
            seen.add(page)
            for post in rules:
                if post in seen:
                    return False 
        return True

    # @answer(1234)
    def part_2(self) -> int:
        total = 0
        for update in self.updates:
            update = update.split(",")
            if not self.isValid(update):
                self.fixUpdate(update) 
                middle = int(update[(len(update) // 2)])
                total += middle
        return total 
    
    def fixUpdate(self, update: List[str]) -> None:
        seen = defaultdict(int)
        for i, page in enumerate(update):
            rules = self.ruleBook[page]
            seen[page] = i
            for post in rules:
                if post in seen:
                    update[i], update[seen[post]] = update[seen[post]], update[i]
                    break 
        if not self.isValid(update):
            self.fixUpdate(update) 
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
