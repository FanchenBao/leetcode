# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """LeetCode 905

        The most naive solution

        O(N) space and O(N) time
        153 ms, faster than 12.49% 
        """
        return [n for n in nums if not n % 2] + [n for n in nums if n % 2]


class Solution2:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """O(1) space, O(N) time.

        101 ms, faster than 54.69%
        """
        i, j = 0, len(nums) - 1
        while i < j:
            if not nums[i] % 2:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        return nums


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
