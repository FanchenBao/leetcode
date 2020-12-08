# from pudb import set_trace; set_trace()
from typing import List
from random import randint
from collections import Counter


class Solution1:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """This is the most naive brute force approach. I don't even bother
        submitting it as I know it is going to TLE. But it serves as the ground
        truth to debug other better solutions.
        """
        res = 0
        for i in range(len(time)):
            for j in range(i + 1, len(time)):
                if not (time[i] + time[j]) % 60:
                    res += 1
        return res


class Solution2:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """Using a bucket to mark what numbers are available. Use a finite list
        of multiplies of 60 to check on each number.

        O(17N) = O(N), 512 ms, ranking too low to show.
        """
        buckets = [0] * 501
        for t in time:
            buckets[t] += 1
        mult_60 = [60 * i for i in range(1, 17)]
        res = 0
        for t in time:
            buckets[t] -= 1
            for ms in mult_60:
                if 0 < ms - t <= 500 and buckets[ms - t] > 0:
                    res += buckets[ms - t]
        return res


class Solution3:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """After reading the hint, the solution becomes more math based, and
        thus much faster. We create a counter of all the remainders appearing
        in the time list after divided by 60. We know that any two numbers' sum
        can be divided by 60 if the sum of their remaniders is 60. Thus, we can
        find the number of numbers whose remainders are one, and the number of
        numbers whose remainders are 59. Their sum are divisible by 60. And the
        total number of pairs between these two types of numbers is the product
        of their counts.

        Special cases are given to remainders of 0 and 30. They can only be
        paired with themselves, thus the formula to compute total number of
        pairs is slightly different.

        O(N), 200 ms, 98% ranking.
        """
        c = Counter(t % 60 for t in time)
        return sum(c[j] * (c[j] - 1) // 2 for j in [0, 30]) + sum(c[i] * c[60 - i] for i in range(1, 30))


sol_correct = Solution2()
sol = Solution3()
times = [[randint(1, 500) for _ in range(randint(1, 5000))] for _ in range(10)]
tests = [(t, sol_correct.numPairsDivisibleBy60(t)) for t in times]

# tests = [([337, 483, 181, 477, 33], 1)]

for i, (time, ans) in enumerate(tests):
    res = sol.numPairsDivisibleBy60(time)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}, Time: {time}')
        # print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
