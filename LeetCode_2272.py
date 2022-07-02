# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict, Counter
import heapq
from itertools import groupby, zip_longest


class Solution:
    def largestVariance(self, s: str) -> int:
        trfmed = [(k, len(list(g))) for k, g in groupby(s)]
        conseq_counts = defaultdict(list)
        order = []
        max_conseq = defaultdict(int)
        res = 0
        for le, c in trfmed:
            if le not in conseq_counts:
                order.append(le)
            conseq_counts[le].append(c)
            max_conseq[le] = max(max_conseq[le], c)
        if len(order) == 1:
            return 0
        for i in range(len(order)):
            for j in range(i + 1, len(order)):
                presum = [0]
                lei, lej = order[i], order[j]
                has_b = True
                for a, b in zip_longest(conseq_counts[lei], conseq_counts[lej]):
                    if a and b:
                        presum.append(presum[-1] + a)
                        presum.append(presum[-1] - b)
                    elif not a and b:
                        presum[-1] -= b
                    elif a and not b:
                        if has_b:  # previously b exists
                            presum.append(presum[-1] + a)
                        else:  # previously b already not exists
                            presum[-1] += a
                        has_b = False
                cur_min = min(presum[:3])
                cur_max = max(presum[:3])
                res = max(res, abs(presum[2]), max_conseq[lei] - 1, max_conseq[lej] - 1)
                for k in range(3, len(presum)):
                    res = max(res, abs(presum[k] - cur_min), abs(presum[k] - cur_max))
                    cur_min = min(cur_min, presum[k])
                    cur_max = max(cur_max, presum[k])
        return res


sol = Solution()
tests = [
    ("aababbb", 3),
    ("abcde", 0),
    ("icexiahccknibwuwgi", 3),
    ("dsyemilsuwhciclqwprizywgkwkbgcqhtcwfvlw", 5),
]

for i, (s, ans) in enumerate(tests):
    res = sol.largestVariance(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
