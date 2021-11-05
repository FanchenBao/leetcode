# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def arrangeCoins(self, n: int) -> int:
        """LeetCode 441
        
        Math solution.
        """
        return int((math.sqrt(1 + 8 * n) - 1) / 2 )


class Solution2:
    def arrangeCoins(self, n: int) -> int:
        """Iterative"""
        res, s = 0, 0
        while s <= n:
            res += 1
            s += res
        return res - 1


class Solution3:
    def arrangeCoins(self, n: int) -> int:
        """Binary search
        
        Note that hi must be larger than n, because hi must be larger than the
        correct answer. Since n can be the correct answer, e.g. n = 1, we must
        make hi larger than n.
        """
        lo, hi = 0, n + 1
        while lo < hi:
            mid = (lo + hi) // 2
            cur = mid * (1 + mid) // 2
            if cur <= n:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1


sol = Solution3()
tests = [
    (5, 2),
    (8, 3),
    (10, 4),
    (1, 1)
]

for i, (n, ans) in enumerate(tests):
    res = sol.arrangeCoins(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
