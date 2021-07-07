# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right
import heapq


class Solution1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """LeetCode 378

        Sort the entire matrix by merge sorting every two rows.
        O(N^3), 1024 ms, too slow to have percentage ranking.
        """

        def merge_sort(arr1: List[int], arr2: List[int]) -> List[int]:
            res = []
            n1, n2 = len(arr1), len(arr2)
            arr1.append(math.inf)
            arr2.append(math.inf)
            i1, i2 = 0, 0
            while i1 < n1 or i2 < n2:
                if arr1[i1] <= arr2[i2]:
                    res.append(arr1[i1])
                    i1 += 1
                else:
                    res.append(arr2[i2])
                    i2 += 1
            return res

        n = len(matrix)
        res = []
        for i in range(0, n, 2):
            if i <= n - 2:
                res = merge_sort(res, merge_sort(matrix[i], matrix[i + 1]))
            else:
                res = merge_sort(res, matrix[i])
        return res[k - 1]


class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """I wasn't able to come up with a binary search solution, despite
        knowing that binary search would work. The following solution is from

        https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1322101/C%2B%2BPython-Binary-Search-Picture-Explain-Clean-and-Concise

        The main trick is to binary search any value between min matrix and max
        matrix, not a value specifically inside the matrix. For each value, we
        count the number of elements in the matrix that are smaller or equal to
        it. The count goes like this: if matrix[i][j] smaller or equal to value,
        then all j + 1 values in row i are smaller or equal to value. Otherwise,
        we move j to the left until matrix[i][j] is smaller or equal to value
        again.

        We shrink the search range to the left when the count is larger or equal
        to k. This allows us to find the smallest value that satisfies the k
        requirement. The final value is the answer.

        O(log(M)N), where M is max(matrix) - min(matrix) and N is the size
        of the matrix.  156 ms, 97% ranking.
        """
        n = len(matrix)
        left, right = matrix[0][0], matrix[n - 1][n - 1]
        while left < right:
            mid = (left + right) // 2
            count, j = 0, n - 1
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                if j < 0:
                    break
                count += j + 1
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left


class Solution3:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """The heap solution. From

        https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1322101/C%2B%2BPython-Binary-Search-Picture-Explain-Clean-and-Concise

        O(N^2log(k)), 196 ms
        """
        heap = []
        for row in matrix:
            for v in row:
                heapq.heappush(heap, -v)
                if len(heap) > k:
                    heapq.heappop(heap)
        return -heap[0]


class Solution4:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """Most naive. But it is not slow, because N is a small value. It has
        similar runtime as Solution2, because Nlog(N) is not too much bigger
        than log(M).

        On the other hand, Solution3, which seems pretty good, is slower than
        Solution4 because log(k) can be much larger than log(N).

        O(N^2log(N)), 156 ms
        """
        return sorted([v for row in matrix for v in row])[k - 1]


sol = Solution2()
tests = [
    ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13),
    ([[-5]], 1, -5),
    ([[1, 2], [1, 3]], 2, 1),
    ([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 5, 7),
]

for i, (matrix, k, ans) in enumerate(tests):
    res = sol.kthSmallest(matrix, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
