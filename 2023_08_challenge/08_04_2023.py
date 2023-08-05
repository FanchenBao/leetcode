# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """LeetCode 139

        Build a Trie from wordDict, and then DP it. DP(idx) returns whether it
        is possible to break up s[idx:].

        I forgot to DP in my initial attempt.

        O(N^2 + M), where N = len(s) and M is the total number of letters in
        wordDict. 42 ms, faster than 94.01%
        """
        trie = lambda: defaultdict(trie)
        root = trie()
        for word in wordDict:
            node = root
            for le in word:
                node = node[le]
            node['*'] = True

        @lru_cache(maxsize=None)
        def helper(idx: int) -> bool:
            if idx == len(s):
                return True
            node = root
            for i in range(idx, len(s)):
                if s[i] not in node:
                    return False
                node = node[s[i]]
                if '*' in node and helper(i + 1):
                    return True
            return False

        return helper(0)


sol = Solution()
tests = [
    ("leetcode", ["leet","code"], True),
    ("applepenapple", ["apple","pen"], True),
    ("catsandog", ["cats","dog","sand","and","cat"], False),
]

for i, (s, wordDict, ans) in enumerate(tests):
    res = sol.wordBreak(s, wordDict)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
