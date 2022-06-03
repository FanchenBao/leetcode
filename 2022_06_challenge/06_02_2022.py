# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """LeetCode 867

        94 ms, faster than 54.92%
        """
        M, N = len(matrix), len(matrix[0])
        grid = [[0] * M for _ in range(N)]
        for j in range(N):
            for i in range(M):
                grid[j][i] = matrix[i][j]
        return grid
        

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
