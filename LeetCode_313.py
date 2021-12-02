# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution1:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """TLE"""
        if n == 1:
            return 1
        viables = set([1])
        i = 2
        primes.sort()
        while len(viables) < n:
            for p in primes:  # check whether i is viable
                q, r = divmod(i, p)
                if r == 0 and q in viables:
                    viables.add(i)
                    break
            i += 1
        return i - 1


class Solution2:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """The heap solution from the discussion. But I have not read the code.

        The idea is that each new ugly number must be produced by multiplying
        one of the ugly numbers already found with one of the primes. Thus, we
        can create a heap for all the ugly numbers already found. We then pop
        the smallest of these ugly numbers and keep the count. The smallest ugly
        number is the count-th ugly number. And for each popped ugly number, we
        put in another round of ugly numbers by multiplying it with each primes.

        TLE. Apparently, I didn't fully comprehend the idea behind priority
        queue.
        """
        ugly = []
        count, cur = 0, 1
        while count < n:
            while ugly:
                new_cur = heapq.heappop(ugly)
                if new_cur != cur:
                    cur = new_cur
                    break
            count += 1
            for p in primes:
                heapq.heappush(ugly, cur * p)
        return cur


class Solution3:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """This time, I read the discussion post.

        https://leetcode.com/problems/super-ugly-number/discuss/277313/My-view-of-this-question-hope-it-can-help-you-understand!!!

        And now I finally understand. This problem is similar to merging sorted
        list. For detailed explanation, refer to the discussion post.

        The heap is used to find the smallest value among the max of the sorted
        lists under each prime numbers.

        O(Nlog(K)), where K = len(primes). 3112 ms, 54% ranking.
        """
        heap = []
        for p in primes:  # each element is (max_of_list, the_prime_of_the_list, index_on_the_list)
            heapq.heappush(heap, (p, p, 0))
        ugly = [1]
        while len(ugly) < n:
            min_ugly, p, idx = heapq.heappop(heap)
            if min_ugly != ugly[-1]:  # handle duplicates
                ugly.append(min_ugly)
            heapq.heappush(heap, (p * ugly[idx + 1], p, idx + 1))
        return ugly[-1]


sol = Solution3()
tests = [
    (12, [2,7,13,19], 32),
    (1, [2,3,5], 1),
    (15, [3,5,7,11,19,23,29,41,43,47], 35),
]

for i, (n, primes, ans) in enumerate(tests):
    res = sol.nthSuperUglyNumber(n, primes)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
