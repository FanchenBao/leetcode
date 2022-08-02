# from pudb import set_trace; set_trace()
from typing import List
import heapq
from bisect import bisect_right


class Solution1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """LeetCode 378

        Priority queue.

        O(NlogN) time, O(N) space, 296 ms, faster than 55.42% 
        """
        n = len(matrix)
        heap = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(heap)
        for _ in range(k):
            val, i, j = heapq.heappop(heap)
            j += 1
            if j < n:
                heapq.heappush(heap, (matrix[i][j], i, j))
        return val


class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """Binary search.

        Given a value, go row by row, find the number of elements that are
        smaller or equal to the value. Add them up. If the total count of nums
        smaller or equal to val is smaller than k, then we need to pick a
        larger value. Otherwise, we pick a smaller. We end the search when the
        count is equal to k - 1.

        O(Nlog(M)), where M = max(matrix) - min(matrix), O(1) space

        206 ms, faster than 90.92%
        """
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            count = 0
            for row in matrix:
                idx = bisect_right(row, mid)
                count += idx
            if count >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
        

sol = Solution2()
tests = [
    ([[1,5,9],[10,11,13],[12,13,15]], 8, 13),
    ([[-5]], 1, -5),
    ([[1,5,9],[10,11,13],[12,13,15]], 5, 11),
]

for i, (matrix, k, ans) in enumerate(tests):
    res = sol.kthSmallest(matrix, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
