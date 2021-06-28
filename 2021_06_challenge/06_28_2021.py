# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def removeDuplicates(self, s: str) -> str:
        """LeetCode 1047

        A simple stack solution suffices.

        O(N), 56 ms, 96% ranking.
        """
        stack = []
        for le in s:
            if not stack or stack[-1] != le:
                stack.append(le)
            else:
                stack.pop()
        return ''.join(stack)


sol = Solution()
tests = [
    ('abbaca', 'ca'),
    ('azxxzy', 'ay'),
]

for i, (s, ans) in enumerate(tests):
    res = sol.removeDuplicates(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
