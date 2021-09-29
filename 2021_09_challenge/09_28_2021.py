# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """LeetCode 922

        Two pointers, one go with even positions and the other odd positions.
        We swap when both an even and odd positions are wrong. Otherwise, we
        move the even and odd position to the next one.

        O(N) time and in-place.

        212 ms, 66% ranking.

        UPDATE: have to read DBabichev's solution to realize that my original
        if conditions are total trash. It could be written in a much more
        succint manner.
        """
        ev, od = 0, 1
        while ev < len(nums) - 1 and od < len(nums):
            if nums[ev] & 1 == 0:
                ev += 2
            elif nums[od] & 1 == 1:
                od += 2
            else:
                nums[ev], nums[od] = nums[od], nums[ev]
        return nums


sol = Solution()
tests = [
   ([4, 2, 5, 7], [4, 5, 2, 7]),
   ([2, 3], [2, 3]),
   ([2, 3, 1, 1, 4, 0, 0, 4, 3, 3],[2, 3, 0, 1, 4, 1, 0, 3, 4, 3]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.sortArrayByParityII(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
