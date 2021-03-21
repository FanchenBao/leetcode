# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict, Counter


class Solution1:
    def reorderedPowerOf2(self, N: int) -> bool:
        """LeetCode 869
        This problem looks daunting at first, but once we realize that the
        total number of power of twos is quite limited. There are only 30 of
        them from 2^0 to 2^29. So we can write them out. My strategy is to use
        the length of the number as the key, and then group all the power of two
        of the same digit length together. And we also do a sort for all the
        power of twos, such that we can make a simple comparison between the
        given N to one of the power of twos. This is possible also because the
        question stipulates that we cannot reduce the length of N when
        reordering the digits.

        Since all the variables are bounded. This can be considered O(1).
        36 ms, 54% ranking.
        """
        all_powers = defaultdict(list)
        for i in range(30):
            power = str(2**i)
            all_powers[len(power)].append(sorted(power))
        str_n = str(N)
        sorted_n = sorted(str_n)
        return any(p == sorted_n for p in all_powers[len(str_n)])


class Solution2:
    def reorderedPowerOf2(self, N: int) -> bool:
        """This is the official solution using counter.
        """
        counter_n = Counter(str(N))
        return any(counter_n == Counter(str(1 << i)) for i in range(30))


class Solution3:
    def reorderedPowerOf2(self, N: int) -> bool:
        """This is applying the style of the official solution to our original
        sorting solution. But sorting is slightly slower than using a counter.
        """
        sorted_n = sorted(str(N))
        return any(sorted_n == sorted(str(1 << i)) for i in range(30))


sol = Solution3()
tests = [
    (1, True),
    (2, True),
    (3, False),
    (4, True),
    (10, False),
    (16, True),
    (61, True),
    (24, False),
    (46, True),
]

for i, (N, ans) in enumerate(tests):
    res = sol.reorderedPowerOf2(N)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
