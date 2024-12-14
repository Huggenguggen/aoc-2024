# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/14

from ...base import StrSplitSolution, answer
import re
from typing import List 

class Solution(StrSplitSolution):
    _year = 2024
    _day = 14

    @answer(222062148)
    def part_1(self) -> int:
        quads = [0, 0, 0, 0] # LU, RU, LL, RL
        # p1FieldX = 11 # test case
        # p1FieldY = 7 # test case
        seconds = 100
        p1FieldX = 101 
        p1FieldY = 103 
        for line in self.input:
            x,y,dx,dy = map(int, re.findall(r'-?\d+', line))
            endPos = 0
            endX = (x + (dx * seconds)) % p1FieldX
            endY = (y + (dy * seconds)) % p1FieldY
            if endX + 1 == (p1FieldX + 1) / 2 or \
                endY + 1 == (p1FieldY + 1) / 2:
                continue 
            if endX > p1FieldX / 2:
                endPos = endPos + 1
            if endY > p1FieldY / 2:
                endPos = endPos + 2
            
            quads[endPos] += 1
        
        res = 1
        for quad in quads:
            res *= quad 
        return res

    @answer(7520)
    def part_2(self) -> int:
        p2FieldX = 101 
        p2FieldY = 103 
        robots = []
        for line in self.input:
            x,y,dx,dy = map(int, re.findall(r'-?\d+', line))
            robots.append([x, y, dx, dy])
        seconds = 0
        while True:
            seconds = seconds + 1
            for robot in robots:
                robot[0] = (robot[0] + robot[2]) % p2FieldX 
                robot[1] = (robot[1] + robot[3]) % p2FieldY
            self.printrobots(robots, p2FieldX, p2FieldY, seconds)

    def printrobots(self, robotspos: List, FieldX: int, FieldY: int, seconds: int):
        telltale = '**********'
        tentative = False
        fieldmap = [ ['.'] * FieldX for i in range(FieldY)]
        for printrobot in robotspos:
            fieldmap[printrobot[1]][printrobot[0]] = '*'
        for line in fieldmap:
            picstring = "".join(line)
            if picstring.count(telltale) > 0:
                tentative = True
        if tentative:
            for line in fieldmap:
                picstring = "".join(line)
                print(picstring)
            print("After {:d} seconds ".format(seconds))
            exit(0)


    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
