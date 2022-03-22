# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        """LeetCode 1663

        This problem can be solved mathematically. The best way to set up the
        string is to get as many 'a' as possible. Then, when no more 'a' can
        be added, we find one more smallest letter that can make the string
        work, which results in the remaining letters all being 'z'.

        We can check the intermediate letter from 'a' to 'z' and report the
        first letter that can make the string possible. Note that during the
        check, we have to also make sure the number of 'a' remains non-negative

        O(1), 32 ms, 98% ranking.
        """
        for i in range(1, 27):
            y, r = divmod(k + 1 - n - i, 25)
            if r == 0 and n - 1 - y >= 0:
                break
        return 'a' * (n - 1 - y) + chr(i - 1 + 97) + 'z' * y


sol = Solution()
tests = [
    (3, 27, 'aay'),
    (5, 73, 'aaszz'),
    (5, 130, 'zzzzz'),
]

for i, (n, k, ans) in enumerate(tests):
    res = sol.getSmallestString(n, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
