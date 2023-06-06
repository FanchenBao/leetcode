# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution1:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        """We should not sort by the size of reward1 or reward2. We shall sort
        by the advantage we can get by taking reward1 over reward2. We shall
        take the k types of cheese that grant us the max advantage of taking
        reward1 over reward2. The advantage can be computed by the difference
        between r1 and r2. Thus, we sort in reverse, based on r1 - r2.

        Then we just take the first k rewards from reward1, and take the
        remaining from reward2.

        O(NlogN), 927 ms, faster than 68.15% 
        """
        r1r2 = sorted([(r1, r2) for r1, r2 in zip(reward1, reward2)], key=lambda tup: -tup[0] + tup[1])
        sum_1 = rem_2 = 0
        for i in range(k):
            sum_1 += r1r2[i][0]
            rem_2 += r1r2[i][1]
        return sum(reward2) - rem_2 + sum_1


class Solution2:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        """Inspired by lee215: https://leetcode.com/problems/mice-and-cheese/discuss/3368322/JavaC%2B%2BPython-K-Largest-Ai-Bi

        This is wonderful implementation. Two things to note:

        1. we don't have to sum separately sum_1 and rem_2 as in Solution1,
        because by summing r1 - r2, we already have sum_1 - rem_2.
        2. we can use heapq.nlargest to directly find the k largest r1 - r2.

        Bravo.

        982 ms, faster than 47.71%
        """
        return sum(reward2) + sum(heapq.nlargest(k, (r1 - r2 for r1, r2 in zip(reward1, reward2))))

sol = Solution2()
tests = [
    ([1,1,3,4],[4,4,1,1], 2, 15),
    ([1,1], [1,1], 2, 2),
    ([10,10,10,10], [10,10,1,1], 2, 40),
    ([10,10,10,10], [10,10,100,100], 2, 220),
    ([1,2,2,2,3,3], [2,1,2,4,3,2], 5, 15),
]

for i, (reward1, reward2, k, ans) in enumerate(tests):
    res = sol.miceAndCheese(reward1, reward2, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
