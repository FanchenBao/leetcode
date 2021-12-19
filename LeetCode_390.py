# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def lastRemaining(self, n: int) -> int:
        """The idea is to write out a few examples and look for the pattern. The
        pattern is always that the gap between the remaining values are doubled
        after each round. Thus, if we can keep track of the first remaining
        value when we go from left to right, and the last remaining value when
        we go from right to left, we will have found all remaining values. We
        can keep this process until there is only one remaining value after a
        round.

        O(logN), 58 ms, 19% ranking.
        """
        if n == 1:
            return 1
        go_right, left, right, gap = True, 2, n, 2
        while True:
            if go_right:
                right = (right - left) // gap * gap + left
                if left == right:
                    return left
                right -= gap
            else:
                left = right - (right - left) // gap * gap
                if left == right:
                    return right
                left += gap
            gap *= 2
            go_right = not go_right


class Solution2:
    def lastRemaining(self, n: int) -> int:
        """This is a much easier way to attack this problem.

        Ref: https://leetcode.com/problems/elimination-game/discuss/87119/JAVA%3A-Easiest-solution-O(logN)-with-explanation

        We already know that the gap doubles after each round, and that we only
        need to find out the first (or last) remaining value to know the entire
        remaining sequence. This method only needs to know the first value,
        because if we go from left to right, the next first value must be the
        current first value plus the previous gap. If we go from right to left,
        if there are odd number of values remaining, then the current first
        value will be eliminated, and thus the next first value is also the
        current first value plus the previous gap. But, if there are even number
        of values remaining, then the current first value does not get
        eliminated and remains the first value for the next round.
        """
        go_right, left, gap = True, 1, 1
        remain = n
        while remain > 1:
            if go_right or remain % 2:
                left += gap
            remain //= 2
            gap *= 2
            go_right = not go_right
        return left


sol = Solution2()
tests = [
    (9, 6),
    (2, 2),
    (9, 6),
    (20, 6),
    (21, 6),
    (22, 8),
    (23, 8),
    (100, 54),
]

for i, (n, ans) in enumerate(tests):
    res = sol.lastRemaining(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
