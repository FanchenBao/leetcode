# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def countVowelStrings(self, n: int) -> int:
        """LeetCode 1641

        There is a pattern to this. given a list of strings of length n - 1,
        for length n, 'a' can be added to all of the strings of length n - 1;
        'e' can be added to all but those starting with 'a'; i can be added
        to all but htose starting with 'a' or 'e', etc. Using this observation,
        we can come up with a pattern of how the number of strings starting
        with each increasing vowel can be formulated.

        O(5N), 42 ms, faster than 58.32%
        """
        count = [1] * 5
        for _ in range(n - 1):
            s = sum(count)
            for i in range(5):
                temp, count[i] = count[i], s
                s -= temp
        return sum(count)


class Solution2:
    def countVowelStrings(self, n: int) -> int:
        """DP solution. Building up a prefix sum from 'u' to 'a'
        """
        dp = list(range(1, 6))
        for _ in range(n - 1):
            for i in range(1, 5):
                dp[i] += dp[i - 1]
        return dp[-1]


class Solution3:
    def countVowelStrings(self, n: int) -> int:
        """Combination solution. Read my own explanation here:

        https://leetcode.com/problems/count-sorted-vowel-strings/discuss/918498/JavaC++Python-DP-O(1)-Time-and-Space/822478
        """
        return math.comb(n + 4, 4)
        
        

sol = Solution3()
tests = [
    (1, 5),
    (2, 15),
    (3, 35),
]

for i, (n, ans) in enumerate(tests):
    res = sol.countVowelStrings(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
