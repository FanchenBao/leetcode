# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def removeDuplicates(self, s: str, k: int) -> str:
        """LeetCode 1209

        Use stack. Surprisingly, this is the same solution that I learned from
        lee215 the last time it was attempted.

        O(N), 201 ms, faster than 31.07%
        """
        stack = []
        for le in s:
            if not stack or stack[-1][1] != le:
                stack.append([1, le])
            else:
                stack[-1][0] += 1
            if stack[-1][0] == k:
                stack.pop()
        return ''.join(le * c for le, c in stack)


class Solution2:
    def removeDuplicates(self, s: str, k: int) -> str:
        """This is the other solution that I learned from lee215 last time. It
        uses two pointers, where one keeps moving forward along s, whereas the
        other records the letters to be included in the result.

        O(N), 154 ms, faster than 57.93%
        """
        N = len(s)
        res_lst = [''] * N
        count = [0] * N
        i = 0
        for j in range(N):
            res_lst[i] = s[j]
            count[i] = 1 + count[i - 1] * (j > 0 and s[j] == res_lst[i - 1])
            if count[i] == k:
                i -= k
            i += 1
        return ''.join(res_lst[:i])
            

sol = Solution2()
tests = [
    ('abcd', 2, 'abcd'),
    ('deeedbbcccbdaa', 3, 'aa'),
    ('pbbcggttciiippooaais', 2, 'ps'),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.removeDuplicates(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
