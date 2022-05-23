# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def countSubstrings(self, s: str) -> int:
        """LeetCode 647

        Like I said yesterday, if I attack a DP problem from the right angle,
        it is not difficult. This problem is a prime example of it. The DP
        concept here is that dp[i] is an array of indices, in which each index
        can form a palindrome from the index to i. The for i + 1, we only need
        to check all the indices from dp[i] and compare s[i] with s[index - 1].
        The tricky part is that when s[i] == s[i - 1], this situation must be
        considered separately.

        O(N^2), 134 ms, faster than 76.37%
        """
        res, pre = 1, [0]
        for i in range(1, len(s)):
            pre = [j - 1 for j in pre if j > 0 and s[i] == s[j - 1]]
            if s[i] == s[i - 1]:
                pre.append(i - 1)
            pre.append(i)
            res += len(pre)
        return res

        
sol = Solution()
tests = [
    ("abc", 3),
    ("aaa", 6),
]

for i, (s, ans) in enumerate(tests):
    res = sol.countSubstrings(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
