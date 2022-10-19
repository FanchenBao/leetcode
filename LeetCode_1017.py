# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def baseNeg2(self, n: int) -> str:
        """Definitely not a good solution. Overall, we didn't bifurcate on each
        occassion, but still the savings from the two special cases where we
        don't have to bifurcate don't seem too big. I will have to check the
        solution for better ideas.

        Also, limiting the highest power significantly reduces runtime.

        O(2^N), 511 ms, faster than 6.32%
        """
        if n == 0:
            return '0'
        
        @lru_cache(maxsize=None)
        def dfs(val: int, p: int) -> str:
            if val == 0:
                return '0' * (p + 1)
            cur = (-2)**p
            if val == cur:
                return '1' + '0' * p
            if p == 0:
                return '*'  # impossible case
            if (val > 0 and p % 2) or (val < 0 and p % 2 == 0):
                return '0' + dfs(val, p - 1)
            op1 = '1' + dfs(val - cur, p - 1)
            if op1[-1] != '*':
                return op1
            return '0' + dfs(val, p - 1)

        l = int(math.log2(n))
        l += 1 if l % 2 else 2
        return dfs(n, l).lstrip('0')


class Solution2:
    def baseNeg2(self, n: int) -> str:
        """The trick is .... the same as base 2. But I forgot that base 2 can
        be converted using remainder. We can do the same with base -2, except
        when the remainder is negative, which can only be -1, we remove another
        -2 from it to make it positive, and add one to the quotient. We keep
        doing this until the quotient is zero.

        O(logN), 63 ms, faster than 20.00%
        """
        if n == 0:
            return '0'
        q = n
        res = []
        while q:
            q, r = divmod(q, -2)
            if r < 0:
                q += 1
                res.append('1')
            else:
                res.append('0')
        return ''.join(res[::-1])


sol = Solution2()
tests = [
    (2, '110'),
    (3, '111'),
    (4, '100'),
    (7, '11011'),
]

for i, (n, ans) in enumerate(tests):
    res = sol.baseNeg2(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
