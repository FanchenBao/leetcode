# from pudb import set_trace; set_trace()
from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        """LeetCode 384

        The idea is to swap. We first focus on index 0 in nums. We ask the
        question: which value in nums can be randomly selected to replace the
        value at index 0. For that we use random.randint(0, len(nums) - 1) to
        find the index for swap. Next, we determine which value in nums,
        excluding the first one, can be randomly selected to replace the value
        at index 1. We keep doing this until all possible positions in nums are
        swapped. This is correct because each position is randomly selected
        among the remaining possible values.

        O(N) for both reset and shuffle. 312 ms, 62% ranking.
        """
        self.original = nums
        self.nums = nums[:]
        self.N = len(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(self.N - 1):
            idx = random.randint(i, self.N - 1)
            self.nums[i], self.nums[idx] = self.nums[idx], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
