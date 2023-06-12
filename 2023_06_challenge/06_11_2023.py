# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class SnapshotArray:
    """LeetCode 1146

    For each index, we keep an array of [snap_id, val] pairs. Then when querying
    an index and a snap_id, we use binary search for the snap_id to find the val
    that lies between the previous snap_id and the current snap_id.

    O(logN) for get().  692 ms, faster than 53.27%
    """

    def __init__(self, length: int):
        self.arr = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.snap_id == self.arr[index][-1][0]:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect_right(self.arr[index], snap_id, key=lambda tup: tup[0])
        return self.arr[index][idx - 1][1]


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
