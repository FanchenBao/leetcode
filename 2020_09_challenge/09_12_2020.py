# from pudb import set_trace; set_trace()
from typing import List
from itertools import combinations


class Solution1:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """Brute force"""
        res = []
        for comb in combinations(range(1, 10), k):
            if sum(comb) == n:
                res.append(list(comb))
        return res


class Solution2:
    def helper(self, k: int, n: int, start: int, cur: List[int], res: List[List[int]]) -> None:
        if k == 1 and start <= n <= 9:
            res.append(cur + [n])
        else:
            for next_val in range(start + 1, n // 2 + 1):
                self.helper(k - 1, n - start, next_val, cur + [start], res)
                if k == 2:  # with current start, the degree of freedom is only one
                    return

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        for start in range(1, n // 2 + 1):
            self.helper(k, n, start, [], res)
        return res


class Solution3:
    def helper(self, k: int, remain: int, cur: List[int], res: List[List[int]]) -> None:
        if k == 0 and remain == 0:
            res.append(cur[:])
        else:
            for start in range(cur[-1] + 1, 10):
                self.helper(k - 1, remain - start, cur + [start], res)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """Cleaner backtrack"""
        res = []
        for start in range(1, n // 2 + 1):
            self.helper(k - 1, n - start, [start], res)
        return res


sol = Solution3()
print(sol.combinationSum3(2, 9))

# sol = Solution3()
# tests = [
#     # ([1, 2, 3, 1], 3, 0, True),
#     # ([1, 0, 1, 1], 1, 2, True),
#     ([1, 5, 9, 1, 5, 9], 2, 3, False),
#     # ([1, 4, 9, 1, 4, 9], 1, 3, True),
#     # ([-1, -1], 1, -1, False),
#     # ([1, 3, 6, 2], 1, 2, True),
# ]

# for i, (nums, k, t, ans) in enumerate(tests):
#     res = sol.containsNearbyAlmostDuplicate(nums, k, t)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
