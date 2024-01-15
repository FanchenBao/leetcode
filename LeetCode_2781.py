# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict
from functools import reduce


class Solution1:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        fset = set(forbidden)
        trie = lambda: defaultdict(trie)
        root = trie()
        # Create a trie for the forbidden words, in which each word is traversed
        # from right to left
        for w in fset:
            node = root
            for le in w[::-1]:
                node = node[le]
            node['*'] = True  # indicating the end of a word

        # print(root)

        # Sliding window to find the longest valid substring
        res = 0
        lo = 0
        for hi, le in enumerate(word):
            # Traverse the trie to identify whether any substring ending at
            # word[hi] appears in the trie. If some substring appears, we must
            # skip forward.
            node = root
            in_forbidden = True
            for i in range(hi, lo - 1, -1):
                if word[i] not in node:
                    in_forbidden = False
                    break
                node = node[word[i]]
                if '*' in node:
                    in_forbidden = True
                    break
            if in_forbidden:
                lo = i + 1
            else:
                res = max(res, hi - lo + 1)
            # print(lo, hi, le)
        return res


class Solution2:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        """
        This is the solution inspired by lee215
        https://leetcode.com/problems/length-of-the-longest-valid-substring/discuss/3771520/Python-HashMap-and-Trie-Solutions

        It is the same idea, but I really like his implementation, especially
        the creation of the Trie. Also, we will create the Trie from left to
        right, which means we need to iterate through word from right to left.

        O(M + N), 1582 ms, faster than 30.33%
        """
        # Amazingly succint way of creating a trie
        trie = lambda: defaultdict(trie)
        root = trie()
        for w in forbidden:
            reduce(dict.__getitem__, w, root)['*'] = True
        res, hi = 0, len(word)
        for lo in range(len(word) - 1, -1, -1):
            node = root
            for i in range(lo, hi):
                if word[i] not in node:
                    break
                node = node[word[i]]
                if '*' in node:
                    hi = i  # this means from lo to i, the substring is forbidden
                    break
            res = max(res, hi - lo)
        return res


sol = Solution2()
tests = [
    # ('cbaaaabc', ['aaa', 'cb'], 4),
    # ('acbc', ['cbc', 'acb', 'acb', 'acbc'], 2),
    ("aaaabaaacc", ["bcca","aaa","aabaa","baaac"], 4),
]

for i, (word, forbidden, ans) in enumerate(tests):
    res = sol.longestValidSubstring(word, forbidden)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
