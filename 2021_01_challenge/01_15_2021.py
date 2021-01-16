# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        """Easy question. Straightforward solution. No explanation needed.

        O(N), 28 ms, 87% ranking.
        """
        if n == 0:
            return 0
        nums = [0, 1]
        res = 1
        for i in range(2, n + 1):
            if i % 2:
                nums.append(nums[i // 2] + nums[i // 2 + 1])
            else:
                nums.append(nums[i // 2])
            res = max(res, nums[-1])
        return res


sol = Solution()
tests = [
    (7, 3),
    (2, 1),
    (3, 2),
    (0, 0),
    (1, 1),
]

for i, (n, ans) in enumerate(tests):
    res = sol.getMaximumGenerated(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
