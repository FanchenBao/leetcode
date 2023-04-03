# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class Solution1:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """LeetCode 2300

        This follows yesterday's idea of two pointers. We sort spells from large
        to small, and then potions from small to large. Then for each spell,
        we go from small to large in potions until their product is larger or
        equal to success. Now, when we handle the next spell, since it is smaller
        than the previous one, we don't have to restart the search in potions.
        Instead, we continue from the previous stoppage. Continue this until
        we handle all spells.

        This problem is a little bit more complicated, because the returned
        value has to be the number of valid pairs per spells in its original
        order. Therefore, we have to handle that as well. But it is not that
        hard.

        O(NlogN + MlogM + M + N), 1294 ms, faster than 79.60%
        """
        sorted_spells = sorted([(s, i) for i, s in enumerate(spells)], reverse=True)
        potions.sort()
        j = 0
        res = [0] * len(spells)
        for s, i in sorted_spells:
            while j < len(potions) and potions[j] * s < success:
                j += 1
            res[i] = len(potions) - j
        return res


class Solution2:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """We will try the binary search solution, which only requires us to
        sort potions. It's actually simpler.

        O(MlogM + NlogM), 1196 ms, faster than 95.47% 
        """
        potions.sort()
        res = []
        for s in spells:
            q, r = divmod(success, s)
            q -= int(r == 0)  # pay attention to the case where s divides success
            res.append(len(potions) - bisect_right(potions, q))
        return res


sol = Solution2()
tests = [
    ([5,1,3], [1,2,3,4,5], 7, [4,0,3]),
    ([3,1,2], [8,5,8], 16, [2,0,2]),
]

for i, (spells, potions, success, ans) in enumerate(tests):
    res = sol.successfulPairs(spells, potions, success)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
