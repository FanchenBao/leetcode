# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """LeetCode 1288

        We sort the intervals first, but the key is to first sort based on the
        left range increasingly. And if the left range is the same, we sort
        based on the right range decreasingly. This makes sure that if multiple
        intervals have the same left range, the biggest range always gets
        visited first.

        O(NlogN), 100 ms, 81% ranking
        """
        intervals.sort(key=lambda inter: (inter[0], -inter[1]))
        remove = 0
        i, N = 0, len(intervals)
        for j in range(1, N):
            if intervals[j][1] <= intervals[i][1]:
                remove += 1
            else:
                i = j
        return N - remove


sol = Solution()
tests = [
    ([[1,4],[3,6],[2,8]], 2),
    ([[1,4],[2,3]], 1),
    ([[1,2],[1,4],[3,4]], 1),
]

for i, (intervals, ans) in enumerate(tests):
    res = sol.removeCoveredIntervals(intervals)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
