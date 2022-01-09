# from pudb import set_trace; set_trace()
from typing import List, Tuple


class Solution1:
    def isRobotBounded(self, instructions: str) -> bool:
        """LeetCode 1041

        The insight is that no matter what instructions there are, we will
        always end up with the robot pointing north after either 1, 2 or 4
        rounds of instructions. When the robot points north again, we check
        whether its position is the same as the starting position. If it is,
        we can be sure that the robot will be contained within a circle.
        Otherwise, the robot will not be bounded.

        More specifically, if after the first round of instruction, the robot
        ends up pointing north, we only need this round; if it points south,
        we need 2 rounds; if it points east or west, we need 4 rounds.

        O(4N) in the worst case, where N is the length of instructions.

        32 ms, 65% ranking.
        """
        dxdy = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        def next_pos(x: int, y: int, d: int) -> Tuple[int, int, int]:
            for ins in instructions:
                if ins == 'G':
                    x, y = x + dxdy[d][0], y + dxdy[d][1]
                elif ins == 'L':
                    d = (d + 1) % 4
                else:
                    d = (4 + d - 1) % 4
            return x, y, d

        x, y, d = 0, 0, 0
        while True:
            x, y, d = next_pos(x, y, d)
            if not d:
                if x == 0 and y == 0:
                    return True
                else:
                    return False


class Solution2:
    def isRobotBounded(self, instructions: str) -> bool:
        """Solution1 is too complicated. We don't have to wait for the robot
        to point north again. It is guaranteed that if after one round of
        instruction, the robot does not end up pointing north, then it will
        definitely go back to the original position after two (if ending up
        pointing south) or four rounds (if ending up pointing east or west).
        Thus, our check is for the end position and orientation after one round
        """
        dxdy = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        def next_pos(x: int, y: int, d: int) -> Tuple[int, int, int]:
            for ins in instructions:
                if ins == 'G':
                    x, y = x + dxdy[d][0], y + dxdy[d][1]
                elif ins == 'L':
                    d = (d + 1) % 4
                else:
                    d = (4 + d - 1) % 4
            return x, y, d

        x, y, d = next_pos(0, 0, 0)
        return (x == 0 and y == 0) or d > 0


sol = Solution2()
tests = [
    ("GGLLGG", True),
    ('GG', False),
    ('GL', True),
]

for i, (instructions, ans) in enumerate(tests):
    res = sol.isRobotBounded(instructions)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
