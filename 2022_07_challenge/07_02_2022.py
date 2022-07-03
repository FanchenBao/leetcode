# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """LeetCode 1465

        Find the biggest vertical cut range and the biggest horizontal cut
        range, multiply them together.
        
        O(NlogN + MlogM), 514 ms, faster than 34.56%
        """
        horizontalCuts.sort()
        verticalCuts.sort()
        max_hor = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            max_hor = max(max_hor, horizontalCuts[i] - horizontalCuts[i - 1])
        max_ver = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            max_ver = max(max_ver, verticalCuts[i] - verticalCuts[i - 1])
        return (max_hor * max_ver) % 1000000007


sol = Solution()
tests = [
    (5, 4, [1,2,4], [1,3], 4),
    (5, 4, [3,1], [1], 6),
    (5, 4, [3], [3], 9),
]

for i, (h, w, horizontalCuts, verticalCuts, ans) in enumerate(tests):
    res = sol.maxArea(h, w, horizontalCuts, verticalCuts)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
