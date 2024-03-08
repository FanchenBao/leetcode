# from pudb import set_trace; set_trace()
from collections import Counter
from typing import List
import math


class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        """
        An attempt of using Greedy.

        Sort items and pick the last k as the initial elegance. Then we go
        through each of the last k from the smallest profit to the largest.

        If any item belongs to a category that has more than one item, it can
        be replaced by the biggest remaining element that does not have a
        category belonging to the last k. This guarantees that we are reducing
        the smallest profit, adding the biggest remaining profit, and increasing
        the number of unique count.

        One thing to note is that when we add the new item, it must also be
        unique. Otherwise, we will not benefit from the increase of unique
        count.

        O(N), 1313 ms, faster than 39.19%
        """
        items.sort()
        freq: Counter = Counter()
        N = len(items)
        eleg = 0
        for i in range(N - k, N):
            eleg += items[i][0]
            freq[items[i][1]] += 1
        eleg += len(freq) ** 2
        res = eleg
        i, j = N - k, N - k - 1
        n = len(freq)  # original number of unique categories
        while i < N and j >= 0:
            if freq[items[i][1]] > 1:
                while j >= 0 and items[j][1] in freq:
                    j -= 1
                if j >= 0 and freq[items[j][1]] == 0:
                    eleg = eleg - items[i][0] + items[j][0] + 2 * n + 1
                    res = max(res, eleg)
                    freq[items[i][1]] -= 1
                    freq[items[j][1]] += 1
                    j -= 1
                    n += 1
            i += 1
        return res


sol = Solution()
tests = [
    # ([[1, 6], [10, 1], [4, 4], [8, 1], [6, 2], [10, 1], [5, 5], [4, 4]], 5, 51),
    ([[2, 2], [8, 6], [10, 6], [2, 4], [9, 5], [4, 5]], 4, 39),
]

for i, (items, k, ans) in enumerate(tests):
    res = sol.findMaximumElegance(items, k)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
