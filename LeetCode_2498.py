# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def maxJump(self, stones: List[int]) -> int:
        """This solution comes completely from the hint. Basically we say the
        optimal strategy is to skip every other stones on the way there, and
        take all the remaining stones on the way back.

        I don't have a solid proof, but this strategy does make sense.

        O(N), 793 ms, faster than 83.80%
        """
        N = len(stones)
        fmax = 0
        for i in range(0, N, 2):
            if i + 2 < N:
                fmax = max(fmax, stones[i + 2] - stones[i])
        if N % 2 == 0:
            fmax = max(fmax, stones[-1] - stones[-2])
            rmax = 0
            for i in range(N - 1, -1, -2):
                if i - 2 >= 0:
                    rmax = max(rmax, stones[i] - stones[i - 2])
            rmax = max(rmax, stones[1] - stones[0])
        else:
            rmax = stones[N - 1] - stones[N - 2]
            for i in range(N - 2, -1, -2):
                if i - 2 >= 0:
                    rmax = max(rmax, stones[i] - stones[i - 2])
            rmax = max(rmax, stones[1] - stones[0])
        return max(fmax, rmax)


class Solution2:
    def maxJump(self, stones: List[int]) -> int:
        """After checking the discussion, I saw better implementation. I am
        slightly more convinced of the proof the alternative the steps is the
        best strategy.
        """
        N = len(stones)
        res = stones[1] - stones[0]
        for i in range(2, N, 2):
            res = max(res, stones[i] - stones[i - 2])
        for i in range(3, N, 2):
            res = max(res, stones[i] - stones[i - 2])
        return res


sol = Solution2()
tests = [
    ([0,2,5,6,7], 5),
    ([0,3,9], 9),
]

for i, (stones, ans) in enumerate(tests):
    res = sol.maxJump(stones)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
