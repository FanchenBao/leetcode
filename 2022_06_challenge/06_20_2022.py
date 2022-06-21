# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
from functools import reduce


class Solution1:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """LeetCode 820

        Two words can share the same encoding if the shorter word is the suffix
        of the longer word. The problem is converted to build a suffix trie,
        and add up the length of each path in the trie.

        O(N), where N is the total number of letters in words.
        181 ms, faster than 79.07%
        """
        trie = lambda: defaultdict(trie)
        res = 0
        root = trie()
        for word in words:
            node = root
            for i in range(len(word) - 1, -1, -1):
                node = node[word[i]]
                if '*' in node:
                    res -= (node['*'] + 1)
                    del node['*']
            if len(node) == 0:
                node['*'] = len(word)
                res += len(word) + 1
        return res


class Solution2:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """This is the amazingly short solution using Trie and reduce"""
        Trie = lambda: defaultdict(Trie)
        root = Trie()
        # this set up requires that the input has no duplication
        non_dupes = list(set(words))
        last_nodes = [reduce(dict.__getitem__, w[::-1], root) for w in non_dupes]
        # if a node in last_nodes is empty, that means it is the last node of
        # the path
        return sum(len(non_dupes[i]) + 1 for i, node in enumerate(last_nodes) if not node)


sol = Solution2()
tests = [
    (["time", "me", "bell"], 10),
    (['t'], 2),
    (["time","a","pytime","me"], 9),
    (["time","aptime","me"], 7),
    (["time", "timebel", "bell"], 18),
    (["time", "time", "time", "time"], 5),
]

for i, (words, ans) in enumerate(tests):
    res = sol.minimumLengthEncoding(words)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
