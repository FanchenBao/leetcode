# from pudb import set_trace; set_trace()
from typing import List
from random import randint


class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """LeetCode 215

        O(NlogN), 118 ms, faster than 36.36%
        """
        return sorted(nums)[-k]


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Quick select with random pivot

        O(N), 74 ms, faster than 83.44% 
        """

        def pick_pivot(l: int, r: int) -> int:
            piv = randint(l, r)
            nums[l], nums[piv] = nums[piv], nums[l]
            i, j = l + 1, r
            while i < j:
                if nums[i] > nums[l]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                else:
                    i += 1
            if i <= r and nums[i] < nums[l]:
                nums[i], nums[l] = nums[l], nums[i]
                return i
            nums[i - 1], nums[l] = nums[l], nums[i - 1]
            return i - 1

        l, r = 0, len(nums) - 1
        N = len(nums)
        while l <= r:
            piv = pick_pivot(l, r)
            if N - piv == k:
                return nums[piv]
            if N - piv > k:
                l = piv + 1
            else:
                r = piv - 1


sol = Solution2()
tests = [
    ([3,2,1,5,6,4], 2, 5),
    ([3,2,3,1,2,4,5,5,6], 4, 4),
    ([1], 1, 1),
    ([1, 1, 1, 1], 3, 1),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.findKthLargest(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
