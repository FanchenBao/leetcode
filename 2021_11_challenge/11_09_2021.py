# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict, Counter
from random import choice
from string import ascii_lowercase
from functools import reduce


class Solution0:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        word_sets = [set(w) for w in words]
        puz_sets = [(set(p), p[0]) for p in puzzles]
        return [sum(p.union(w) == p and p0 in w for w in word_sets) for p, p0 in puz_sets]


class Solution1:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """LeetCode 1178

        Trie with BFS works. One thing that gave me LOTS OF trouble: duplicates
        in words. This bug took me a good 10 min of manual work to resolve.

        Build the trie takes O(Mk), where M is the length of words and k the
        average length of each word. BFS takes O(NMK) in the worst case, where
        N is the length of puzzles. But on average, BFS should take much shorter
        to run because we can terminate the search on some branches early.

        3396 ms, 8% ranking.
        """
        trie = lambda: defaultdict(trie)
        root = trie()
        for word, count in Counter(words).items():
            node = root
            for le in word:
                node = node[le]
            node['#'] = count  # indicate end of word
        res = []
        for puz in puzzles:
            pset = set(puz)
            res.append(0)
            queue = [(root, False)]
            while queue:
                temp = []
                for node, contain_first in queue:
                    if '#' in node:
                        res[-1] += contain_first * node['#']
                    for le in node:
                        if le in pset:
                            temp.append((node[le], contain_first | (le == puz[0])))
                queue = temp
        return res



class Solution2:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """Trie with DFS
        """
        trie = lambda: defaultdict(trie)
        root = trie()
        for word, count in Counter(words).items():
            node = root
            for le in word:
                node = node[le]
            node['#'] = count  # indicate end of word

        def dfs(node, p, contain_first: bool) -> None:
            res = contain_first * node.get('#', 0)
            for le in node:
                if le in p:
                    res += dfs(node[le], p, contain_first | (le == p[0]))
            return res

        return [dfs(root, p, False) for p in puzzles]


class Solution3:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """Hashset with bitmap and combination of each puzzle.

        This is the official solution. Very good!

        O(MP + N * 2^Q) 82% ranking. M = len(words), P = average word length,
        N = len(puzzles), Q = average puzzle length
        """
        # Turn each word into its bitmap format
        counter = Counter()
        for w in words:
            counter[reduce(lambda a, b: a | (1 << ord(b) - 97), w, 0)] += 1
        res = []
        for p in puzzles:
            # Obtain all the combination of all possible bitmap repr of puzzle
            # while always keeping the first letter present
            comb = [1 << ord(p[0]) - 97]
            for le in p[1:]:
                comb += [c | (1 << ord(le) - 97) for c in comb]
            # For a word to match the puzzle, its bitmap must exist as one of
            # the bitmap combinations in comb. Instead of going through all the
            # words, we can go through all the combinations, which is much
            # smaller than the length of words, to check how many of it exists
            # in words. This can be accomplished with the counter
            res.append(sum(counter[c] for c in comb))
        return res


sol0 = Solution0()
sol = Solution3()
tests = [
    (["aaaa","asas","able","ability","actt","actor","access"], ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]),
    (["apple","pleas","please"], ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]),
    (["sgma","sgma"],["grsamet"]),
]
# num_tests = 1000
# len_puzzles = 10
# len_words = 100
# len_word = 50
# len_puz = 7
# tests = [
#     (
#         [''.join(choice(ascii_lowercase) for _ in range(len_word)) for _ in range(len_words)],
#         [''.join(choice(ascii_lowercase) for _ in range(len_puz)) for _ in range(len_puzzles)],
#     ) for _ in range(num_tests)
# ]

for i, (words, puzzles) in enumerate(tests):
    res = sol.findNumOfValidWords(words, puzzles)
    ans = sol0.findNumOfValidWords(words, puzzles)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
