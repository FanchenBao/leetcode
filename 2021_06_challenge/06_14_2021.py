# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """LeetCode 1710.

        It is a knapsack problem, but specifically it is a bounded knapsack
        with equal weight on each item. Since the weight is the same for all
        boxes, we can solve this problem using greedy method. That is, we always
        choose the boxes with the highest units first.

        O(Nlog(N)), 156 ms, 59% ranking.
        """
        boxTypes.sort(key=lambda tup: tup[1], reverse=True)
        res = 0
        for n, u in boxTypes:
            res += min(n, truckSize) * u
            truckSize -= n
            if truckSize <= 0:
                break
        return res


sol = Solution()
tests = [
    ([[1, 3], [2, 2], [3, 1]], 4, 8),
    ([[5, 10], [2, 5], [4, 7], [3, 9]], 10, 91),
]

for i, (boxTypes, truckSize, ans) in enumerate(tests):
    res = sol.maximumUnits(boxTypes, truckSize)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
