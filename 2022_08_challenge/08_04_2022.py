# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def mirrorReflection(self, p: int, q: int) -> int:
        """LeetCode 858

        I thought this is going to be an easy problem, but I got stuck for one
        hour and 45 minutes. It was just so convoluted in my head and I
        couldn't make sense of it. The final solution is very complicated, and
        I am sure the actual solution is very simple.

        This solution uses divmod to compute the number of steps taken to
        advance either upwards or downwards, and the starting position of the
        laser in the next round on either the left or right wall.

        The complication is that depending on the direction of the laser move-
        ment and the parity of the number of steps, the destination corner
        changes.

        47 ms, faster than 62.38%
        """
        r, c_ = 0, 0
        dr = 'ur'
        while True:
            c, r = divmod(p - (q - r), q)
            c += c_ + 1
            if r == 0:
                if dr == 'lr' or dr == 'll':
                    return 0
                if (dr == 'ur' and c % 2 == 0) or (dr == 'ul' and c % 2):
                    return 2
                if (dr == 'ur' and c % 2) or (dr == 'ul' and c % 2 == 0):
                    return 1
            if dr == 'ur':
                dr = 'lr' if c % 2 else 'll'
            elif dr == 'ul':
                dr = 'll' if c % 2 else 'lr'
            elif dr == 'lr':
                dr = 'ur' if c % 2 else 'ul'
            elif dr == 'll':
                dr = 'ul' if c % 2 else 'ur'
            c_ = 1


class Solution2:
    def mirrorReflection(self, p: int, q: int) -> int:
        """Use a dict to codify the rules for next direction and final checking
        
        Better performance because we avoid a lot of if-else.
        37 ms, faster than 83.17%
        """
        r, c_ = 0, 0
        dr = 'ur'
        next_dr_rule = {
            'ur': ['ll', 'lr'],
            'ul': ['lr', 'll'],
            'lr': ['ul', 'ur'],
            'll': ['ur', 'ul']
        }
        checking = {
            'lr': [0, 0],
            'll': [0, 0],
            'ur': [2, 1],
            'ul': [1, 2],
        }
        while True:
            c, r = divmod(p - (q - r), q)
            c += c_ + 1
            if r == 0:
                return checking[dr][c % 2]
            dr = next_dr_rule[dr][c % 2]
            c_ = 1


class Solution3:
    def mirrorReflection(self, p: int, q: int) -> int:
        """Inspired by https://leetcode.com/problems/mirror-reflection/discuss/146336/Java-solution-with-an-easy-to-understand-explanation

        Read that post to have a visual understanding of the solution.

        51 ms, faster than 45.54%
        """
        lcm_ = math.lcm(p, q)  # least common multiplier
        num_ref = lcm_ // q - 1  # number of reflections
        num_room = lcm_ // p  # number of TOTAL rooms (original + extended)
        if num_ref % 2:  # odd reflections, always ending on the left side
            return 2
        # even reflections, depending on the number of rooms. Each even count
        # of rooms can be thought of as the original room flipped upwards.
        # Hence, the top right corner of an even-th room represents 0.
        return 1 if num_room % 2 else 0


sol = Solution3()
tests = [
    (2, 1, 2),
    (3, 1, 1),
    (5, 2, 0),
    (15, 12, 0),
    (3, 2, 0),
    (4, 3, 2),
]

for i, (p, q, ans) in enumerate(tests):
    res = sol.mirrorReflection(p, q)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
