# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        """LeetCode

        The only surprise is that negative numbers are not considered numeric
        directly by .isnumeric() function call.

        O(N), 65 ms, 37% ranking.

        UPDATE: we can check for numeric at the end, thus avoiding the direct
        check for negative values
        """
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)


sol = Solution()
tests = [
    (["5","-2","4","C","D","9","+","+"], 27),
]

for i, (ops, ans) in enumerate(tests):
    res = sol.calPoints(ops)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
