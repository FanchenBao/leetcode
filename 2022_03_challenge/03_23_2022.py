# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from collections import deque


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        """LeetCode 991

        My initial solution was BFS, which considers all possibilities. It
        fails due to memory limit. This suggests that the correct answer must
        be greedy. In the greedy solution, odd target must plus one. This is
        deterministic. Even target can plus one or divided by 2. The thing is
        if we do even target plus one, the next step will have to plus one as
        well because the target becomes odd. Then we divide by two, we reach
        a value in three steps, whereas if we start by dividing by 2, we can
        reach the same value in two steps. Hence, add one to even target is
        always worse than dividing it by two.

        Thus, we have the greedy: if target is odd, plus one; if target is even
        divided by 2. We start from target and work backwards toward startValue.
        Any time target is smaller than startValue, we can deterministically
        say the number of steps is startValue - target.

        O(logN), 35 ms, 71% ranking.
        """
        res = 0
        while target != startValue:
            if target <= startValue:
                return res + startValue - target
            if target % 2:
                target += 1
            else:
                target //= 2
            res += 1
        return res


sol = Solution1()
tests = [
    (2, 3, 2),
    (5, 8, 2),
    (3, 10, 3),
    (1, 1, 0),
]

for i, (startValue, target, ans) in enumerate(tests):
    res = sol.brokenCalc(startValue, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
