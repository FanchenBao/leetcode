# from pudb import set_trace; set_trace()
from typing import List
import math
from collection import defaultdict


class WordDictionary:

    def __init__(self):
        """LeetCode 211

        Use Trie and BFS. We also implement an early termination of BFS.

        6478 ms, faster than 89.30%
        """
        trie = lambda: defaultdict(trie)
        self.root = trie()

    def addWord(self, word: str) -> None:
        """O(N), where N = len(word)"""
        node = self.root
        for le in word:
            node = node[le]
        node['*'] = True

    def search(self, word: str) -> bool:
        """Worst case is word == '...', and there is no overlap in the trie.
        Then we have to go through every single node in the trie.

        The best case is we go down a single path in trie during BFS, so the
        time complexity is the height of the trie.
        """
        queue = [self.root]
        for i, le in enumerate(word):
            if not queue:
                return False
            tmp = []
            for node in queue:
                if i == len(word) - 1 and le in node and '*' in node[le]:
                    return True
                if le != '.':
                    if le in node:
                        tmp.append(node[le])
                else:
                    for k in node:
                        if k != '*':
                            tmp.append(node[k])
            queue = tmp
        return any('*' in node for node in queue)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
