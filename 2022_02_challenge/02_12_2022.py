# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """LeetCode 127

        I have done this one at least two times in the past, and I have vivid
        memory of how it is solved. There are two obstacles. First, we need to
        figure out a way to quickly find connections among words. Second, we
        need to build a graph of all the words and run BFS or DFS to find the
        shortest path from beginWord to endWord, if both exist in the graph.

        The graph traversal part of this problem is not difficult. The challenge
        is to find a fast method to build the graph. I remember that we can
        replace each letter in the word with a '*'. If two words are identical
        after the letter at the same position is removed, they must differ by
        one letter, and thus have a connection.

        O(NK + N), where N = len(wordList) and K = length of each word.
        128 ms, 89% ranking.
        """
        adj = defaultdict(list)
        group = defaultdict(list)
        for w in set(wordList + [beginWord]):
            for i in range(len(w)):
                key = w[:i] + '*' + w[i + 1:]
                for pre_w in group[key]:
                    adj[pre_w].append(w)
                    adj[w].append(pre_w)
                group[key].append(w)
        if endWord not in adj or beginWord not in adj:
            return 0
        # BFS
        res = 1
        queue = [beginWord]
        seen = set([beginWord])
        while queue:
            temp = []
            for w in queue:
                if w == endWord:
                    return res
                for nei in adj[w]:
                    if nei not in seen:
                        temp.append(nei)
                        seen.add(nei)
            queue = temp
            res += 1
        return 0


sol = Solution()
tests = [
    ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
    ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
]

for i, (beginWord, endWord, wordList, ans) in enumerate(tests):
    res = sol.ladderLength(beginWord, endWord, wordList)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
