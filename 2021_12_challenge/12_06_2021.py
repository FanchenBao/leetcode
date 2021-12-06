# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """LeetCode 1217

        All even-positioned chips can move to postion 2 with no cost.
        All odd-positioned chips can move to position 1 with no cost.
        Thus the min cost is the min count of chips in position 2 and 1.

        O(N), 28 ms, 90% ranking.
        """
        total_odd = sum(p & 1 for p in position)
        total_even = len(position) - total_odd
        return min(total_odd, total_even)


sol = Solution()
tests = [
    ([1, 2, 3], 1),
    ([2, 2, 2, 2, 3, 3], 2),
    ([1, 1000000000], 1),
    ([1], 0),
]

for i, (position, ans) in enumerate(tests):
    res = sol.minCostToMoveChips(position)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
