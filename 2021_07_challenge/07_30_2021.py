# from pudb import set_trace; set_trace()
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0

class MapSum:

    def __init__(self):
        """
        LeetCode 677

        I didn't understand the problem fully. It requires that if the current
        key already exists, we must OVERWRITE the original value. This means
        when updating the Trie (by the way, we use Trie as the data structure
        because of the prefix of letters), we need to add a delta, instead of
        the given val. I missed two big parts. First is the delta, and the
        second is to update the key-value pair when the same key shows up.

        I also missed a small part regarding when a prefix sum request has the
        prefix not exist in the Trie. In this situation, we need to return 0,
        but I don't think the problem is very clear about this.

        Anyway, this is similar to a BIT but with a Trie as the underlying data
        structure.

        Time complexity for insert and prefix is both O(N), where N is the length
        of the given key or prefix.

        28 ms, 88% ranking.
        """
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        node = self.root
        for le in key:
            if le not in node.children:
                node.children[le] = TrieNode()
            node = node.children[le]
            node.val += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for le in prefix:
            if le in node.children:
                node = node.children[le]
            else:
                return 0
        return node.val


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
