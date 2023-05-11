# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        """HINT

        The hint is very helpful. There are two key intuitions.

        1. The problem is equivalent to finding all subarrays whose XOR equals 0
        I get this one from last night's effort.

        2. A prefix XOR behaves exactly the same as prefix sum, in which the XOR
        from nums[i] to nums[j] is equal to prefix[j] ^ prefix[i - 1]. This
        insight I missed. With this insight, the problem is immediately
        simplified, because to find all the subarray ending at i whose XOR is
        zero, we just need to find all subarrays ending at i - 1 whose XOR is
        equal to nums[i]. That means, we want find all the js, such that
        prefix[j] ^ prefix[i - 1] = nums[i]

        This is equivalent to finding all prefix[j] whose value is prefix[i - 1]
        ^ nums[i]. We can use a counter to keep track the number of each
        prefix[j], and the problem is solved.

        O(N), 1271 ms, faster than 14.07%
        """
        prexor = [0]
        counter = Counter([0])
        res = 0
        for i in range(len(nums)):
            res += counter[nums[i] ^ prexor[-1]]
            prexor.append(prexor[-1] ^ nums[i])
            counter[prexor[-1]] += 1
        return res


class Solution2:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        """Same as Solution1, but with better implementation. We don't need to
        keep the entire prefix xor array, only the last one will suffice.

        Ref lee215: https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/discuss/3286372/JavaC%2B%2BPython-Prefix-XOR

        O(N), 1146 ms, faster than 46.63%
        """
        pxor = res = 0
        counter = Counter([0])
        for n in nums:
            res += counter[n ^ pxor]
            pxor ^= n
            counter[pxor] += 1
        return res


sol = Solution2()
tests = [
    ([4,3,1,2,4], 2),
    ([1,10,4], 0),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.beautifulSubarrays(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
