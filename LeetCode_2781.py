# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
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




sol = Solution()
tests = [
    ('cbaaaabc', ['aaa', 'cb'], 4),
]

for i, (word, forbidden, ans) in enumerate(tests):
    res = sol.longestValidSubstring(word, forbidden)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
