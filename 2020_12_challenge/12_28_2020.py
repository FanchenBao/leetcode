# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def reachNumber(self, target: int) -> int:
        """This requires some thinking. The best way is to write out a few
        answers and study how they work. The idea is to first find the max n
        such that 1 + 2 + 3 + ... + n <= target. Then we keep adding n + 1,
        n + 2, ... Each time a new number is added, we compute how much we need
        to deduct to reach the target. Once the deduction number is even, we
        have reached the target, because each even deduction can be achieved
        by reversing one or more of the numbers we have added already.

        O(?), 32 ms, 71% ranking.
        """
        target = abs(target)  # negative number works the same way as positive
        max_n = int(math.sqrt(2 * target + 0.25) - 0.5)
        base = max_n * (max_n + 1) // 2
        n = max_n
        while base - target < 0 or (base - target) % 2:
            n += 1
            base += n
        return n


sol = Solution()
tests = [
    (1, 1),
    (2, 3),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 3),
    (7, 5),
    (8, 4),
    (9, 5),
    (10, 4),
    (11, 5),
    (12, 7),
]

for i, (target, ans) in enumerate(tests):
    res = sol.reachNumber(target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
