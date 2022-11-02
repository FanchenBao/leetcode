# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def is_diff_by_one(self, a: str, b: str) -> bool:
        return sum(int(la != lb) for la, lb in zip(a, b)) == 1

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """LeetCode 433

        This is the same as word ladder. Build a graph and then BFS.

        O(N), 63 ms, faster than 23.22% 

        UPDATE: turn bank into a set to remove any duplicates.
        50 ms, faster than 67.16%
        """
        if end not in bank:
            return -1
        queue = [start]
        visited = set([start])
        bank = set(bank)
        res = 0
        while queue:
            temp = []
            for g in queue:
                if g == end:
                    return res
                for b in bank:
                    if b not in visited and self.is_diff_by_one(g, b):
                        temp.append(b)
                        visited.add(b)
            queue = temp
            res += 1
        return -1
        

sol = Solution()
tests = [
    ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
    ("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"], 2),
    ("AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"], 3),
]

for i, (start, end, bank, ans) in enumerate(tests):
    res = sol.minMutation(start, end, bank)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
