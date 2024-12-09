# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/9

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2024
    _day = 9

    @answer(6258319840548)
    def part_1(self) -> int:
        self.input = list(map(lambda x: int(x), list(self.input)))
        self.intermediate = []
        index = 0
        for i,v in enumerate(self.input):
            if i % 2 == 0:
                self.intermediate.extend([index] * v)
                index += 1
            else:
                self.intermediate.extend(['.'] * v)
        
        front = 0
        back = len(self.intermediate) - 1

        while front < back:
            while self.intermediate[front] != '.':
                front += 1
            while self.intermediate[back] == '.':
                back -= 1
            
            # swap front and back 
            self.intermediate[front] = self.intermediate[back]
            self.intermediate[back] = '.'
            front += 1
            back -= 1
        
        checksum = 0
        for i, v in enumerate(self.intermediate):
            if v == '.':
                return checksum 
            else:
                checksum += i * v

        return checksum

    @answer(6286182965311)
    def part_2(self) -> int:
        self.indexes = []
        self.blanks = []
        index = 0
        self.intermediate = []
        for i, v in enumerate(self.input):
            if i % 2 == 0:
                self.indexes.append([index, len(self.intermediate), v])
                self.intermediate.extend([index] * v)
                index += 1
            else:
                self.blanks.append([len(self.intermediate), v])
                self.intermediate.extend(['.'] * v)
            
        # print(self.intermediate)
        # print("blanks:", self.blanks)
        for i in range(len(self.indexes) - 1, -1, -1):
            print(f"{-1 * (i - len(self.indexes))} out of {len(self.indexes)} complete: {(-1*(i - len(self.indexes)) / len(self.indexes)) * 100}")
            value, index, length = self.indexes[i]
            for j in range(len(self.blanks)):
                blankIdx, blankLength = self.blanks[j]  
                if length <= blankLength and blankIdx < index:
                    for k in range(length):
                        self.intermediate[blankIdx + k] = value 
                        self.intermediate[index + k] = '.'
                    self.blanks = []
                    k = 0
                    while k < len(self.intermediate) - 1:
                        v = self.intermediate[k]
                        if v == '.':
                            count = 0
                            while self.intermediate[k] == '.' and k < len(self.intermediate) - 1:
                                count += 1
                                k += 1
                            self.blanks.append([k - count, count])
                        k += 1
                    break
                elif blankIdx > index:
                    break
                else:
                    continue
            # print("Blanks: ", self.blanks)
            # print("Intermediate: ", self.intermediate) 
        
        checksum = 0
        for i, v in enumerate(self.intermediate):
            if v == '.':
                continue 
            else:
                checksum += i * v

        return checksum

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
