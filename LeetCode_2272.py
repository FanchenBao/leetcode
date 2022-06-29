# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution:
    def largestVariance(self, s: str) -> int:
        uniques = set(s)
        precount = {le: [0] for le in uniques}
        indices = {le: [] for le in uniques}
        for i, le in enumerate(s):
            for uniq in uniques:
                if le == uniq:
                    precount[uniq].append(1 + precount[uniq][-1])
                else:
                    precount[uniq].append(precount[uniq][-1])
            indices[le].append(i)
        tgt_le = min(indices, key=lambda le: len(indices[le]))
        for i, idx in enumerate(indices[tgt_le]):
            l = 0 if i == 0 else indices[tgt_le][i - 1]



        
sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
