# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """It's apparent that we need binary search, because the requirement is
        Logrithm runtime. The idea is to binary search the h-index. For each
        possible h-index, we check whether citations[N - h] is larger or smaller
        than h. If it is smaller than h, that means h is too big, otherwise too
        small.

        The difficult part is when h = 0. This means the h-index is either 0 or
        1. In this case, we simply increment lo and break out.

        After the binary search is done, lo could be the h-index or one bigger
        than the h-index. Thus, we need to do one more check.

        O(logN), 136 ms, 85% ranking.
        """
        lo, hi, N = 0, len(citations), len(citations)
        while lo < hi:
            mid = (lo + hi) // 2
            if mid == 0 or citations[N - mid] > mid:
                lo = mid + 1
            else:
                hi = mid
        return lo if citations[N - lo] >= lo else lo - 1


sol = Solution()
tests = [
    ([0,1,3,5,6], 3),
    ([1, 2, 100], 2),
    ([0,1,5,5,6], 3),
    ([0,1,5,5,6,5], 4),
    ([0], 0),
    ([1], 1),
    ([2], 1),
    ([0, 0], 0),
    ([1, 1, 1, 1], 1),
    ([0, 0, 0, 0, 2, 2], 2),
    ([11, 15], 2),
]

for i, (citations, ans) in enumerate(tests):
    res = sol.hIndex(citations)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
