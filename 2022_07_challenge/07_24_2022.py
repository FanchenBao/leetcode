# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right


class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """LeetCode 240

        O(MlogN), 185 ms, faster than 86.99% 
        """
        for row in matrix:
            if row[0] > target:
                break
            idx = bisect_right(row, target)
            if row[idx - 1] == target:
                return True
        return False


class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Smarter method. Always compare to the upper right corner. If it is
        smaller than target, then we HAVE to move to the next row. If is bigger
        then we move leftwards.

        O(M + N)
        """
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False

        

# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
