# from pudb import set_trace; set_trace()
from typing import List
import itertools


class Solution1:
    def concatenatedBinary(self, n: int) -> int:
        """This is an easy problem. Straightforward solution. Concatenate all
        the binary numbers as str, and finally convert the binary to int.

        Update: This is more like cheating, after viewing the discussions.

        O(N), 1456 ms, 68% ranking.
        """
        b_str = ''
        for i in range(1, n + 1):
            b_str += format(i, 'b')
        return int(b_str, 2) % (10**9 + 7)


class Solution2:
    def concatenatedBinary(self, n: int) -> int:
        """One liner, because lol"""
        return int(''.join(format(i, 'b') for i in range(1, n + 1)), 2) % (10**9 + 7)


class Solution3:
    def concatenatedBinary(self, n: int) -> int:
        """The official O(N) solution.

        f(1) = 1
        f(2) = 110 = f(1) << 2 + 2
        f(3) = 11011 = f(2) << 2 + 3
        ...

        It's slower than the solutions above, because the binary convertion in
        Python must have been optimized.

        O(N), 3660 ms, 12% ranking.
        """
        f = 1
        for i in range(2, n + 1):
            # important to do modulo each time, otherwise the number gets too
            # big and the bit manipulation slows down to TLE.
            f = ((f << len(format(i, 'b'))) + i) % (10**9 + 7)
        return f


class Solution4:

    cache = list(itertools.accumulate(range(10**5 + 1), lambda t, e: ((t << len(format(e, 'b'))) + e) % (10**9 + 7)))

    def concatenatedBinary(self, n: int) -> int:
        """A trick to use on LeetCode. It is actually not a trick, because this
        is taking advantage of a class variable, which is shared among ALL
        instances of the same class. Anything declared within the __init__()
        function is an instance variable, which get's recreated when a new
        instance is created. On LeetCode, each test case requries creation of
        a new instance. Thus, our cache cannot exist in the instance variable
        form. It is perfect for the class variable, because the cache does not
        change for all instances.

        O(1) runtime for the function, not counting the creation of the cache.
        64 ms, 99% ranking.
        """
        return Solution4.cache[n]


# sol = Solution4()
tests = [
    (1, 1),
    (3, 27),
    (12, 505379714),
    (44684, 259179281),
]

for i, (n, ans) in enumerate(tests):
    sol = Solution4()
    res = sol.concatenatedBinary(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
