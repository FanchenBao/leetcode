# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution1:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """A little bit DP.

        We record at each position, the longest Fib length ending in that num
        and its previous num.

        For each new position, we go back one by one and see if a Fib sequence
        can be formed by the previous value and the previous value's previous
        value.

        This search happens until the previous value is smaller or equal to
        half of the current value.

        O(N^2), 3814 ms, faster than 55.39%
        """
        arr_set = set(arr)
        dp = [{}, {}]  # dp[i] = {prev val in fib: longest fib length}
        res = 0
        for i in range(2, len(arr)):
            j = i - 1
            dp.append({})
            while j >= 0 and arr[j] > arr[i] // 2:
                pp = arr[i] - arr[j]
                if pp in dp[j]:
                    dp[-1][arr[j]] = dp[j][pp] + 1
                elif pp in arr_set:
                    dp[-1][arr[j]] = 3
                j -= 1
            if dp[-1]:
                res = max(res, max(dp[-1].values()))
        return res


class Solution2:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """Official solution's DP. It's cleaner than mine, but the idea is the
        same. We record the longest Fib for each pair of values. Then for any
        new pair, we find the pp, and produce the new pair's longest length by
        the previous pair's longest length plus one.

        O(N^2), 1435 ms, faster than 93.08%
        """
        arr_set = set(arr)
        dp = defaultdict(lambda: 2)  # any pair has Fib length of 2
        for i, a in enumerate(arr):
            for j in range(i):
                pp = a - arr[j]
                if pp in arr_set and pp < arr[j]:
                    dp[arr[j], a] = dp[pp, arr[j]] + 1
        return max(dp.values()) if dp else 0


sol = Solution2()
tests = [
    ([1,2,3,4,5,6,7,8], 5),
    ([1,3,7,11,12,14,18], 3),
    ([1,2,3,4,5,9,14,23,37], 7),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.lenLongestFibSubseq(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
