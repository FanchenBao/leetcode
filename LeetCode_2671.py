# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class FrequencyTracker:
    """Two counters. One for frequency of values. The other for frequency of
    frequencies.

    686 ms, faster than 16.22%
    """

    def __init__(self):
        self.vc = Counter()
        self.fc = Counter()

    def add(self, number: int) -> None:
        pre_c = self.vc[number]
        self.vc[number] += 1
        self.fc[self.vc[number]] += 1
        if self.fc[pre_c]:
            self.fc[pre_c] -= 1

    def deleteOne(self, number: int) -> None:
        pre_c = self.vc[number]
        if pre_c:
            self.vc[number] -= 1
            self.fc[self.vc[number]] += 1
            if self.fc[pre_c]:
                self.fc[pre_c] -= 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.fc[frequency] > 0


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
