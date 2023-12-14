# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # minHeap = []
        # maxHeap = []
        lo = 0
        res = 0
        minV = maxV = nums[0]
        for i in range(1, len(nums)):
            if abs(nums[i] - minV) <= 2 and abs(nums[i] - maxV) <= 2:
                minV = min(minV, nums[i])
                maxV = max(maxV, nums[i])
                continue
            j = i - 1
            minV, maxV = nums[i], nums[i]
            while j >= 0:
                if abs(nums[i] - nums[j]) > 2:
                    break
                minV = min(minV, nums[j])
                maxV = max(maxV, nums[j])
                j -= 1
            count = j - lo + 1
            res += (count + 1) * count // 2
            lo = j + 1
        return res


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
