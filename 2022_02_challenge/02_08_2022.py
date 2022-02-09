# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def addDigits(self, num: int) -> int:
        """LeetCode 258

        This solution uses loop. Thus, it does not satisfy the requirement of
        O(1) time without loop.

        O(log(num)), 40 ms, 51% ranking.
        """
        numstr = str(num)
        while len(numstr) > 1:
            numstr = str(sum(int(d) for d in numstr))
        return int(numstr)


class Solution2:
    def addDigits(self, num: int) -> int:
        """O(1) no loop solution

        0 => 0
        1 - 9 => 1 - 9
        10 - 18 => 1 - 9
        19 - 27 => 1 - 9
        28 - 36 => 1 - 9
        .
        .
        .
        55 - 63 => 1 - 9
        .
        .
        .
        91 - 99 => 1 - 9
        100 - 108 => 1 - 9
        .
        .
        .
        Thus all we need to do is num % 9, and analyze the remainder afterwards.
        """
        r = num % 9
        return r if r else 9 if num else 0


sol = Solution2()
tests = [
    (38, 2),
    (0, 0),
    (108, 9),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.addDigits(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
