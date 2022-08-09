# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """LeetCode 823

        Naive DP solution. The key to speed things up is to exit the second
        loop early and double count each non-identical left and right children.

        dp[q] is the number of binary trees formed with q at its root.

        O(N^2), 274 ms, faster than 93.94% 
        """
        dp = Counter(arr)
        arr.sort()
        N = len(arr)
        for i in range(N):
            for j in range(i):
                q, r = divmod(arr[i], arr[j])
                if q < arr[j]:  # early termination
                    break
                if r == 0 and q in dp:
                    dp[arr[i]] += dp[arr[j]] * dp[q]
                    if arr[j] != q:
                        dp[arr[i]] += dp[arr[j]] * dp[q]  # swap left and right
        return sum(dp.values()) % 1000000007


sol = Solution()
tests = [
    ([2,4], 3),
    ([2,4,5,10], 7),
    ([2,3,4,5,6,7,8,9,10], 19),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.numFactoredBinaryTrees(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
