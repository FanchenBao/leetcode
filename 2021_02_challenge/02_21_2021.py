# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        """LeetCode 991
    
        We know from the beginning that if X >= Y, then the answer is trivial
        which is X - Y.

        If X < Y, it is harder to reason from the perspective of X, because X
        can either double or minus one and then double. We are not sure which
        way to go. On the contrary, if we see the problem from the perspective
        of Y, it becomes very clear, because Y can only plus one or half. Since
        an odd number cannot half, it is deterministic that Y either half when
        it is an even number, or plus one and then half if it is an odd number.
        So we can bring Y down to X. Now Y can be brought down to exactly the
        same as X, and we are done. However, it is also possible that Y is
        brought down to a value lower than X. In that case, we are actually in
        the first scenario, and the additonal steps would just be the difference
        between X and that value smaller than X.

        O(log(Y)), 28 ms, 86% ranking.
        """
        steps = 0
        while Y > X:
            Y = (Y + 1) if Y % 2 else (Y // 2)
            steps += 1
        return steps + X - Y


sol = Solution()
tests = [
    (2, 3, 2),
    (5, 8, 2),
    (3, 10, 3),
    (1024, 1, 1023),
    (3, 101, 11),
]

for i, (X, Y, ans) in enumerate(tests):
    res = sol.brokenCalc(X, Y)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
