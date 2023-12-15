# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        """
        The essense of the problem is that given nums[i:j] that are
        continuous and with any pairs not differ by more than 2. Now
        we have a next value nums[j + 1]. If it also falls inline, we
        simply extend the array.

        However, if nums[j + 1] is too big or too small, we need to find
        the right most value in nums[i:j] that differs from nums[j + 1]
        by more than 2. The next continous subarray will start from the
        right neighbor of this value.

        How can we find this value without going back one by one? I use
        monotonic stack. Two stacks to be exact, one increasing and the
        other decreasing. Since the diff within a good continuous stack
        is no more than 2, the size of the stack will not be more than 3.

        If nums[j + 1] is too big, we go through the monotomic increasing
        stack from right to left to identify the right most value V that
        cannot fit nums[j + 1]. Since we record its index, and also the
        index of the start of the current subarray, we can easily compute
        the total number of subarrays in that range. Then we reset the
        stack by removing all the elements to the left of V (including V)
        and push the current value into the stack.

        If nums[j + 1] is too small, we use the monotonic decreasing stack
        the same way as described above.

        O(N), 723 ms, faster than 70.91%
        """
        lo = 0
        res = 0
        inc_stack = [(nums[0], 0)]
        dec_stack = [(nums[0], 0)]
        for i in range(1, len(nums)):
            if nums[i] > inc_stack[-1][0]:
                for j in range(len(inc_stack) - 1, -1, -1):
                    if nums[i] - inc_stack[j][0] > 2:
                        cl = i - lo
                        cr = i - inc_stack[j][1]
                        res += (cr + cl) * (cl - cr + 1) // 2
                        lo = inc_stack[j][1] + 1
                        inc_stack = inc_stack[j + 1:]
                        break
            elif nums[i] < dec_stack[-1][0]:
                for j in range(len(dec_stack) - 1, -1, -1):
                    if dec_stack[j][0] - nums[i] > 2:
                        cl = i - lo
                        cr = i - dec_stack[j][1]
                        res += (cr + cl) * (cl - cr + 1) // 2
                        lo = dec_stack[j][1] + 1
                        dec_stack = dec_stack[j + 1:]
                        break
            # update the stacks
            while inc_stack and inc_stack[-1][0] >= nums[i]:
                inc_stack.pop()
            inc_stack.append((nums[i], i))
            while dec_stack and dec_stack[-1][0] <= nums[i]:
                dec_stack.pop()
            dec_stack.append((nums[i], i))
        count = len(nums) - lo
        return res + (count + 1) * count // 2


sol = Solution()
tests = [
    ([5,4,2,4], 8),
    ([1,2,3], 6),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.continuousSubarrays(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
