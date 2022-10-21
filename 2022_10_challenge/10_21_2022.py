# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """LeetCode 219

        1576 ms, faster than 26.33%
        """
        hashmap = {}
        for i, n in enumerate(nums):
            if n in hashmap:
                if i - hashmap[n] <= k:
                    return True
            hashmap[n] = i
        return False


class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """Sliding window, from previous submission.

        We first check the first k + 1 values in nums. If there are repeats,
        we can return True immediately.

        If all of them are unique, we create a window of unique values. Then
        we move forward. For each new number, we remove a number from the left.
        If the new number is in the window, we reutrn True. Otherwise, we
        maintain that the window has all unique values.
        """
        w = set()
        for i, n in enumerate(nums):
            if i > k:
                w.remove(nums[i - k - 1])
            if n in w:
                return True
            w.add(n)
        return False


sol = Solution2()
tests = [
    ([1,2,3,1], 3, True),
    ([1,0,1,1], 1, True),
    ([1,2,3,1,2,3], 2, False),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.containsNearbyDuplicate(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
