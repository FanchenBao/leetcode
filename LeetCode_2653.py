# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq
from sortedcontainers import SortedList


class Solution1:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        """This is cheating, but I am okay with it now since I have been stuck
        on it for a very long time.

        O(NlogN), 6513 ms, faster than 18.97%
        """
        window = SortedList()
        res = []
        for i, n in enumerate(nums):
            window.add(n)
            if len(window) > k:
                window.remove(nums[i - k])
            if len(window) == k:
                res.append(window[x - 1] if window[x - 1] < 0 else 0)
        return res


class Solution2:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        """The hint says iterate through all the negative integers. I was like
        what?? Then I saw the range for numbers in nums is -50 to 50. So yes,
        we shall iterate through all the negative values.

        I feel punked.

        4432 ms, faster than 85.99%
        """
        counter = [0] * 51
        res = []
        win_size = 0
        for i, n in enumerate(nums):
            win_size += 1
            if n < 0:
                counter[-n] += 1
            if win_size > k:
                if nums[i - k] < 0:
                    counter[-nums[i - k]] -= 1
                win_size -= 1
            if win_size == k:
                c = 0
                for j in range(50, 0, -1):
                    c += counter[j]
                    if c >= x:
                        res.append(-j)
                        break
                else:
                    res.append(0)
        return res
        

sol = Solution2()
tests = [
    ([1,-1,-3,-2,3], 3, 2, [-1,-2,-2]),
    ([-1,-2,-3,-4,-5], 2, 2, [-1,-2,-3,-4]),
    ([-3,1,2,-3,0,-3], 2, 1, [-3,0,-3,-3,-3]),
    ([-38,-37,44], 2, 2, [-37, 0]),
]

for i, (nums, k, x, ans) in enumerate(tests):
    res = sol.getSubarrayBeauty(nums, k, x)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
