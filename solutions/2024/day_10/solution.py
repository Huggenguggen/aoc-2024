# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/10

from ...base import CharSplitSolution, answer
from collections import deque

class Solution(CharSplitSolution):
    _year = 2024
    _day = 10

    @answer(624)
    def part_1(self) -> int:
        count = 0
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        self.input = [[int(x) for x in row] for row in self.input]
        for i in range(len(self.input)):
            for j in range(len(self.input[0])):
                if self.input[i][j] == 0:
                    count += len(self.bfs(i, j, 1))

        return count

    def bfs(self, i: int, j: int, part: int = 1):
        q = deque()
        q.append((i, j))
        reached = set()
        total = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                if self.input[x][y] == 9:
                    reached.add((x, y))
                    total += 1
                    continue 
                for dx, dy in self.directions:
                    nextX, nextY = dx + x, dy + y 
                    if nextX in range(0, len(self.input)) \
                        and nextY in range(0, len(self.input[0])) \
                            and self.input[nextX][nextY] == self.input[x][y] + 1:
                        q.append((nextX,nextY))
    
        return reached if part == 1 else total

    @answer(1483)
    def part_2(self) -> int:
        count = 0
        for i in range(len(self.input)):
            for j in range(len(self.input[0])):
                if self.input[i][j] == 0:
                    count += self.bfs(i, j, 2)
        return count 
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
