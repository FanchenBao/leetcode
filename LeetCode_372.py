# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def superPow(self, a: int, b: List[int]) -> int:
        """The insight is that we can reduce the power by two at each iteration.
        This means, givan a^p, we turn the problem into (a^2)^?. Depending on
        whether p is even or odd, we will have

        (a^2)^? % m = ((a^2 % m)^(p // 2) * a ) % m, if p is odd
        (a^2)^? % m = ((a^2 % m)^(p // 2)) % m, if p is even

        We can continue doing this to reduce p until it is gone. Then we can
        compute the mod more easily.

        O(logP), where P is the total power computed from b.

        320 ms, 12% ranking

        UPDATE: surprisingly, I have come up with the right-to-left binary
        method as detailed here:

        https://en.wikipedia.org/wiki/Modular_exponentiation

        But the implementation can be improved.
        """
        m = 1337
        r = a % m
        p = int(''.join(str(bb) for bb in b))
        res = 1
        while p > 0:
            if p % 2:
                res = (res * r) % m
            p = p >> 1
            r = (r * r) % m
        return res


class Solution2:
    def superPow(self, a: int, b: List[int]) -> int:
        """The pow() built-in function is specifically for this"""
        p = int(''.join(str(bb) for bb in b))
        return pow(a, p, 1337)


sol = Solution1()
tests = [
    (2, [3], 8),
    (2, [1, 0], 1024),
    (1, [4, 3, 3, 8, 5, 2], 1),
    (2147483647, [2, 0, 0], 1198),
]

for i, (a, b, ans) in enumerate(tests):
    res = sol.superPow(a, b)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
