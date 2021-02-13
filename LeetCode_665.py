# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """This is not straightforward. My straightforward idea is to use stack
        and pop the odd ones out. It does not work, because it is hard to reason
        with the test case [1, 2, 3, 1]. If we pop odd one out, the final result
        would be stack = [1, 1] and oddones = [2, 3]. It's just impossible to
        tell whether this is a good or not.

        The changed solution does not use stack at all. It checks adjacent
        numbers. Whenever an odd one is discovered, i.e. the current value
        is larger than the next one, we need to make a decision whether the odd
        one is the current value or the next value. We can make this decision
        by checking the numbers surrounding the suspicious one. For instance,
        let's say we find that nums[i] > nums[i + 1]. If nums[i] is the odd one,
        then we must have nums[i - 1] <= nums[i + 1] or if nums[i] is the first
        value. Similarly, if nums[i + 1] is the odd one, then we must have
        nums[i] <= nums[i + 2] or if nums[i + 1] is the last value. If the above
        condition is met, then we have found an odd one that can be modified to
        maintain the increasing requirement. If neither of the above condition
        is met, then we already have a false result.

        We can continue this process and keep count of the number of changes.
        Once the number of changes becomes 2, we have a false result.

        O(N), 172 ms, 97% ranking.
        """
        num_change = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # check whether nums[i] is odd one
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                    num_change += 1
                # check whether nums[i + 1] is odd one
                elif i == len(nums) - 2 or nums[i] <= nums[i + 2]:
                    nums[i + 1] = nums[i]
                    num_change += 1
                else:
                    return False
            if num_change == 2:
                return False
        return True


sol = Solution()
tests = [
    ([4, 2, 3], True),
    ([4, 2, 1], False),
    ([1, 2, 3, 1], True),
    ([4, 5, 1, 2, 3], False),
    ([5, 7, 1, 8], True),
    ([1, 2, 3, 1, 2], False),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.checkPossibility(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
