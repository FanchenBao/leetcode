# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
from bisect import bisect_right


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        indices = defaultdict(list)
        prefsum = {}
        for i, a in enumerate(arr):
            indices[a].append(i)
            if a not in prefsum:
                prefsum[a] = [i]
            else:
                prefsum[a].append(i + prefsum[a][-1])
        res = []
        for i, a in enumerate(arr):
            idx = bisect_right(indices[a], i) - 1
            # count of smaller, count of larger
            sc, lc = idx, len(indices[a]) - idx - 1
            ss = prefsum[a][idx - 1] if idx > 0 else 0  # sum of smaller
            ls = prefsum[a][-1] - prefsum[a][idx]  # sum of larger
            res.append(i * sc - ss + ls - i * lc)
        return res
        

sol = Solution()
tests = [
    ([2,1,3,1,2,3,3], [4,2,7,2,4,4,5]),
    ([10,5,10,10], [5,0,3,4]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.getDistances(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
