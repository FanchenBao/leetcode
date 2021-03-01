# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def distributeCandies(self, candyType: List[int]) -> int:
        """LeetCode 575

        A very straightforward solution. We compute the total number of
        unique candy types. Say there are in total N candies and n types of
        candidies. If N // 2 >= n, we return n (i.e. there are fewer types of
        candies than the amount Alice can eat). Otherwise, we return N (i.e.
        there are more candy types than the amount Alice can eat).

        We also try to be a smartass by writing it in oneline with the help of
        walrus operator.

        O(N), 812 ms, 48% ranking.
        """
        return n if (N := len(candyType) // 2) >= (n := len(set(candyType))) else N


class Solution2:
    def distributeCandies(self, candyType: List[int]) -> int:
        """We only need to return the min between N // 2 and n.

        Inspired by https://leetcode.com/problems/distribute-candies/solution/129295
        """
        return min(len(candyType) // 2, len(set(candyType)))


sol = Solution2()
tests = [
    ([1, 1, 2, 2, 3, 3], 3),
    ([1, 1, 2, 3], 2),
    ([6, 6, 6, 6], 1),
]

for i, (candyType, ans) in enumerate(tests):
    res = sol.distributeCandies(candyType)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
