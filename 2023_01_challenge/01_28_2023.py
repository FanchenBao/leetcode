# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class SummaryRanges:

    def __init__(self):
        """LeetCode 352

        Just analyze the hell out of merging conditions.

        O(1) for getIntervals
        O(N) for addNum
        491 ms, faster than 26.09%
        """
        self.range = []

    def addNum(self, value: int) -> None:
        idx = bisect_right(self.range, value, key=lambda tup: tup[0])
        if idx == 0:
            if not self.range or self.range[0][0] > value + 1:
                self.range.insert(0, [value, value])
            else:
                self.range[0][0] = value
        elif idx == len(self.range):
            if value == self.range[idx - 1][1] + 1:
                self.range[idx - 1][1] = value
            elif value > self.range[idx - 1][1] + 1:
                self.range.append([value, value])
        else:
            if self.range[idx - 1][1] + 1 == value and value < self.range[idx][0] - 1:
                self.range[idx - 1][1] = value
            elif self.range[idx - 1][1] + 1 == value and value == self.range[idx][0] - 1:
                lo, hi = self.range.pop(idx)
                self.range[idx - 1][1] = hi
            elif self.range[idx - 1][1] + 1 < value and value == self.range[idx][0] - 1:
                self.range[idx][0] = value
            elif self.range[idx - 1][1] + 1 < value and value < self.range[idx][0] - 1:
                self.range.insert(idx, [value, value])

    def getIntervals(self) -> List[List[int]]:
        return self.range


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
