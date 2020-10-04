# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """98% ranking. This is a very easy question"""
        counter = Counter(nums)
        res = 0
        for n in counter.keys():
            counter[n] -= 1
            if counter.get(n + k, 0):
                res += 1
            counter[n] += 1
        return res



sol = Solution()
tests = [
    ([3, 1, 4, 1, 5], 2, 2),
    ([1, 2, 3, 4, 5], 1, 4),
    ([1, 3, 1, 5, 4], 0, 1),
    ([1, 2, 4, 4, 3, 3, 0, 9, 2, 3], 3, 2),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.findPairs(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
