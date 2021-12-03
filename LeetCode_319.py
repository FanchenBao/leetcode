# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution1:
    def bulbSwitch(self, n: int) -> int:
        """This is pretty hard for me. But I am pretty sure the actual solution
        will be five lines using some math.

        My idea starts from realizing that for the ith bulb to be on, i must
        have odd number of unique factors (including 1 and itself). Given an
        integer N = p^a * q^b * ... * r^c, where p, q, ..., r are prime numbers,
        the total number of unique factors are (a + 1)(b + 1)...(c + 1). To make
        this value odd, we require that a, b, ..., c must all be even. This
        means the only value that can keep the bulb on is N = (p^2)^α * (q^2)^β
        * ... * (r^2)^γ, where α, β, ..., γ are non-negative integers. Thus, we
        need to find all prime numbers whose square is smaller or equal to the
        given n. Then, we need to find all combinations of these prime numbers
        as factors to generate a value smaller or equal to n.

        I use the sieve to first obtain all the prime numbers. Then I use
        priority queue to obtain a sequence of sorted numbers that all have the
        given prime factors. The final result is the length of this sorted list.

        O(M^2), where M = sqrt(N), 548 ms, 5% ranking.
        """
        if n == 0:
            return 0
        if n <= 3:
            return 1
        lim = int(math.sqrt(n))
        sieve = [1 if i % 2 else 0 for i in range(lim + 1)]
        sieve[2] = 1
        sieve[1] = 0
        i = 3
        while i * i < lim:
            for j in range(i * i, lim + 1, i * i):
                sieve[j] = 0
            i += 2
        prime_sq = [i * i for i, s in enumerate(sieve) if s]
        heap = [1]
        while prime_sq:
            temp = []
            cur = prime_sq.pop()
            while True:
                temp.append(heapq.heappop(heap))
                if cur * temp[-1] <= n:
                    heapq.heappush(heap, cur * temp[-1])
                else:
                    break
            heap.extend(temp)
            heapq.heapify(heap)
        return len(set(heap))


class Solution2:
    def bulbSwitch(self, n: int) -> int:
        """I am so close, but at the same time also so far away from the smart
        solution.

        I will link Mr. Pochmann: https://leetcode.com/problems/bulb-switcher/discuss/77104/Math-solution..

        I am close, because I also realized that to make bulb stay on, the
        number must have odd number of factors. Then I proceeded to list all the
        valid factors and try to compute the total number of values that can be
        produced by these factors. However, the smart intuition is that any non
        square numbers has even number of factors. The only value that has odd
        number of factors is square number. This is because factors always come
        in pairs, except when the number is a square, then the last pair has
        identical values. Thus, the problem is finding the number of square
        numbers smaller or equal to n.
        """
        return int(math.sqrt(n))



sol = Solution2()
tests = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 2),
    (6, 2),
    (7, 2),
    (8, 2),
    (9, 3),
    (10, 3),
    (11, 3),
    (100, 10),
    (1000, 31),
]

for i, (n, ans) in enumerate(tests):
    res = sol.bulbSwitch(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
