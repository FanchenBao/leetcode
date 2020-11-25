# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def smallestRepunitDivByK(self, K: int) -> int:
        """94% ranking

        The observation is that the remainder of 111...1 divided by K is the
        sum of the remainders of 100..0, 10..0, ..., 100, 10, 1 divided by K.
        If the sum of these remainders first becoems  a multiple of K, we have
        found the target 111...1

        The trick is finding 10^N mod K. What I did was to record r = 10^(N - 1)
        mod K, then 10^N mod K = (10 * r) mod K, which speeds up computation
        tremendously.
        """
        ld = int(str(K)[-1])
        if ld == 5 or ld % 2 == 0:  # impossible case
            return -1
        if K == 1:  # special case
            return 1
        N, cum_r, prev_r = 1, 1, 1
        while cum_r % K:
            cur_r = (10 * prev_r) % K  # compute remainder of 10**N % K
            cum_r += cur_r
            prev_r = cur_r
            N += 1
        return N


class Solution2:
    def smallestRepunitDivByK(self, K: int) -> int:
        """Standard solution.

        Two intuition: 1. we directly compute the remainder of 11...1 % K, but
        using the trick of next_rem = (prev_rem * 10 + 1) % K.
        2. The goal is to test all possible 11...1 and see if one of them
        results in remainder 0. Impossible case happens when after a bunch of
        search, the remainder starts to loop. That means we will never reach
        a remainder of 0. To check the loop, we use Pigeonhole theory, i.e.
        given that K only has K remainders, if we still haven't found 0
        remainder in these K tries, then the next try will definitely be a
        loop.
        """
        if not K % 2 or not K % 5:
            return -1
        rem = 1
        for N in range(K):
            if rem % K == 0:
                break
            rem = (rem * 10 + 1) % K
        return N + 1




sol = Solution2()
tests = [
   (1, 1),
   (11, 2),
   (111, 3),
   (2, -1),
   (3, 3),
   (7, 6),
   (9, 9),
   (19, 18),
   (13, 6),
   (407, 6),
   (49993, 49992),
]

for i, (K, ans) in enumerate(tests):
    res = sol.smallestRepunitDivByK(K)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
