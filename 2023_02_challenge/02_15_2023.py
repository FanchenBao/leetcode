# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        """LeetCode 989

        288 ms, faster than 88.34% 

        UPDATE: this is not the most efficient solution, because if num is huge
        but k is small, we will have to iterate through the remainder of num
        which is unnecessary.
        """
        res = []
        i = len(num) - 1
        c = 0
        while i >= 0 and k:
            s = num[i] + k % 10 + c
            c, r = divmod(s, 10)
            res.append(r)
            k //= 10
            i -= 1
        while i >= 0:
            s = num[i] + c
            c, r = divmod(s, 10)
            res.append(r)
            i -= 1
        while k:
            s = k % 10 + c
            c, r = divmod(s, 10)
            res.append(r)
            k //= 10
        if c:
            res.append(c)
        return res[::-1]


class Solution2:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        """More efficient solution from https://leetcode.com/problems/add-to-array-form-of-integer/solution/393863

        The trick is to add k to each element of num and change num in-place.

        271 ms, faster than 95.33%
        """
        num[-1] += k
        for i in range(len(num) - 1, -1, -1):
            k, r = divmod(num[i], 10)
            if not k:
                break
            num[i] = r
            if i:
                num[i - 1] += k  # k is essentially carry
        while k:
            k, r = divmod(k, 10)
            num = [r] + num
        return num


sol = Solution2()
tests = [
    ([0], 23, [2,3]),
]

for i, (num, k, ans) in enumerate(tests):
    res = sol.addToArrayForm(num, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
