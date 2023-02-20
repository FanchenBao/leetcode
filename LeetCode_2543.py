# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        """Following the hint, we go from targetX and targetY back to (1, 1).
        This requires us to make the following moves:

        (x + y, y), (x, x + y), (x / 2, y), (x, y / 2)
        
        What I know so far. If targetX and targetY has gcd not equal to 1 or
        power of 2, no matter how we add them, the new x and y will always have
        a factor not divisible by 2. This means we can never reach 1 by division

        Thus, we can first take all factors of 2 away from targetX and targetY,
        and then check the remaining x, y gcd. If it is not 1, then it is not
        possible.

        However, what I currently cannot prove is that if x and y are coprime
        and odd, they can always go back to (1, 1).

        I can convert this problem to proving we can always create power of 2
        by some movement of (x + y, y) and (x, x + y), but I do not know how to
        prove this.

        Yep, it works: 41 ms, faster than 46.98%. But how do we prove it??
        """
        while targetX % 2 == 0:
            targetX //= 2
        while targetY % 2 == 0:
            targetY //= 2
        return math.gcd(targetX, targetY) == 1


class Solution2:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        """The full proof is by lee215:

        https://leetcode.com/problems/check-if-point-is-reachable/discuss/3082073/JavaC%2B%2BPython-1-line-GCD-Solution

        I was close. I realize that we can get down to two odd numbers for x and
        y that are also coprime. Then, I was trying to see if we can use some
        sort of mechanism to add x and y to reach power of 2, but the correct
        method is to decrease them and see if we can reach one. Since x and y
        are both odd, we can always do (x + y) / 2 to bring the larger of x and
        y down. If this new value is even, we keep dividing it by 2. Then we
        will reach a new pair of odd x and y. Repeat this process, and
        eventually we will reach a point where x or y becomes 1. And we know
        that once one of x or y becomes 1, we can return back to (1, 1). Or we
        can keep doing the trick of (x + y) / 2, and eventually we will have
        both x and y reaching 1.

        Thus from this analysis, we can even simplify the check to seeing
        whether the gcd of targerX and targetY is power of 2.

        lee215 uses this check x == x & -x to see whether x is power of 2
        """
        g = math.gcd(targetX, targetY)
        return g == g & -g


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
