# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def is_chain(self, w1: str, w2: str) -> bool:
        for i in range(len(w2)):
            if w1 == (w2[:i] + w2[i + 1:]):
                return True
        return False

    def longestStrChain(self, words: List[str]) -> int:
        """LeetCode 1048

        This is a pure brute force solution. We first turn words into a dict
        with keys being the length of each word. Then, we go from low length to
        high length. In the dict, we also record the starting lvl that can reach
        each word. During lvl traversal, if a word at the current lvl finds a
        word in the next lvl that can be chained, we update the starting lvl of
        the next lvl word if its starting lvl is not smaller than the new update.
        This way, we keep the starting value of each word the smalleset possible.

        We update the res either when there is no next level, or a word cannot
        find its next chain.

        952 ms, 16% ranking. Pretty awful solution.
        """
        graph = defaultdict(list)
        for w in words:
            graph[len(w)].append([len(w), w])
        res = 0
        for lvl in sorted(graph.keys()):
            for st, w in graph[lvl]:
                if lvl + 1 not in graph:
                    res = max(res, lvl - st + 1)
                else:
                    for j in range(len(graph[lvl + 1])):
                        if self.is_chain(w, graph[lvl + 1][j][1]):
                            graph[lvl + 1][j][0] = min(graph[lvl + 1][j][0], st)
                        else:
                            res = max(res, lvl - st + 1)
        return res


class Solution2:
    def longestStrChain(self, words: List[str]) -> int:
        """The bottom up DP solution from official solution. Very nice and quite
        standard DP thinking.

        For each word, we find all of its possible predecessors, and look into
        the DP table to see the max length of chain ending at the predecessor.
        We pick the largest of the max length, plus 1, and then store in the DP
        table for the current word.

        O(NL^2), N is the number of words, L is the length of word.

        124 ms, 90% ranking.
        """
        dp = defaultdict(int)
        words.sort(key=lambda w: len(w))
        min_len = len(words[0])
        for w in words:
            if len(w) == min_len:
                dp[w] = 1
            else:
                for i in range(len(w)):
                    pre = w[:i] + w[i + 1:]
                    dp[w] = max(dp[w], dp[pre] + 1)
        return max(dp.values())


sol = Solution2()
tests = [
    (['a', 'b', 'ba', 'bca', 'bda', 'bdca'], 4),
    (['xbc', 'pcxbcf', 'xb', 'cxbc', 'pcxbc'], 5),
    (['a', 'aaa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa'], 4),
    (['a', 'b', 'ab', 'bac'], 2),
    (['ksqvsyq', 'ks', 'kss', 'czvh', 'zczpzvdhx', 'zczpzvh', 'zczpzvhx', 'zcpzvh', 'zczvh', 'gr', 'grukmj', 'ksqvsq', 'gruj', 'kssq', 'ksqsq', 'grukkmj', 'grukj', 'zczpzfvdhx', 'gru'], 7),
    (['a', 'ab', 'ac', 'bd', 'abc', 'abd', 'abdd'], 4),
]

for i, (words, ans) in enumerate(tests):
    res = sol.longestStrChain(words)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
