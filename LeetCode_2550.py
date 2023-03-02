# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def monkeyMove(self, n: int) -> int:
        """I see why people hate this problem. It's essentially a test of
        whether one knows how to write a fast power algorithm. I knew its
        existence, but I forgot how to write it.

        But that is not all. There is another trick at the end when the returned
        value of fast power needs to be further processed before minus 2.

        O(logN), 31 ms, faster than 66.42%
        """
        MOD = 10**9 + 7

        def fast_power(base: int, power: int, mod: int) -> int:
            """Learned from https://www.rookieslab.com/posts/fast-power-algorithm-exponentiation-by-squaring-cpp-python-implementation

            I've done this before many times, but still couldn't write it from
            scratch.
            """
            res = 1
            while power:
                if power % 2:
                    res = (res * base) % mod
                # notice that we intentionally skip the else condition
                base = (base * base) % mod
                power //= 2
            return res

        # pay attention!! fast_power with mod might return smaller than 2.
        return (fast_power(2, n, MOD) + MOD - 2) % MOD


class Solution2:
    def monkeyMove(self, n: int) -> int:
        """I forgot the built-in pow function has MOD support.

        23 ms, faster than 96.24%
        """
        MOD = 10**9 + 7
        return (pow(2, n, MOD) + MOD - 2) % MOD


sol = Solution2()
tests = [
    (3, 6),
    (4, 14),
    (500000003, 1000000006)
]

for i, (n, ans) in enumerate(tests):
    res = sol.monkeyMove(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
