# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minimumTime(self, s: str) -> int:
        res = 0
        N = len(s)
        i, j = 0, N - 1
        while i < N and s[i] == '1':
            i += 1
        while j > i and s[j] == '1':
            j -= 1
        res += i + (N - 1 - j)
        mid = (i + j) // 2
        one_indices = []
        for k in range(i, mid + 1):
            if s[k] == '1':
                one_indices.append(k)
        left_min = 2 * len(one_indices)
        for cnt, idx in enumerate(one_indices):
            left_min = min(left_min, 2 * len(one_indices) - (cnt + 1) * 2 + idx + 1)
        one_indices = []
        for k in range(j, mid, -1):
            if s[k] == '1':
                one_indices.append(k)
        right_min = 2 * len(one_indices)
        for cnt, idx in enumerate(one_indices):
            right_min = min(right_min, 2 * len(one_indices) - (cnt + 1) * 2 + N - idx)
        return res + left_min + right_min


sol = Solution()
tests = [
    ('1100101', 5),
    ('0010', 2),
    ('010001000', 4),
    ('011100001000000', 6)
]

for i, (s, ans) in enumerate(tests):
    res = sol.minimumTime(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
