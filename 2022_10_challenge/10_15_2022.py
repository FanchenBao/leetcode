# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math
from itertools import groupby
from functools import lru_cache
from collections import Counter


class Solution1:
    def __init__(self):
        self.count =[]
        for i in range(101):
            if i <= 1:
                self.count.append(i)
            elif 1 < i <= 9:
                self.count.append(2)
            elif 9 < i <= 99:
                self.count.append(3)
            else:
                self.count.append(4)

    def get_encoding_len(self, inputs: List):
        pre_le, pre_c = inputs[0]
        res = 0
        for i in range(1, len(inputs)):
            le, c = inputs[i]
            if c > 0:
                if le == pre_le:
                    pre_c += c
                else:
                    res += self.count[pre_c]
                    pre_le, pre_c = le, c
        res += self.count[pre_c]
        return res

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """TLE
        """
        lst = [[le, len(list(g))] for le, g in groupby(s)]
        
        def helper(idx: int, rem: int) -> int:
            if rem == 0 or idx == len(lst):
                return self.get_encoding_len(lst)
            res = helper(idx + 1, rem)  # not change lst[idx]
            c = lst[idx][1]
            # reduce by 1
            if c == 100:
                lst[idx][1] = 99
                res = min(res, helper(idx + 1, rem - 1))
            elif 10 <= c < 100:
                r = c - 9
                if r <= rem:
                    lst[idx][1] = 9
                    res = min(res, helper(idx + 1, rem - r))
            elif 1 < c < 10:
                r = c - 1
                if r <= rem:
                    lst[idx][1] = 1
                    res = min(res, helper(idx + 1, rem - r))
            else:
                lst[idx][1] = 0    
                res = min(res, helper(idx + 1, rem - 1))
            lst[idx][1] = c

            # reduce by 2
            if c == 100:
                if 91 <= rem:
                    lst[idx][1] = 9
                    res = min(res, helper(idx + 1, rem - 91))
            elif 10 <= c < 100:
                r = c - 1
                if r <= rem:
                    lst[idx][1] = 1
                    res = min(res, helper(idx + 1, rem - r))
            elif 1 < c < 10:
                if c <= rem:
                    lst[idx][1] = 0
                    res = min(res, helper(idx + 1, rem - c))
            lst[idx][1] = c

            # reduce by 3
            if c == 100:
                if 99 <= rem:
                    lst[idx][1] = 1
                    res = min(res, helper(idx + 1, rem - 99))
            elif 10 <= c < 100:
                if c <= rem:
                    lst[idx][1] = 0
                    res = min(res, helper(idx + 1, rem - c))
            lst[idx][1] = c

            # reduce by 4
            if c == 100 and c <= rem:
                lst[idx][1] = 0
                res = min(res, helper(idx + 1, rem - c))

            return res

        return helper(0, k)


class Solution2:
    def encoding_len(self, num_repeats: int) -> int:
        if num_repeats == 1:
            return 1
        if num_repeats < 10:
            return 2
        if num_repeats < 100:
            return 3
        return 4

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """LeetCode 1531

        I wasn't able to do it, so I checked out this solution

        https://leetcode.com/problems/string-compression-ii/discuss/756022/C%2B%2B-Top-Down-DP-with-explanation-64ms-short-and-clear

        Truely brilliant solution. I posted a comment explaining my thought
        process of understanding the solution.

        https://leetcode.com/problems/string-compression-ii/discuss/756022/C++-Top-Down-DP-with-explanation-64ms-short-and-clear/1645542

        O(N^2 * K), 3140 ms, faster than 55.83%
        """

        @lru_cache(maxsize=None)
        def dp(idx: int, rem: int) -> int:
            """get the min encoding length from s[idx:] with rem number of
            letters to remove
            """
            if rem < 0:  # impossible case
                return math.inf
            if len(s) - idx <= rem:  # we can remove all the letters in s[idx:]
                return 0
            res = math.inf
            counter = Counter()
            max_count = 0
            for i in range(idx, len(s)):
                counter[s[i]] += 1
                max_count = max(max_count, counter[s[i]])
                # number of letters to remove in s[idx:i + 1] such that we have
                # max_count repeats of a single letter
                r = i - idx + 1 - max_count
                res = min(
                    res, self.encoding_len(max_count) + dp(i + 1, rem - r),
                )
            return res

        return dp(0, k)


sol = Solution2()
tests = [
    ("aaabcccd", 2, 4),
    ("aabbaa", 2, 2),
    ("aaaaaaaaaaa", 0, 3),
    ('aabaa', 2, 2),
    ('a', 1, 0),
    ("abcdefghijklmnopqrstuvwxyz", 16, 10),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.getLengthOfOptimalCompression(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
