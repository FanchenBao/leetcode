# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def can_transform(self, w1: str, w2: str) -> bool:
        return sum(l1 != l2 for l1, l2 in zip(w1, w2)) == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """TLE. :-(
        """
        if endWord not in wordList:
            return 0
        n = len(wordList)
        transform_table = [[None] * n for _ in range(n)]
        min_steps = [n + 1]
        all_indices = set(range(n))

        def dfs(cur_idx, remain_indices, steps):
            if wordList[cur_idx] == endWord:
                min_steps[0] = min(min_steps[0], steps)
            else:
                for i in list(remain_indices):
                    if transform_table[cur_idx][i] is None:
                        transform_table[cur_idx][i] = self.can_transform(
                            wordList[cur_idx], wordList[i],
                        )
                    if transform_table[cur_idx][i]:
                        remain_indices.remove(i)
                        dfs(i, remain_indices, steps + 1)
                        remain_indices.add(i)

        for i, word in enumerate(wordList):
            if self.can_transform(beginWord, word):
                all_indices.remove(i)
                dfs(i, all_indices, 2)
                all_indices.add(i)

        return min_steps[0] if min_steps[0] < n + 1 else 0


sol = Solution()
tests = [
    ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'], 5),
    ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log'], 0),
    ('hot', 'dog', ['hot', 'dog'], 0),
]

for i, (beginWord, endWord, wordList, ans) in enumerate(tests):
    res = sol.ladderLength(beginWord, endWord, wordList)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
