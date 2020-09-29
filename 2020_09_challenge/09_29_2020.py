# from pudb import set_trace; set_trace()
from typing import List, Set
from functools import reduce
import operator


class Solution1:
    def dfs(self, left: int, s: str, wordSet: Set[str]) -> bool:
        """TLE, too simple, sometimes naive"""
        if left == len(s):
            return True
        for right in range(left, len(s)):
            if s[left:right + 1] in wordSet:
                if self.dfs(right + 1, s, wordSet):
                    return True
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dfs(0, s, set(wordDict))


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """54% ranking.
        Adapted from this solution:
        https://leetcode.com/explore/featured/card/september-leetcoding-challenge/558/week-5-september-29th-september-30th/3477/discuss/43788/4-lines-in-Python
        """
        pre_breaks = {-1}
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordDict and j - 1 in pre_breaks:
                    pre_breaks.add(i - 1)
        return len(s) - 1 in pre_breaks





sol = Solution2()
tests = [
    ('leetcode', ["leet", "code"], True),
    ('applepenapple', ["apple", "pen"], True),
    ('catsandog', ["cats", "dog", "sand", "and", "cat"], False),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"], False)
]

for i, (s, wordDict, ans) in enumerate(tests):
    res = sol.wordBreak(s, wordDict)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
