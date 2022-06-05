# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def removeDigit(self, number: str, digit: str) -> str:
        return str(max(int(number[:i] + number[i + 1:]) for i in range(len(number)) if number[i] == digit))


class Solution2:
    def removeDigit(self, number: str, digit: str) -> str:
        cands = [i for i, n in enumerate(number) if n == digit]
        if len(cands) == 1:
            return number[:cands[0]] + number[cands[0] + 1:]
        for j, idx in enumerate(cands):
            if j == len(cands) - 1 or number[idx + 1] > digit:
                return number[:idx] + number[idx + 1:]


sol = Solution2()
tests = [
    ('123', '3', '12'),
    ('1231', '1', '231'),
    ('551', '5', '51'),
]

for i, (number, digit, ans) in enumerate(tests):
    res = sol.removeDigit(number, digit)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
