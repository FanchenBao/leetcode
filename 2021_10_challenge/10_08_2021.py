# from pudb import set_trace; set_trace()
from typing import List, Dict, Optional


class Trie:
    """LeetCode 208

    We have solved this problem before. Initially I was trying to use a smart
    way to set up the Trie nodes, but using defaultdict seems to be problematic.
    It turns out using a vanila dictionary is good enough and pretty easy to
    implement. One important trick is to set up a sentinel to indicate the end
    of a word. In the current implementation, we set '#' to true to signal that
    the current node represents the end of a word.

    128 ms, 93% ranking.

    UPDATE: following the official solution, we create a helper function called
    _search_prefix which returns the last maching node if it exists, or None if
    there is a mismatch. Then we can use _search_prefix to handle search and
    startsWith more easily.
    """
    def __init__(self):
        self.root = {'#': False}

    def insert(self, word: str) -> None:
        node = self.root
        for le in word:
            if le not in node:
                node[le] = {'#': False}
            node = node[le]
        node['#'] = True

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node is not None and node['#']

    def startsWith(self, prefix: str) -> bool:
        node = self._search_prefix(prefix)
        return node is not None

    def _search_prefix(self, prefix: str) -> Optional[Dict[str, Dict]]:
        node = self.root
        for le in prefix:
            if le in node:
                node = node[le]
            else:
                return None
        return node


trie = Trie()
trie.insert("apple")
print(trie.root)
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.root)
print(trie.search("app"))
print(trie.search("apple"))

# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
