# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """We use a counter to count the number of appearances of each number.
        Then for each number in nums, we count the length of harmonious
        sequence involving n and n + 1, or n and n - 1, if such sequence exists.
        We update the result after each count.

        UPDATE: no need to do both n + 1 and n - 1. We only need to do one of
        them.

        O(N), 316 ms, 54 % ranking.
        """
        counter = Counter(nums)
        res = 0
        for n in counter.keys():
            if n + 1 in counter:
                res = max(res, counter[n] + counter[n + 1])
        return res


sol = Solution()
tests = [
    ([1, 3, 2, 2, 5, 2, 3, 7], 5),
    ([1, 2, 3, 4], 2),
    ([1, 1, 1, 1], 0),
    ([1], 0),
    ([1, 3, 5, 7], 0)
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findLHS(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
