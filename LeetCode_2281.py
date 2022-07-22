# from pudb import set_trace; set_trace()
from typing import List


class Solution:
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
