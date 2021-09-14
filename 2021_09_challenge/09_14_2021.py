# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def reverseOnlyLetters(self, s: str) -> str:
        """LeetCode 917

        Use two pointers, one at the front and one at the end. If both point
        to an English letter, we swap them. Otherwise, we move the pointer
        towards the center if it does not point to an English letter.

        O(N) time complexity. O(N) space. 52 ms, 5% ranking

        UPDATE: make sure that isalpha() runs only once for each letter. 45 ms,
        11% ranking.
        """
        lst = list(s)
        lo, hi = 0, len(s) - 1
        while lo < hi:
            if not lst[lo].isalpha():
                lo += 1
                continue
            if not lst[hi].isalpha():
                hi -= 1
                continue
            lst[lo], lst[hi] = lst[hi], lst[lo]
            lo += 1
            hi -= 1
        return ''.join(lst)


class Solution2:
    def reverseOnlyLetters(self, s: str) -> str:
        """Stack solution from the official solution.

        https://leetcode.com/problems/reverse-only-letters/solution/

        Faster than solution1, 32 ms.
        """
        stack = [c for c in s if c.isalpha()]
        lst = []
        for c in s:
            if c.isalpha():
                lst.append(stack.pop())
            else:
                lst.append(c)
        return ''.join(lst)


sol = Solution2()
tests = [
    ('ab-cd', 'dc-ba'),
    ('a-bC-dEf-ghIj', 'j-Ih-gfE-dCba'),
    ('Test1ng-Leet=code-Q!', 'Qedo1ct-eeLg=ntse-T!'),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseOnlyLetters(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
