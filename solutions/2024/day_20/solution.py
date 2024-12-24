# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/20

from ...base import CharSplitSolution, answer


class Solution(CharSplitSolution):
    _year = 2024
    _day = 20

    @answer(1402)
    def part_1(self) -> int:
        if self.use_test_data:
            picoseconds = 50
        else:
            picoseconds = 100
        track = self.parseTrack()
        
        return sum(saved >= picoseconds for saved in self.cheats(track, 2))

    def parseTrack(self):
        self.start = next((x, y) for y, row in enumerate(self.input)
                           for x, cell in enumerate(row) if cell == 'S')
        x, y = self.start
        track = [None, (x, y)]
        while self.input[y][x] != 'E':
            x, y = next(nb for nb in ((x - 1, y), (x + 1, y), (x, y -1), (x, y + 1)) 
                        if nb != track[-2] and self.input[nb[1]][nb[0]] != '#')
            track.append((x, y))
        return track[1:]

    def cheats(self, track, max_dist):
        for (t1, (x1, y1)) in enumerate(track):
            for t2 in range(t1 + 3, len(track)):
                x2, y2 = track[t2]
                dist = abs(x2 - x1) + abs(y2 - y1)
                if dist <= max_dist and t2 - t1 > dist:
                    yield t2 - t1 - dist

    @answer(1020244)
    def part_2(self) -> int:
        if self.use_test_data:
            picoseconds = 50
        else:
            picoseconds = 100
        track = self.parseTrack()

        return sum(saved >= picoseconds for saved in self.cheats(track, 20))
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
