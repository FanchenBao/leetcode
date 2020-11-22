# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def search(self, nums: List[int], target: int) -> bool:
        """62% ranking.

        The trick is to remove the values at the end of nums that is identical
        to that at the start of nums. The rest is just a more complicated
        version of binary search,
        """
        # remove confusing items in nums, i.e. the same number that ends and
        # starts the nums list. The presence of this type of number would cause
        # trouble identifying which rising portion the mid is on
        while len(nums) > 1 and nums[-1] == nums[0]:
            nums.pop()
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                if nums[mid] <= nums[-1]:  # mid is on the right rising portion
                    if target <= nums[-1]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:  # mid is on the left rising portion
                    left = mid + 1
            elif nums[mid] > target:
                if nums[mid] <= nums[-1]:  # mid is on the right rising portion
                    right = mid - 1
                else:  # mid is on the left rising portion
                    if target >= nums[0]:
                        right = mid - 1
                    else:
                        left = mid + 1
            else:
                return True
        return False


class Solution2:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Another approach without alterning nums and also cleans the binary
        search logic.
        """
        left = 0
        right = len(nums) - 1
        while nums and right > 0 and nums[right] == nums[0]:
            right -= 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] <= nums[right]:  # mid is on the right rising portion
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:  # mid is on the right rising portion
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False


sol = Solution2()
tests = [
    ([2, 5, 6, 0, 0, 1, 2], 0, True),
    ([2, 5, 6, 0, 0, 1, 2], 3, False),
    ([1, 1, 3, 1], 3, True),
    ([3, 1, 1, 1], 3, True),
    ([1], 1, True),
    ([1, 1, 1, 1, 1], 1, True),
    ([], 0, False),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.search(nums, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
