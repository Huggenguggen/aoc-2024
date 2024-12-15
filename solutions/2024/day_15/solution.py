# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/15

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 15

    def canMove(self, grid, move, currX, currY):
        directions = {
            "<": (0, -1),
            ">": (0, 1),
            "^": (-1, 0),
            "v": (1, 0)
        }
        dy, dx = directions[move]
        x, y = currX, currY
        while grid[y][x] != '.':
            if grid[y][x] == '#':
                return False 
            y += dy 
            x += dx

        return True

    def Move(self, grid, move, currX, currY):
        directions = {
            "<": (0, -1),
            ">": (0, 1),
            "^": (-1, 0),
            "v": (1, 0)
        }
        dy, dx = directions[move]
        last = "."
        x, y = currX, currY
        while grid[y][x] != '.':
            grid[y][x], last = last, grid[y][x]
            y += dy
            x += dx
        grid[y][x] = last

        return (currX + dx, currY + dy)

    @answer(1511865)
    def part_1(self) -> int:
        grid = self.input[:self.input.index("")]
        grid = [list(x) for x in grid]
        moves = self.input[self.input.index("")+1:]
        moves = "".join(moves)
        # print(f"grid: {grid} \n moves: {moves}")
        currY = currX = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    currY, currX = i, j
                    break

        for move in moves:
            # print(f"Move: {move}")
            # print(f"Grid: \n {'\n'.join("".join(x for x in row) for row in grid)}")
            # print(f"currentpos: {currX}, {currY}")
            if self.canMove(grid, move, currX, currY):
                # print(f"move will occur next")
                currX, currY = self.Move(grid, move, currX, currY)

        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O":
                    total += (100 * i + j)
        return total

    @answer(1519991)
    def part_2(self) -> int:
        grid = self.input[:self.input.index("")]
        grid = [list(x.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")) for x in grid]
        moves = self.input[self.input.index("")+1:]
        moves = "".join(moves)
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "@":
                    cx,cy = i,j
                    break
        for idx,move in enumerate(list(moves)):
            dx,dy = {
                "^": (-1,0),
                "v": (1,0),
                ">": (0,1),
                "<": (0,-1)
            }[move]

            c2m = [(cx,cy)]
            i = 0
            impos = False
            while i < len(c2m):
                x,y = c2m[i]
                nx,ny = x+dx,y+dy
                if grid[nx][ny] in "O[]":
                    if (nx,ny) not in c2m:
                        c2m.append((nx,ny))
                    if grid[nx][ny] == "[":
                        if (nx,ny+1) not in c2m:
                            c2m.append((nx,ny+1))
                    if grid[nx][ny] == "]":
                        if (nx,ny-1) not in c2m:
                            c2m.append((nx,ny-1))
                elif grid[nx][ny] == "#":
                    impos = True
                    break
                i += 1
            if impos:
                continue

            new_grid = [[grid[i][j] for j in range(m)] for i in range(n)]
            for x,y in c2m:
                new_grid[x][y] = "."
            for x,y in c2m:
                new_grid[x+dx][y+dy] = grid[x][y]

            grid = new_grid

            cx += dx
            cy += dy

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] not in "[O":
                    continue
                ans += 100 * i + j
        return ans
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
