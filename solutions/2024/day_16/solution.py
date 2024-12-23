# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/16

from ...base import CharSplitSolution, answer
from heapq import heappop, heappush

class Solution(CharSplitSolution):
    _year = 2024
    _day = 16

    @answer(90440)
    def part_1(self) -> int:
        m, n = len(self.input), len(self.input[0])

        for i in range(m):
            for j in range(n):
                if self.input[i][j] == 'S':
                    self.start = (i, j)
                elif self.input[i][j] == 'E':
                    self.end = (i, j)
        # remove the E but keep the end location
        self.input[self.end[0]][self.end[1]] = '.'

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        heap = [(0, 0, *self.start)]
        visited = set() 
        final_score = None 
        while heap:
            score, d, i, j = heappop(heap)
            if (i, j) == self.end:
                final_score = score 
                break

            if (d, i, j) in visited:
                continue 

            visited.add((d, i, j))

            x = i + directions[d][0]
            y=  j + directions[d][1]
            if self.input[x][y] == '.' and (d, x, y) not in visited:
                heappush(heap, (score + 1, d, x, y))
            
            left = (d - 1) % 4 
            if (left, i, j) not in visited:
                heappush(heap, (score + 1000, left, i, j))
            right = (d + 1) % 4
            if (right, i, j) not in visited:
                heappush(heap, (score + 1000, right, i, j))
        
        return final_score

    @answer(479)
    def part_2(self) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        heap = [(0, 0, *self.start, {self.start})]
        winning_paths = set()
        self.visited = {}
        final_score = None 
        while heap:
            score, d, i, j, path = heappop(heap)
            if final_score and final_score < score:
                break

            if (i, j) == self.end:
                final_score = score
                winning_paths |= path
                continue

            if not self.can_visit(d, i, j, score):
                continue 

            x = i + directions[d][0]
            y=  j + directions[d][1]
            if self.input[x][y] == '.' and self.can_visit(d, x, y, score+1):
                heappush(heap, (score + 1, d, x, y, path | {(x, y)}))
            
            left = (d - 1) % 4 
            if self.can_visit(left, i, j, score + 1000):
                heappush(heap, (score + 1000, left, i, j, path))
            right = (d + 1) % 4
            if self.can_visit(right, i, j, score + 1000):
                heappush(heap, (score + 1000, right, i, j, path))
        
        return len(winning_paths)

    def can_visit(self, d, i, j, score):
        prev_score = self.visited.get((d, i, j))
        if prev_score and prev_score < score:
            return False 
        self.visited[(d, i, j)] = score 
        return True
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
