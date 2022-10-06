# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict
from bisect import bisect_right


class TimeMap:
    """LeetCode 981

    Binary search.

    O(1) for set
    O(logN) for get
    903 ms, faster than 79.84%
    """
    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_right(self.m[key], timestamp, key=lambda tup: tup[0])
        if idx == 0:
            return ''
        return self.m[key][idx - 1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
