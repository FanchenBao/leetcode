# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """LeetCode 402

        I accidentally saw the shape of my previous solution, which provided
        sufficient hint to allow me to hit the right direction: monotonic stack

        O(N), 65 ms, 42% ranking.
        """
        stack = []
        for d in num + '0':
            while stack and k and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        stack.pop()
        return str(int(''.join(stack))) if stack else '0'


sol = Solution()
tests = [
    ("1432219", 3, '1219'),
    ("10200", 1, '200'),
    ("10", 2, '0'),
    ('1', 1, '0'),
]

for i, (num, k, ans) in enumerate(tests):
    res = sol.removeKdigits(num, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
