# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """LeetCode 1338

        Just sort the count, and go from large to small.

        O(NlogN), 877 ms, faster than 63.53%
        """
        tgt = len(arr) // 2
        acc, res = 0, 0
        for c in sorted(Counter(arr).values(), reverse=True):
            if acc >= tgt:
                break
            acc += c
            res += 1
        return res
        

sol = Solution()
tests = [
    ([3,3,3,3,5,5,5,2,2,7], 2),
    ([7,7,7,7,7,7], 1),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minSetSize(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
