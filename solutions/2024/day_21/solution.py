# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/21

from ...base import StrSplitSolution, answer
from collections import defaultdict
from typing import List

class Solution(StrSplitSolution):
    _year = 2024
    _day = 21

    def enter_codes(self, codes: List[str], robot_dir_keypads: int):
        global button_presses
        complexity_sum = 0
        for code in codes:
            # A "button press" is a sequence of ending in A
            button_presses = defaultdict(int)

            # First count button presses on the numeric keypad
            self.move_numeric_keypad(code)

            # Count all the button presses on the directional keypads
            for n in range(robot_dir_keypads):
                self.count_dir_keypad_presses()

            complexity = 0
            for button_press, count in button_presses.items():
                complexity += len(button_press) * count
            complexity_sum += complexity * int(code[:3])
        return complexity_sum


    def move_numeric_keypad(self, code: str):
        from_button = 'A'
        for button in code:
            directions = self.move_to_button(from_button, button)
            from_button = button
            directions += 'A'
            button_presses[directions] += 1
        return

    def move_to_button(self, from_button, to_button):
        """If moving in the preferred direction would eventually move to the
        missing button, then move all the way in the 90° direction. """
        keypad = {'7':(0,0), '8':(1,0), '9':(2,0),
                '4':(0,1), '5':(1,1), '6':(2,1),
                '1':(0,2), '2':(1,2), '3':(2,2),
                'x':(0,3), '0':(1,3), 'A':(2,3)}
        
        x1, y1 = keypad[from_button]
        x2, y2 = keypad[to_button]
        nx, ny = keypad['x']    # missing button
        directions = ''
        while (x1, y1) != (x2, y2):
            if x2 < x1:             # highest priority is left
                if (y1 == ny) and (x2 == nx):    # if would move to missing button
                    directions += '^' * (y1 - y2)   # move up instead
                    y1 = y2
                else:
                    directions += '<'
                    x1 -= 1
            elif y2 < y1:           # move up
                directions += '^'
                y1 -= 1
            elif y2 > y1:
                if (x1 == nx) and (y2 == ny):    # if would move to missing button
                    directions += '>' * (x2 - x1)   # move right instead
                    x1 = x2
                else:
                    directions += 'v'   # move down
                    y1 += 1
            elif x2 > x1:        # lowest priority is right
                directions += '>'
                x1 += 1
        return directions


    def count_dir_keypad_presses(self):
        iterate_button_presses = dict(button_presses)
        for button_press, count in iterate_button_presses.items():
            self.move_dir_keypad(button_press, count)
            button_presses[button_press] -= count
        return

    def move_dir_keypad(self, code, count):
        dir_keypad_moves = dict([(('A','^'),'<A'),
                            (('A','>'),'vA'),
                            (('A','v'),'<vA'),
                            (('A','<'),'v<<A'),
                            (('^','A'),'>A'),
                            (('^','>'),'v>A'),
                            (('^','<'),'v<A'),
                            (('^','v'),'vA'),
                            (('v','A'),'^>A'),
                            (('v','>'),'>A'),
                            (('v','<'),'<A'),
                            (('v','^'),'^A'),
                            (('>','A'),'^A'),
                            (('>','^'),'<^A'),
                            (('>','v'),'<A'),
                            (('>','<'),'<<A'),
                            (('<','A'),'>>^A'),
                            (('<','^'),'>^A'),
                            (('<','v'),'>A'),
                            (('<','>'),'>>A')])
        
        from_button = 'A'
        for button in code:
            if from_button == button:
                directions = 'A'
            else:
                directions = dir_keypad_moves[(from_button, button)]
            from_button = button
            button_presses[directions] += count
        return

    @answer(176650)
    def part_1(self) -> int:
        return self.enter_codes(self.input, 2)

    @answer(217698355426872)
    def part_2(self) -> int:
        return self.enter_codes(self.input, 25)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
