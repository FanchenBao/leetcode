# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Trie:

    def __init__(self):
        """LeetCode 208

        We use the trick this time (I did not use the trick last time and I
        claimed last time that using defaultdict trick was not going to work.
        Now look who is the joker). Also set up a helper function self._search
        to simplify the implementation of self.search and self.startswith.

        128 ms, faster than 93.24%
        """
        trie = lambda: defaultdict(trie)
        self.root = trie()

    def insert(self, word: str) -> None:
        node = self.root
        for le in word:
            node = node[le]
        node['*'] = True

    def _search(self, s: str) -> Dict:
        node = self.root
        for le in s:
            if le not in node:
                return {}
            node = node[le]
        return node

    def search(self, word: str) -> bool:
        node = self._search(word)
        return '*' in node

    def startsWith(self, prefix: str) -> bool:
        return len(self._search(prefix)) > 0



sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
