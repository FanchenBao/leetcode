# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """This is more of a math problem than programming.

        Once it is proven that the only situation where the robot cannot be
        bounded is when after executing the instructions, it ends up pointing
        the same direction as the start and its position is not the same as the
        start. Any other scenarios will always bound the robot. Thus, the
        programming is reduced to finding the end position and direction of the
        robot after executing the instructions for once.

        Note: using dx, dy to dictate directions to go is cleaner than setting
        up a dirs list. See the solution here:
        https://leetcode.com/explore/featured/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3463/discuss/290856/JavaC++Python-Let-Chopper-Help-Explain

        In addition, see this for the math proof:
        leetcode.com/explore/featured/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3463/discuss/290856/JavaC++Python-Let-Chopper-Help-Explain/275582
        """
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W
        x, y, di = 0, 0, 0
        for ins in instructions:
            if ins == 'G':
                x, y = x + dirs[di][0], y + dirs[di][1]
            elif ins == 'L':
                di = (di - 1 + 4) % 4
            else:  # ins == 'R'
                di = (di + 1) % 4
        return True if (x == 0 and y == 0) or di != 0 else False
