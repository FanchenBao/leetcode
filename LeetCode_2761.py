# from pudb import set_trace; set_trace()
from typing import List
import math
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        """
        The sieve takes a long time to run.

        O(N^2), 6273 ms, faster than 14.84% 
        """
        # Use eratosthenes' sieve to find all the prime numbers from
        # 2 to n
        sieve = [1] * (n + 1)
        sieve[0] = sieve[1] = 0
        for i in range(4, n + 1, 2):
            sieve[i] = 0
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            j = i
            while j * i <= n:
                sieve[j * i] = 0
                j += 2
        primes = set()
        for i in range(2, n + 1):
            if sieve[i]:
                primes.add(i)
        # print(primes, len(primes))
        res = []
        for p in sorted(primes):
            if p > n // 2:
                break
            if n - p in primes:
                res.append([p, n - p])
        return res


class Solution2:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        """
        The sieve takes a long time to run.

        No need to create a set. We can use the sieve directly when
        finding the prime pairs.

        O(N^2), 5433 ms, faster than 21.19%
        """
        # Use eratosthenes' sieve to find all the prime numbers from
        # 2 to n
        sieve = [1] * (n + 1)
        sieve[0] = sieve[1] = 0
        for i in range(4, n + 1, 2):
            sieve[i] = 0
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            j = i
            while j * i <= n:
                sieve[j * i] = 0
                j += 2
        
        res = []
        for p in range(2, n // 2 + 1):
            if sieve[p] and sieve[n - p]:
                res.append([p, n - p])
        return res



sol = Solution2()
tests = [
    (10, [[3,7],[5,5]]),
    (2, []),
]

for i, (n, ans) in enumerate(tests):
    res = sol.findPrimePairs(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
