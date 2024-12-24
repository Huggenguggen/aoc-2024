# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/18

from ...base import StrSplitSolution, answer
from typing import List
from ...utils.graph import generate2DGraph, print2DGraph, dijkstra2D
from collections import deque

class Solution(StrSplitSolution):
    _year = 2024
    _day = 18

    def generateGraph(self, rows: int, cols: int, nanoseconds: int) -> List[List[str]]:
        graph = [["." for _ in range(cols + 1)] for _ in range(rows + 1)]
        for i in range(nanoseconds):
            x, y = self.input[i]
            print(self.input[i])
            graph[y][x] = "#"
        return graph

    def bfs(self, _map, size):
        # matrix_of_shortest_paths = [[0 for _ in range(size + 1)] for _ in range(size + 1)]
        queue = deque()
        queue.append((0, 0, 0))
        visited = set()
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            x, y, length = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))

            if (x, y) == (size, size):
                return length
            for move in moves:
                if 0 <= x + move[0] <= size and 0 <= y + move[1] <= size and _map[x + move[0]][y + move[1]] == ".":
                    queue.append((x + move[0], y + move[1], length + 1))

    @answer(252)
    def part_1(self) -> int:
        if self.use_test_data:
            size = 6
            corrupted = 12
        else:
            size = 70
            corrupted = 1024
        self.input = [[int(x) for x in row.split(",")] for row in self.input]
        graph = generate2DGraph(rows=size, cols=size, \
                                    clear=".", obstacle="#", \
                                        obstacles=self.input[:corrupted])
        print2DGraph(graph)

        return self.bfs(graph, size)
    @answer("5,60")
    def part_2(self) -> int:
        if self.use_test_data:
            size = 6
            corrupted = 12
        else:
            size = 70
            corrupted = 1024
        graph = generate2DGraph(rows=size, cols=size, \
                                    clear=".", obstacle="#", \
                                        obstacles=self.input)

        print2DGraph(graph)

        for i in range(len(self.input) - 1, corrupted, -1):
            newX, newY = self.input[i]
            graph[newY][newX] = "."
            result = self.bfs(graph, size)
            if result is not None:
                return ",".join([str(x) for x in self.input[i]])
        return None
    
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
