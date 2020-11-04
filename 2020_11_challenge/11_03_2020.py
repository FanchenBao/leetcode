# from pudb import set_trace; set_trace()
from typing import List
from itertools import groupby


class Solution1:
    def maxPower(self, s: str) -> int:
        """Cheating method, using groupby method. 33% ranking"""
        return max(len(list(reps)) for _, reps in groupby(s))


class Solution2:
    def maxPower(self, s: str) -> int:
        """Non cheating method"""
        pre = ''
        res, temp = 0, 1
        for cur in s:
            if cur == pre:
                temp += 1
            else:
                temp = 1
                pre = cur
            res = max(res, temp)
        return res


sol = Solution2()
tests = [
    ('leetcode', 2),
    ('abbcccddddeeeeedcba', 5),
    ('triplepillooooow', 5),
    ('hooraaaaaaaaaaay', 11),
    ('tourist', 1),
]

for i, (s, ans) in enumerate(tests):
    res = sol.maxPower(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
