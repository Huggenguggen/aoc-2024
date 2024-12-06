# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from ...base import CharSplitSolution, answer
import json

class Solution(CharSplitSolution):
    _year = 2024
    _day = 6

    @answer(4663)
    def part_1(self) -> int:
        # first find the first position of the guard
        curr_pos = (None, None)
        curr_direction = None
        self.seen = set()
        self.directions = {
            "^": (-1, 0),
            ">": (0, 1),
            "v": (1, 0),
            "<": (0, -1)
        }
        self.change = {
            "^": ">",
            ">": "v",
            "v": "<",
            "<": "^"
        }
        for i in range(len(self.input)):
            for j in range(len(self.input[0])):
                if self.input[i][j] == '^':
                    self.start_pos = (i, j)
                    curr_pos = (i, j)
                    curr_direction = self.input[i][j]
                    self.seen.add((i, j))
        
        while curr_pos[0] in range(0, len(self.input)) and \
            curr_pos[1] in range(0, len(self.input[0])):
            dx, dy = self.directions[curr_direction]
            next_x = curr_pos[0] + dx 
            next_y = curr_pos[1] + dy
            # print((next_x, next_y))
            if (next_x in range(0, len(self.input)) and 
                next_y in range(0, len(self.input[0]))) and self.input[next_x][next_y] == '#':
                curr_direction = self.change[curr_direction] 
            elif (next_x in range(0, len(self.input)) and 
                next_y in range(0, len(self.input[0]))):
                self.seen.add((next_x, next_y))
                curr_pos = (next_x, next_y) 
            else:
                return len(self.seen)




    @answer(1530)
    def part_2(self) -> int:
        loop_count = 0
        is_leaving, visited, visited_entry = self.patrol(self.input)

        visited.remove(self.start_pos)
        _map_dump = json.dumps(self.input)  # json dumps/loads faster than deepcopy

        # don't have to test every empty space, just the visited ones
        # because the obstruction must be on the visited path
        for vi, vj in visited:
            _map_copy = json.loads(_map_dump)
            _map_copy[vi][vj] = "#"

            pos = visited_entry[(vi, vj)][0]
            idx = visited_entry[(vi, vj)][1]

            is_leaving_copy, visited_copy, visited_entry_copy = self.patrol(_map_copy, pos, idx)
            if not is_leaving_copy:  # not leaving, because of the loop
                loop_count += 1

        return loop_count


    def patrol(self, _map, pos=None, idx=None):
            if not pos:
                pos = self.start_pos

            if not idx:
                idx = 0

            directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
            rows, cols = len(_map), len(_map[0])

            visited = set()
            visited.add((pos[0], pos[1]))

            visited_entry = {}  # for part 2, mark the entry point of the visited node

            while True:
                d = directions[idx]
                n = (pos[0] + d[0], pos[1] + d[1])

                if n[0] < 0 or n[0] >= rows or n[1] < 0 or n[1] >= cols:
                    return True, visited, visited_entry  # leaving the map

                if _map[n[0]][n[1]] == "#":
                    idx = (idx + 1) % 4
                    continue
                else:
                    visited.add((n[0], n[1]))
                    if n not in visited_entry:
                        visited_entry[n] = (pos, idx)
                    elif visited_entry[n] == (pos, idx):
                        return False, None, None  # loop detected
                    pos = n



    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
