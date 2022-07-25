# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate


class Solution1:
    def totalStrength(self, strength: List[int]) -> int:
        """O(N^2), TLE
        """
        dp = {strength[0]: [1, strength[0]]}
        res = strength[0] * strength[0]
        for i in range(1, len(strength)):
            cur = strength[i]
            tmp = {cur: [1, cur]}
            for k, v in dp.items():
                if k >= cur:
                    tmp[cur][0] += v[0]
                    tmp[cur][1] += v[1] + v[0] * cur
                else:
                    tmp[k] = [v[0], v[1] + v[0] * cur]
            dp = tmp
            for k, v in dp.items():
                res += k * v[1]
        return res


class Solution2:
    def totalStrength(self, strength: List[int]) -> int:
        N = len(strength)
        psum1 = [0] * N
        psum1[-1] = strength[-1]
        ps = strength[-1]
        for i in range(N - 2, -1, -1):
            ps += strength[i]
            psum1[i] = psum1[i - 1] + ps
        psum2 = list(accumulate(strenght))
        ps = 0
        dp = [0] * N
        stack = []



sol = Solution()
tests = [
    ([1,3,1,2], 44),
    ([5,4,6], 213),
]

for i, (strength, ans) in enumerate(tests):
    res = sol.totalStrength(strength)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
