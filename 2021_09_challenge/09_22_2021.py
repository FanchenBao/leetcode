# from pudb import set_trace; set_trace()
from typing import List, Set
from collections import defaultdict


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """LeetCode 1239

        Not very difficult, but we got stuck on when to check the result.
        First of all, we turn each string into a set, and only keep the strings
        that have unique letters themselves.

        Then we generate a directed graph for any pair that do not share letters

        Then we DFS this directed graph, keeping rack of the current set of
        letters that have been concatenated already. For each word, we check
        whether we can concatenate the next child. And for each word, we also
        record in res the current size of the concatenation.

        Time complexity O(N^2). 88 ms, 88% ranking.

        UPDATE: the official solution says the time complexity is O(2^N), which
        I believe.

        I still prefer my way of reasoning. One optimization is to use bit
        manipulation to handle all the work done by set. It is very ingeneous
        to hide the length of the current concatenated size within the first 6
        bits, and use the remaning 26 bits to represent the actual
        word/concatenation. This is pretty smart. I think I can replace all
        the set operation with bit manipulation without changing the core of
        this algo. But I am not doing it today.
        """
        arr_set = [set(a) for a in arr if len(a) == len(set(a))]
        graph = defaultdict(list)
        for i in range(len(arr_set)):
            for j in range(i + 1, len(arr_set)):
                if not arr_set[i].intersection(arr_set[j]):
                    graph[i].append(j)
        self.res = 0

        def dfs(node: int, concat: Set[str]) -> None:
            new_concat = concat.union(arr_set[node])
            for child in graph[node]:
                if not new_concat.intersection(arr_set[child]):
                    dfs(child, new_concat)
            self.res = max(self.res, len(new_concat))

        for i in range(len(arr_set)):
            dfs(i, set())
        return self.res


sol = Solution()
tests = [
    (['un', 'iq', 'ue'], 4),
    (['cha', 'r', 'act', 'ers'], 6),
    (['abcdefghijklmnopqrstuvwxyz'], 26),
    (['ogud', 'ejipchfydrgl', 'b', 'kjxmzhnuoisgqvawel', 'mizlcgdqebwuotfnk', 'bjvkrgeozidytquchlw', 'tzjqwumkirxeal', 'x', 'rkpuabmo'], 20),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.maxLength(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
