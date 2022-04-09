# from pudb import set_trace; set_trace()
from typing import List
import heapq
import math


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """LeetCode 703

        Although it is labeled as easy, it is quite challenging. I know it is
        a heap problem, but I got a few errors because I didn't fully realize
        the edge cases where k > len(self.minh). When that happens, which means
        there are not enough values in minh to generate the kth largest value,
        we simply push new numbers into minh.

        O(NlogN) for initialization. O(logN) per operation. 112 ms, 75% ranking.
        """
        nums.sort()
        self.k = k
        self.minh = nums[-k:]
        self.maxh = [-n for n in nums[:-k]]

    def add(self, val: int) -> int:
        if len(self.minh) < self.k:
            heapq.heappush(self.minh, val)
        else:
            if val <= self.minh[0]:
                heapq.heappush(self.maxh, -val)
            else:
                heapq.heappush(self.maxh, -heapq.heappop(self.minh))
                heapq.heappush(self.minh, val)
        return self.minh[0]


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """This is the official solution. It does not keep all the values, but
        only the top k numbers.
        """
        nums.sort()
        self.heap = nums[-k:]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]


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
