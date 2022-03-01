# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """LeetCode 338

        O(N), 91 ms, 81% ranking.
        """
        return [bin(i).count('1') for i in range(n + 1)]

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
