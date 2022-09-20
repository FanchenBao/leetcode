# from pudb import set_trace; set_trace()
from typing import List, Tuple
from functools import lru_cache
from collections import defaultdict


class Solution1:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """LeetCode 718

        Multiple mistakes. First of all, I thought it was about subsequence, so
        I coded up LCS, but was marvellously wrong.

        Then I tried to code 1D DP directly but got hit by the direction. To
        not overwrite the values that haven't been used, one must go from
        right to left on each dp run.

        O(NM), 7661 ms, faster than 25.96%
        """
        M, N = len(nums1), len(nums2)
        dp = [0] * (N + 1)
        res = 0
        for i in range(1, M + 1):
            # go backwards so that we don't overwrite the values that haven't
            # been used
            for j in range(N, 0, -1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                else:
                    dp[j] = 0
            res = max(max(dp), res)
        return res


class Solution2:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """Binary search with rolling hash. Courtesy of official solution

        O((M + N * K)log(min(M, N))). 738 ms, faster than 93.13%
        """
        P, MOD = 113, 10**9 + 7
        M, N = len(nums1), len(nums2)

        def hash(nums: List[int], lo: int, hi: int) -> Tuple[int, int]:
            h = 0
            power = 1
            for i in range(lo, hi + 1):
                h = (h + nums[i] * power) % MOD
                power = power * P
            return h, power // P


        def check(guess: int) -> bool:
            """The goal is to obtain hashes of all subarry of size guess form
            nums1 and nums2, and check whether any of the hashes match.

            Note that the check goes from right to left. This way, we can avoid
            division when computing the next rolling hash.
            """
            num1_hashes = defaultdict(list)
            h1, power = hash(nums1, M - guess, M - 1)
            num1_hashes[h1].append(M - guess)
            for i in range(M - guess - 1, -1, -1):
                h1 = ((h1 - nums1[i + guess] * power) * P + nums1[i]) % MOD
                num1_hashes[h1].append(i)
            for j in range(N - guess, -1, -1):
                if j == N - guess:
                    h2, power = hash(nums2, j, N - 1)
                else:
                    h2 = ((h2 - nums2[j + guess] * power) * P + nums2[j]) % MOD
                if any(nums1[i:i + guess] == nums2[j:j + guess] for i in num1_hashes.get(h2, [])):
                    return True
            return False

        lo, hi = 0, min(len(nums1), len(nums2)) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1









sol = Solution2()
tests = [
    ([1,2,3,2,1], [3,2,1,4,7], 3),
    ([0,0,0,0,0], [0,0,0,0,0], 5),
    ([0,1,1,1,1], [1,0,1,0,1], 2),
    ([1,0,0,0,1], [1,0,0,1,1], 3),
    ([0,0,0,0,0,0,1,0,0,0], [0,0,0,0,0,0,0,1,0,0], 9),
]

for i, (nums1, nums2, ans) in enumerate(tests):
    res = sol.findLength(nums1, nums2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
