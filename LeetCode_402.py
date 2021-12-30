# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """Produce a monotonic increasing stack based on num. Each value that
        is popped from the stack is the digit that needs to be removed from
        num. Keep counting the number of values popped. If we have enough
        digits popped, the stack and the remaining value in num combined is the
        solution. Otherwise, we must have exhausted all digits in num. Thus we
        need to pop more from the stack from back to front until we hit k pops.

        When returning the value, we must strip the zeros on the left.

        O(N), where N = len(num), 36 ms, 82% ranking.
        """
        stack = []
        count, i = 0, 0
        for n in num:
            while stack and stack[-1] > n and count < k:
                stack.pop()
                count += 1
            stack.append(n)
        return ''.join(stack[:len(num) - k]).lstrip('0') or '0'


sol = Solution()
tests = [
    ('1432219', 3, '1219'),
    ('10200', 1, '200'),
    ('10', 2, '0'),
    ("10001", 1, '1'),
]

for i, (num, k, ans) in enumerate(tests):
    res = sol.removeKdigits(num, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
