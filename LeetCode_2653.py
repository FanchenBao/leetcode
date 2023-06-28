# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in range(x):
            heapq.heappush(heap, (-nums[i], i))
        for i in range(x, k):
            if nums[i] < -heap[0][0]:
                heapq.heappushpop(heap, (-nums[i], i))
        res = [-heap[0][0]] if -heap[0][0] < 0 else [0]
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            # print(heap, i)
            while heap and heap[0][1] < i - k:
                heapq.heappop(heap)
            heapq.heappop(heap)
            res.append(-heap[0][0] if -heap[0][0] < 0 else 0)
        return res
        

sol = Solution()
tests = [
    # ([1,-1,-3,-2,3], 3, 2, [-1,-2,-2]),
    # ([-1,-2,-3,-4,-5], 2, 2, [-1,-2,-3,-4]),
    # ([-3,1,2,-3,0,-3], 2, 1, [-3,0,-3,-3,-3]),
    ([-38,-37,44], 2, 2, [-37, 0]),
]

for i, (nums, k, x, ans) in enumerate(tests):
    res = sol.getSubarrayBeauty(nums, k, x)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
