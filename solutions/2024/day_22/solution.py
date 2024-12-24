# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/22

from ...base import IntSplitSolution, answer
import numpy as np

class Solution(IntSplitSolution):
    _year = 2024
    _day = 22

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    @answer((17005483322, 1910))
    def solve(self) -> tuple[int, int]:
        secret_size = 2001
        buyers = len(self.input)
        mask = 2 ** 24 - 1
        all_4seq = 19 ** 4

        n = np.array(self.input, dtype=np.int32)
        all_secrets = np.zeros((secret_size, buyers), dtype=np.int32)
        all_secrets[0,:] = n
        for i in range(1, secret_size):
            n ^= (n << 6) & mask
            n ^= (n >> 5)
            n ^= (n << 11) & mask 
            all_secrets[i,:] = n
        part1 = sum(n.astype(np.uint64))
        value = all_secrets % 10
        diff = value[:-1] - value[1:] + 9
        encode = diff[:-3] + 19 * diff[1:-2] + 19**2 * diff[2:-1] + 19**3 * diff[3:]
        encode += np.arange(buyers) * all_4seq

        flat_value = value[4:].flatten()
        unique_values, unique_indices = np.unique(encode, return_index=True)
        col = np.zeros(all_4seq, dtype=np.uint16)
        np.add.at(col, unique_values % all_4seq, flat_value[unique_indices])
        return part1, max(col)