# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left
from functools import lru_cache


class Solution1:
    def numberOfArrays(self, s: str, k: int) -> int:
        """TLE
        """
        s = s.lstrip('0')
        nonzeros = []
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(len(s)):
            if s[i] != '0':
                if int(s[i]) <= k:
                    dp[i + 1] = dp[i]
                    for j in nonzeros[::-1]:
                        if int(s[j:i + 1]) <= k:
                            dp[i + 1] += dp[j]
                        else:
                            break
                    nonzeros.append(i)
                else:
                    break
            else:
                for j in nonzeros[::-1]:
                    if int(s[j:i + 1]) <= k:
                        dp[i + 1] += dp[j]
                    else:
                        break
        return dp[-1] % (10**9 + 7)


class Solution2:
    def numberOfArrays(self, s: str, k: int) -> int:
        """TLE

        Dear lord!
        """
        MOD = 10**9 + 7
        s = s.lstrip('0')
        k_dig = len(str(k))
        # all the indices of nonzero values in s.
        nonzeros = []
        # dp[i + 1] is total number of arrays in s[:i + 1]. Note that dp has
        # one more element than s. We set dp[0] to 1, which means if s[:i + 1]
        # in its entirety is smaller than k, we count that as one array as well.
        # Note that the index for dp is 1 larger than that for s
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        
        presum = [0]

        def compute(cur_i: int) -> int:
            idx_l = bisect_left(nonzeros, cur_i - k_dig + 1)
            idx_r = len(nonzeros) - 1
            if idx_l < len(nonzeros):
                if int(s[nonzeros[idx_l]:cur_i + 1]) > k:
                    idx_l += 1
                if idx_l <= idx_r:
                    dp[cur_i + 1] += (
                        presum[nonzeros[idx_r] + 1] -
                        presum[nonzeros[idx_l] - 1 + 1]
                    )

        for i in range(len(s)):
            # print(i, dp, presum)
            if s[i] != '0':
                presum.append(presum[-1] + dp[i])
                if int(s[i]) <= k:
                    dp[i + 1] = dp[i]
                    compute(i)
                    nonzeros.append(i)
                    
                else:
                    break
            else:
                presum.append(presum[-1])
                compute(i)
                
        return dp[-1] % MOD


class Solution3:
    def numberOfArrays(self, s: str, k: int) -> int:
        """LeetCode 1416

        My dear lord! This is not difficult at all, but my initial thought was
        just completely off the mark.

        The logic of top down is very straightforward. dp[i] is the total number
        of arrays in s[i:].

        To compute dp[i], we can use s[i] by itself, then we need to find
        dp[i + 1]. Or we can use s[i:i + 2], then we need to find dp[i + 2], etc
        Until s[i:i + ?] exceeds k.

        The edge case is when i goes out of bound or when s[i] == '0'. In the
        first case, we have found one array, thus returning 1. In the second
        case, it is impossible to start an array with a number of leading zero.
        So we return 0.

        That's it. And since we memoize dp, the runtime is O(NlogK). I cannot
        believe I missed this problem so badly. It is not difficult at all!!

        1490 ms, faster than 71.23%
        """
        N = len(s)
        s = s.lstrip('0')
        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def dp(idx: int) -> int:
            if idx == N:
                return 1
            if s[idx] == '0':
                return 0
            acc = int(s[idx])
            res = 0
            while acc <= k:
                res = (res + dp(idx + 1)) % MOD
                idx += 1
                if idx < N:
                    acc = acc * 10 + int(s[idx])
                else:
                    break
            return res

        return dp(0)


class Solution4:
    def numberOfArrays(self, s: str, k: int) -> int:
        """Bottom up, do not do int(str) to obtain a number for comparison with
        k. Do it iteratively.

        O(NlogK), 1804 ms, faster than 40.26%
        """
        MOD = 10**9 + 7
        s = s.lstrip('0')
        k_dig = len(str(k))
        dp = [0] * (1 + len(s))
        dp[0] = 1
        for i in range(len(s)):
            acc = 0
            tens = 1
            for j in range(i, max(-1, i - k_dig), -1):
                cur = int(s[j])
                if cur:
                    acc = cur * tens + acc
                    if acc <= k:
                        dp[i + 1] = (dp[i + 1] + dp[j]) % MOD
                    else:
                        break
                tens *= 10
            
        return dp[-1]


sol = Solution4()
tests = [
    ('1000', 10000, 1),
    ('1000', 10, 0),
    ('1317', 2000, 8),
    ("97009847265580", 116, 0),
    ("97009847265580", 9999999, 960),
    ("9700980", 9999999, 8),
    ("970098580", 9999999, 30),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.numberOfArrays(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
