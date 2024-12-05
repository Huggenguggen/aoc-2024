# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

from ...base import answer, TextSolution
import re

class Solution(TextSolution):
    _year = 2024
    _day = 3

    @answer(190604937)
    def part_1(self) -> int:
        matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", self.input)        
        total = 0
        for first, second in matches:
            total += int(first) * int(second)
        
        return total 

    @answer(82857512)
    def part_2(self) -> int:
        matches = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\)))", self.input)        
        isDo = True 
        total = 0
        for match in matches:
            if match[0] == "don't()":
                isDo = False 
            elif match[0] == "do()":
                isDo = True 
            elif isDo:
                total += int(match[1]) * int(match[2])                

        return total

    @answer(190604937)
    def part_1_slow(self) -> int:
        indexes = [i for i, ltr in enumerate(self.input) if ltr=='m']
        total = 0
        for i in indexes:
            if i < len(self.input) - 7:
                if self.input[i+1] != 'u' \
                    or self.input[i+2] != 'l' \
                    or self.input[i+3] != '(':
                    continue 
                
                # so at least it is 'mul('
                base = curr = i + 4
                invalid = False
                while self.input[curr] != ',':
                    if not self.input[curr].isnumeric() or curr - base > 3:
                        invalid = True 
                        break 
                    # it is numeric and curr is still less than 3
                    curr += 1
                if self.input[curr] != ',':
                    if self.input[curr + 1] != ',':
                        invalid = True 
                    curr += 1
                if invalid: continue
                firstNum = int(self.input[base:curr])
                curr += 1
                base = curr 
                while self.input[curr] != ')':
                    if not self.input[curr].isnumeric() or curr - base > 3:
                        invalid = True 
                        break 
                    curr += 1
                if self.input[curr] != ')':
                    if self.input[curr + 1] != ')':
                        invalid = True 
                    curr += 1
                if invalid: continue 
                secondNum = int(self.input[base:curr])
                total += firstNum * secondNum
        return total
    
    def part_2_slow(self) -> int:
        indexes = [i for i, ltr in enumerate(self.input) if ltr=='m']
        donts = [i for i in range(len(self.input)) if self.input.startswith("don't()", i)]
        do = [-1] + [i for i in range(len(self.input)) if self.input.startswith("do()", i)]
        events = [(point, 'deactivate') for point in donts] + [(point, 'activate') for point in do]
        events.sort()
        active = False
        active_ranges = []
        current_start = None

        for point, event in events:
            if event == 'activate':
                if not active:  # Start a new active range
                    current_start = point
                active = True
            elif event == 'deactivate':
                if active:  # End the current active range
                    active_ranges.append((current_start, point))
                active = False 
        
        if active:  # If still active at the end
            active_ranges.append((current_start, float('inf')))

        collapsed = []
        for idx in indexes:
            for start, end in active_ranges:
                if start <= idx < end:
                    collapsed.append(idx)
                    break 
        total = 0
        for i in collapsed:
            if i < len(self.input) - 7:
                if self.input[i+1] != 'u' \
                    or self.input[i+2] != 'l' \
                    or self.input[i+3] != '(':
                    continue 
                
                # so at least it is 'mul('
                base = curr = i + 4
                invalid = False
                while self.input[curr] != ',':
                    if not self.input[curr].isnumeric() or curr - base > 3:
                        invalid = True 
                        break 
                    # it is numeric and curr is still less than 3
                    curr += 1
                if self.input[curr] != ',':
                    if self.input[curr + 1] != ',':
                        invalid = True 
                    curr += 1
                if invalid: continue
                firstNum = int(self.input[base:curr])
                curr += 1
                base = curr 
                while self.input[curr] != ')':
                    if not self.input[curr].isnumeric() or curr - base > 3:
                        invalid = True 
                        break 
                    curr += 1
                if self.input[curr] != ')':
                    if self.input[curr + 1] != ')':
                        invalid = True 
                    curr += 1
                if invalid: continue 
                secondNum = int(self.input[base:curr])
                total += firstNum * secondNum
        return total
            

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
