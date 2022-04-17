# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        res = 0
        for v in counter.values():
            if v == 1:
                return -1
            if v % 3 == 0:
                res += v // 3
            else:
                res += v // 3 + 1
        return res


sol = Solution()
tests = [
    ([2,2,3,3,2,4,4,4,4,4], 4),
    ([2, 3, 3], -1),
]

for i, (tasks, ans) in enumerate(tests):
    res = sol.minimumRounds(tasks)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
