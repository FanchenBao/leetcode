# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict
from bisect import bisect_right, insort


class Allocator:

    def __init__(self, n: int):
        """Use self.empties to record all ranges of empty blocks. Use self.mids
        to record the occupied blocks for each memory ID.

        The complex part is the handling of block merges when allocate and free
        are called. When allocate is called, block merge happens in self.mids.
        When free is called, block merge happens in self.empties. The mechanism
        of these merges is the same. We use self._insert to handle this logic.

        372 ms, faster than 87.92%
        """
        self.empties = [[0, n - 1]]
        self.mids = defaultdict(list)

    def _insert(self, ranges: List[List[int]], ran: List[int]) -> None:
        if not ranges:
            ranges.append(ran)
            return
        idx = bisect_right(ranges, ran)
        if idx == 0:
            if ran[1] < ranges[0][0] - 1:
                ranges.insert(0, ran)
            else:
                ranges[0][0] = ran[0]
        elif idx == len(ranges):
            if ran[0] > ranges[-1][1] + 1:
                ranges.append(ran)
            else:
                ranges[-1][1] = ran[1]
        else:
            if ranges[idx - 1][1] + 1 < ran[0] and ran[1] < ranges[idx][0] - 1:
                ranges.insert(idx, ran)
            elif ranges[idx - 1][1] + 1 == ran[0] and ran[1] < ranges[idx][0] - 1:
                ranges[idx - 1][1] = ran[1]
            elif ranges[idx - 1][1] + 1 < ran[0] and ran[1] == ranges[idx][0] - 1:
                ranges[idx][0] = ran[0]
            else:
                ranges[idx - 1][1] = ranges[idx][1]
                ranges.pop(idx)

    def allocate(self, size: int, mID: int) -> int:
        for i, (a, b) in enumerate(self.empties):
            if b - a + 1 >= size:
                self.empties[i][0] = a + size
                self._insert(self.mids[mID], [a, a + size - 1])
                return a
        return -1

    def free(self, mID: int) -> int:
        res = 0
        for ran in self.mids.pop(mID, []):
            self._insert(self.empties, ran)
            res += ran[1] - ran[0] + 1
        return res



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
