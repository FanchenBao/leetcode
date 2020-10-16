# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """92% ranking"""
        for row in matrix:
            if target in row:
                return True
        return False


class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """97% ranking"""
        def binary_search_row(row_idx: int) -> bool:
            lo, hi = 0, len(matrix[row_idx]) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if matrix[row_idx][mid] < target:
                    lo = mid + 1
                elif matrix[row_idx][mid] > target:
                    hi = mid - 1
                else:
                    return True
            return False

        def binary_search_col() -> int:
            lo, hi = 0, len(matrix) - 1
            if lo == hi:  # if matrix has only one row
                return lo
            while lo <= hi:
                mid = (lo + hi) // 2
                if matrix[mid][0] < target:
                    lo = mid + 1
                elif matrix[mid][0] > target:
                    hi = mid - 1
                else:
                    return mid
            return hi

        return binary_search_row(binary_search_col()) if matrix else False


sol = Solution2()
tests = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 1, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 5, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 7, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 10, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 11, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 16, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 20, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 23, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 30, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 34, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 50, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 51, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 31, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 21, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 17, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 8, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 4, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 0, False),
    ([], 0, False),
    ([[]], 0, False),
]

for i, (matrix, target, ans) in enumerate(tests):
    res = sol.searchMatrix(matrix, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
