# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        pre = 0
        res = 0
        for row in bank:
            cur = row.count('1')
            if cur:
                res += pre * cur
                pre = cur
        return res


sol = Solution()
tests = [
    (["011001","000000","010100","001000"], 8),
    (["000","111","000"], 0)
]

for i, (bank, ans) in enumerate(tests):
    res = sol.numberOfBeams(bank)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
