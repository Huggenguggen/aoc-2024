# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/25

from ...base import StrSplitSolution, answer
from typing import List

class Solution(StrSplitSolution):
    _year = 2024
    _day = 25
    separator = "\n\n"

    def haveOverlap(self, key: List[int], lock: List[int]) -> bool:
        """
        determines if a key and lock has overlaps

        Args:
            key (List[int]): key to compare with
            lock (List[int]): lock to compare with
        
        returns:
            bool: determining if there is overlap
        """
        for i in range(len(key)):
            if key[i] + lock[i] >= 6:
                return False 
        return True

    def convertToHeight(self, entry: List[str]) -> List[int]:
        """
        converts the str lock/key into a pin height array

        Args:
            entry (List[str]): key or lock to convert
        
        returns:
            List[int]: list representation of pin heights 
        """
        maxHeight = len(entry)
        rowLen = len(entry[0])
        res = []
        for i in range(rowLen):
            height = 0
            for j in range(maxHeight):
                if entry[j][i] == '#':
                    height += 1
            height -= 1
            res.append(height)
        return res

    # @answer(1234)
    def part_1(self) -> int:
        self.input = [entry.split("\n") for entry in self.input]
        self.heights = [[] for entry in self.input]

        keys = set()
        locks = set()
        for i, entry in enumerate(self.input):
            # print("\n".join(entry) + "\n\n")
            # convert to height
            height = self.convertToHeight(entry)
            if entry[0] == ".....":
                keys.add(tuple(height))
            else:
                locks.add(tuple(height))
        count = 0
        for lock in locks:
            for key in keys:
                if self.haveOverlap(key, lock):
                    count += 1


        return count

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
