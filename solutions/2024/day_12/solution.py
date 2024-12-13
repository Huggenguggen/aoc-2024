# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/12

from ...base import CharSplitSolution, answer
from collections import deque
from typing import Tuple

class Solution(CharSplitSolution):
    _year = 2024
    _day = 12

    @answer(1473620)
    def part_1(self) -> int:
        self.seen = set()
        total = 0
        for i in range(len(self.input)):
            for j in range(len(self.input[0])):
                if (i, j) in self.seen:
                    continue 
                area, perimeter = self.bfs(i, j, self.input[i][j])
                # print(f"Crop: {self.input[i][j]}, Area: {area}, Perimeter: {perimeter}")
                total += area * perimeter
        return total

    def bfs(self, i: int, j: int, crop: str) -> Tuple[int, int]:
        visited = set()
        area = 0
        perimeter = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque([(i, j)])
        while q:
            for _ in range(len(q)):
                currX, currY = q.popleft()
                if self.input[currX][currY] == crop and not (currX, currY) in visited:
                    visited.add((currX, currY))
                    area += 1
                    perimeter += 4
                    for dx, dy in directions:
                        if (currX + dx, currY + dy) in visited:
                            perimeter -= 2
                        else:
                            if (currX + dx) in range(0, len(self.input))\
                                  and (currY + dy) in range(0, len(self.input[0])):
                                q.append((currX + dx, currY + dy))
                else:
                    continue
        self.seen |= visited
        return (area, perimeter)

    @answer(902620)
    def part_2(self) -> int:
        visited = set()
        total = 0
        for i in range(len(self.input)):
            for j in range(len(self.input[0])):
                if (i, j) in visited:
                    continue 
                area, perimeter, corner = self.bfs2(i, j, self.input[i][j], visited)
                # print(f"Crop: {self.input[i][j]}, Area: {area}, Perimeter: {perimeter}")
                total += area * corner
        return total        


    def grid_val(self, i, j):
        if i in range(0, len(self.input)) and j in range(0, len(self.input[0])):
            return self.input[i][j]
        else:
            return ' '

    def bfs2(self, i: int, j: int, crop: str, visited: set) -> Tuple[int, int, int]:
        area = 1
        perim = 0
        corners = 0
        visited.add((i,j))

        # get neighbors
        ch_up = self.grid_val(i-1, j)
        ch_down = self.grid_val(i+1, j)
        ch_left = self.grid_val(i, j-1)
        ch_right = self.grid_val(i, j+1)

        # perimeter
        if ch_up != crop:
            perim += 1
        if ch_down != crop:
            perim += 1
        if ch_left != crop:
            perim += 1
        if ch_right != crop:
            perim += 1

        # corners
        if ch_up != crop and ch_right != crop:
            corners += 1
        if ch_right != crop and ch_down != crop:
            corners += 1
        if ch_down != crop and ch_left != crop:
            corners += 1
        if ch_left != crop and ch_up != crop:
            corners += 1

        # 'negative' corners
        if self.grid_val(i-1, j-1) != crop and ch_up == crop and ch_left == crop:
            corners += 1
        if self.grid_val(i-1, j+1) != crop and ch_up == crop and ch_right == crop:
            corners += 1
        if self.grid_val(i+1, j+1) != crop and ch_down == crop and ch_right == crop:
            corners += 1
        if self.grid_val(i+1, j-1) != crop and ch_down == crop and ch_left == crop:
            corners += 1
            
        if ch_up == crop and not (i-1,j) in visited:
            a, p, c = self.bfs2(i-1,j,crop,visited)
            area += a
            perim += p
            corners += c
        if ch_down == crop and not (i+1,j) in visited:
            a, p, c = self.bfs2(i+1,j,crop,visited)
            area += a
            perim += p
            corners += c
        if ch_left == crop and not (i,j-1) in visited:
            a, p, c = self.bfs2(i,j-1,crop,visited)
            area += a
            perim += p
            corners += c
        if ch_right == crop and not (i,j+1) in visited:
            a, p, c = self.bfs2(i,j+1,crop,visited)
            area += a
            perim += p
            corners += c
        return([area, perim, corners])
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
