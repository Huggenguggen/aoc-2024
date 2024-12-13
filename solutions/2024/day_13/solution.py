# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/13
from ...base import StrSplitSolution, answer
from itertools import groupby
from typing import List, Tuple
import heapq

class Solution(StrSplitSolution):
    _year = 2024
    _day = 13
 
    def getPrize(self, A: List[int], \
                        B: List[int], \
                          prize: List[int]) -> Tuple[bool, int]:
        # perform bfs with pq
        pq = [(0, 0, 0)] # (cost, x, y)
        visited = set()
        heapq.heapify(pq)
        while pq:
            currCost, currX, currY = heapq.heappop(pq)
            if (currX, currY) in visited \
                or currX > prize[0] or currY > prize[1]:
                continue 
            visited.add((currX, currY))
            if currX == prize[0] and currY == prize[1]:
                return True, currCost 
            # add
            heapq.heappush(pq, (currCost + 3, currX + A[0], currY + A[1]))
            heapq.heappush(pq, (currCost + 1, currX + B[0], currY + B[1]))
        return False, -1
    
    @answer(35255)
    def part_1(self) -> int:
        self.games = (list(g) for k,g in groupby(self.input, key=lambda x: x != '') if k)
        total = 0
        self.As, self.Bs, self.prizes = [], [], []
        for game in self.games:
            A = game[0].split(": ")[1].split(", ")
            A[0], A[1] = int(A[0][2:]), int(A[1][2:])
            self.As.append(A)
            B = game[1].split(": ")[1].split(", ")
            B[0], B[1] = int(B[0][2:]), int(B[1][2:])
            self.Bs.append(B)
            prize = game[2].split(": ")[1].split(", ")
            prize[0], prize[1] = int(prize[0][2:]), int(prize[1][2:])
            self.prizes.append(prize)
            getPrize, cost = self.getPrizeFast(A, B, prize)
            if getPrize:
                total += cost
        return total

    def getPrizeFast(self, A: List[int], \
                        B: List[int], \
                          prize: List[int]) -> Tuple[bool, int]:
        denom = A[0] * B[1] - B[0] * A[1]
        X = (prize[0] * B[1] - B[0] * prize[1]) / denom
        Y = (A[0] * prize[1] - prize[0] * A[1]) / denom 
        if X.is_integer() and Y.is_integer():
            return True, int(X*3 + Y)
        
        return False, -1

    @answer(87582154060429)
    def part_2(self) -> int:
        total = 0
        self.prizes = [[x + 10000000000000, y + 10000000000000] for x, y in self.prizes]
        for i in range(len(self.As)):
            getPrize, cost = self.getPrizeFast(self.As[i], self.Bs[i], self.prizes[i])
            if getPrize:
                # print(f"{i+1}'th prize can be found")
                total += cost
        return total

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
