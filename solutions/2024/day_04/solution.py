# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from ...base import CharSplitSolution, answer


class Solution(CharSplitSolution):
    _year = 2024
    _day = 4

    # @answer(1234)
    def part_1(self) -> int:
        xmas = ['X', 'M', 'A', 'S']
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        total_xmas = 0
        for i in range(len(self.input)):
            for j in range(len(self.input[0])):
                if self.input[i][j] == 'X':
                    for dx, dy in directions:
                        ptr = 0
                        currX, currY = i, j
                        while self.input[currX][currY] == xmas[ptr]:
                            if self.input[currX][currY] == xmas[-1]:
                                total_xmas += 1
                                break
                            ptr += 1
                            currX += dx 
                            currY += dy   
                            if not currX in range(0, len(self.input)) or not currY in range(0, len(self.input[0])):
                                break 
        return total_xmas  
                        
            

    # @answer(1234)
    def part_2(self) -> int:
        total_xmas = 0
        for i in range(1, len(self.input) - 1):
            for j in range(1, len(self.input[0]) - 1):
                if self.input[i][j] == 'A':
                    if self.checkCross(i, j):
                        total_xmas += 1
        return total_xmas
    
    def checkCross(self, i: int, j: int) -> bool:
        # there are 4 combi
        combiOne = self.input[i - 1][j - 1] == 'M' and \
                   self.input[i - 1][j + 1] == 'S' and \
                   self.input[i + 1][j - 1] == 'M' and \
                   self.input[i + 1][j + 1] == 'S'
        combiTwo = self.input[i - 1][j - 1] == 'S' and \
                   self.input[i - 1][j + 1] == 'M' and \
                   self.input[i + 1][j - 1] == 'S' and \
                   self.input[i + 1][j + 1] == 'M'
        combiThree = self.input[i - 1][j - 1] == 'M' and \
                  self.input[i - 1][j + 1] == 'M' and \
                  self.input[i + 1][j - 1] == 'S' and \
                  self.input[i + 1][j + 1] == 'S'
        combiFour = self.input[i - 1][j - 1] == 'S' and \
                   self.input[i - 1][j + 1] == 'S' and \
                   self.input[i + 1][j - 1] == 'M' and \
                   self.input[i + 1][j + 1] == 'M'
        return combiOne or combiTwo or combiThree or combiFour

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
