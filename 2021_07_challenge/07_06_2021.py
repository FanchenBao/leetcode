# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """LeetCode 1338

        Use a counter and sort the counter based on the counts. Go from the
        max counts down and count how many numbers we need to put in the set
        such that the removal is more than half the size of the array.

        O(NlogN), 588 mw, 65% ranking.
        """
        counter = Counter(arr)
        removed, n, res = 0, len(arr), 0
        for c in sorted(counter.values(), reverse=True):
            removed += c
            res += 1
            if 2 * removed >= n:
                return res


sol = Solution()
tests = [
    ([3, 3, 3, 3, 5, 5, 5, 2, 2, 7], 2),
    ([7, 7, 7, 7, 7, 7], 1),
    ([1, 9], 1),
    ([1000, 1000, 3, 7], 1),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minSetSize(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
