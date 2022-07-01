# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict, Counter
import heapq


class Solution:
    def largestVariance(self, s: str) -> int:
        counter = Counter(s)
        if min(counter.values()) == 1:
            return max(counter.values()) - 1
        precount = defaultdict(lambda: [0] * (len(s) + 1))
        for i, le in enumerate(s):
            for u in counter:
                precount[u][i + 1] = precount[u][i] + int(u == le)
        res = 0
        indices = defaultdict(list)
        for i in range(len(s)):
            c = 1
            for j in indices[s[i]][::-1]:
                res = max(max(pc[i] - pc[j + 1] for pc in precount.values()) - c, res)
                c += 1
            res = max(max(pc[i] - c for pc in precount.values()), res)
            indices[s[i]].append(i)
        return res


sol = Solution()
tests = [
    ("aababbb", 3),
    ("abcde", 0),
]

for i, (s, ans) in enumerate(tests):
    res = sol.largestVariance(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
