# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution1:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """Straightforward solution. We create a list with each element being
        a tuple of (number of ones, index of the row). We sort this list first
        based on number of ones, and then on index. We return the indices of
        the first k element in the list.

        O(MN + Mlog(M)) where M is the number of rows and N is the number of
        columns. 108 ms, 72% ranking.
        """
        strengths = [(row.count(1), i) for i, row in enumerate(mat)]
        strengths.sort()
        return [tup[1] for tup in strengths[:k]]


class Solution2:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """Same solution but one-liner"""
        return [tup[1] for tup in sorted([(row.count(1), i) for i, row in enumerate(mat)])[:k]]


class Solution3:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """This solution takes advantage of the way 1s and 0s are organized in
        each row. Since each row starts with 1s, we can check columns by columns
        to find the weakest row. The weaker the row, the earlier the 0 shows up.
        We record all the rows that have 0 show up, and the order of recording
        is the order of the weakest rows.

        The trick is when there are not enough weak rows in the matrix. This
        means there are not enough rows that contain 0s. In that case, we have
        to run another round to push in the non-weak rows (i.e. rows containing
        all 1s) from top to bottom until we fill all k positions.

        O(MN + M) = O(MN). 108 ms, 72% ranking.
        """
        res = []
        checked = set()
        for j in range(len(mat[0])):
            for i in range(len(mat)):
                if mat[i][j] == 0 and i not in checked:
                    res.append(i)
                    checked.add(i)
                if len(res) == k:
                    return res
        for i in range(len(mat)):
            if i not in checked:
                res.append(i)
            if len(res) == k:
                return res


class Solution4:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """Heap + binary search solution. Should technically be the fastest
        solution, but in reality, given the small test cases, the overhead of
        setting up heap and binary search makes this solution not optimal.

        Binary search is used to count the number of ones. It can do this in
        O(logN) time, instead of O(N) when using .count()

        Heap is used to keep the top k desirable row indices. The only trick is
        to push the negative of the number of ones and indices, because when we
        pop from the heap when its size exceeds k, we want to pop the rows with
        the most ones. And since heap in Python is a min heap, to pop the rows
        with the most ones, we need to reverse the input.

        O(M * (log(N) + log(k)) + klog(k) + k), which consists of three portions
        the first one is the bulk of the algorithm where we count ones, push or
        pop from the heap. The second one is at the end when we reorder the
        content of the heap. And the last one is the reversal of the result.

        112 ms, 48% ranking.
        """

        def count_ones(row):
            left, right = 0, len(row) - 1
            while left < right:
                mid = (left + right) // 2
                if row[mid]:
                    left = mid + 1
                else:
                    right = mid
            # special case is when the row is all ones, where we must add one
            # to the final result
            return left if not row[left] else left + 1

        heap = []
        for i, row in enumerate(mat):
            heapq.heappush(heap, (-count_ones(row), -i))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            res.append(-heapq.heappop(heap)[1])
        return res[::-1]


sol = Solution4()
tests = [
    ([[1, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1]], 3, [1, 2, 3]),
    # ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 3, [0, 1, 2]),
    # ([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], 3, [2, 0, 3]),
    # ([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2, [0, 2]),
]

for i, (mat, k, ans) in enumerate(tests):
    res = sol.kWeakestRows(mat, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
