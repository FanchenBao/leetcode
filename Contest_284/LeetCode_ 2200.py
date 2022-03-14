# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indices = [i for i, n in enumerate(nums) if n == key]
        res_set = set()
        N = len(nums)
        for idx in indices:
            for j in range(-k, k + 1):
                res_set.add(min(max(idx + j, 0), N - 1))
        return sorted(res_set)
        

# sol = Solution()
# tests = [
#     (9, 6),
#     (2, 2),
#     (9, 6),
#     (20, 6),
#     (21, 6),
#     (22, 8),
#     (23, 8),
#     (100, 54),
# ]

# for i, (n, ans) in enumerate(tests):
#     res = sol.lastRemaining(n)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
