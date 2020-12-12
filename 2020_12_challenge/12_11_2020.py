# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Two pointer solution. `i` is the left pointer, always pointing to
        a place for swap. `j` is the right pointer, always pointing to the next
        new number to check. We use `cur_n` to record the current number under
        consideration and `count` to keep track the number of times `cur_n` has
        repeated. Each time a new number is encounterd on `j` or the repeated
        number <= 2, we swap `i` and `j`. It the repeated number > 2, we do not
        swap and only increment j.

        O(N), 48 ms, 92% ranking.
        """
        i, j, length = 0, 0, len(nums)
        cur_n = -10001  # starting current number must not be part of nums
        count = 0
        while j < length:
            if nums[j] == cur_n:
                count += 1
            else:
                count = 1
                cur_n = nums[j]
            if count <= 2:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return i


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Just when you think your solution is good enough, Stefan Pochmann
        or Lee215 always drops a bomb. This is Pochmann's solution. Its elegance
        is beyond comprehension.

        We are still using two pointers, but we don't need a `count` or `cur_n`
        because we can check nums[i - 2] with nums[j] to achieve both. If
        nums[i - 2] != nums[j], then it is guaranteed that the max repeating
        is 2 or less. If they are equal, given that `nums` is sorted, we can
        also be sure that nums[i - 2] == nums[i - 1] == nums[j], which violates
        the requirement. Hence one check is enough.
        """
        i = 0
        for n in nums:
            if i < 2 or n != nums[i - 2]:
                nums[i] = n  # this is the swap
                i += 1
        return i


sol = Solution2()
tests = [
    ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
    ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
    ([1], 1, [1]),
    ([], 0, []),
    ([1, 2], 2, [1, 2]),
    ([1, 1, 1], 2, [1, 1]),
    ([1, 1, 1, 1, 1, 1, 1, 1], 2, [1, 1]),
]

for i, (nums, ans, ans_num) in enumerate(tests):
    res = sol.removeDuplicates(nums)
    if res == ans and nums[:ans] == ans_num:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Ans_Num: {nums[:res]}, Res: {res}')
