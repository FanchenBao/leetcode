# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def smallestRepunitDivByK(self, k: int) -> int:
        """LeetCode 1015

        Notice that if the current value V = qk + r, then the next value
        V * 10 + 1 = 10qk + (10r + 1). Thus, whether 10V + 1 is divisible by
        k is determined by 10r + 1. Therefore, we keep checking (10r + 1) % k.
        Once it turns to 0, we return the number of iterations. If the
        remainder has occurred before, then we are inside a loop and should
        return -1.

        91 ms, 26% ranking.
        """
        setr = set([0])
        count, r = 0, 0
        while True:
            r = (r * 10 + 1) % k
            count += 1
            if r == 0:
                return count
            if r in setr:
                return -1
            setr.add(r)


class Solution2:
    def smallestRepunitDivByK(self, k: int) -> int:
        """This is the solution I learned a year ago. The idea is the same, but
        we don't have to keep a set to check whether the remainder has repeated.
        We can use pigeon hold theory, which states that given k there must be
        k possible remainders. Thus, if within k iterations, we haven't found a
        zero remainder, then it is impossible to encounter a zero at all.

        Time complexity is O(K)
        """
        r = 0
        for i in range(k):
            r = (r * 10 + 1) % k
            if r == 0:
                return i + 1
        return -1


sol = Solution2()
tests = [
    (1, 1),
    (2, -1),
    (3, 3),
    (23, 22),
]

for i, (k, ans) in enumerate(tests):
    res = sol.smallestRepunitDivByK(k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
