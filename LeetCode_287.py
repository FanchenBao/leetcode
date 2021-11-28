# from pudb import set_trace; set_trace()
from typing import List


class Solution1: 
    def findDuplicate(self, nums: List[int]) -> int:
        """We did get this one using O(N) time and O(1) extra space. My idea is
        to count the number of one-bit at each position from 1 to n without
        duplication. This is the baseline. Then we count the same thing for nums.
        Then, we compare the two counts. If a position in the dup count is
        larger than the non-dup count, that position must be set in the actual
        dup number.

        2988 ms, 5% ranking.

        UPDATE: use bit_length() to reduce the counter size.
        """
        max_n = max(nums)
        counters_uni = [0] * max_n.bit_length()
        N = len(nums) - 1
        for n in range(1, max_n + 1):
            for i, b in enumerate(format(n, f'0{max_n.bit_length()}b')):
                counters_uni[i] += (b == '1')
        counters = [0] * max_n.bit_length()
        for n in nums:
            for i, b in enumerate(format(n, f'0{max_n.bit_length()}b')):
                counters[i] += (b == '1')
        return int(''.join('1' if c2 > c1 else '0' for i, (c1, c2) in enumerate(zip(counters_uni, counters))), 2)


class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        """Binary search from the official solution.

        https://leetcode.com/problems/find-the-duplicate-number/solution/

        O(NlogN), 996 ms, 17% ranking.
        """
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(n <= mid for n in nums) <= mid:
                lo = mid + 1
            else:
                hi = mid
        return lo


class Solution3:
    def findDuplicate(self, nums: List[int]) -> int:
        """The official solution version of Solution1.

        The main difference is that this version does not involve converting
        numbers to binary. Instead, we use a mask to handle bit counting.
        """
        dup = 0
        bit_len = max(nums).bit_length()
        for bit in range(bit_len):
            mask = 1 << bit
            non_dup_count = 0
            dup_count = 0
            for i, n in enumerate(nums):
                # note that i goes from 0 to n. We want i to go from 1 to n, but
                # fortunately, the case of i == 0 is handled gracefully by
                # i & mask returns false.
                non_dup_count += 1 if i & mask else 0
                dup_count += 1 if n & mask else 0
            if non_dup_count < dup_count:
                dup |= mask
        return dup


class Solution4:
    def findDuplicate(self, nums: List[int]) -> int:
        """Tortoise and hare.

        Dup signifies a cycle in the linked list that is created by linking the
        value at nums[i] to the value at nums[nums[i]]

        O(N) time, O(1) extra space. 596 ms, 90% ranking.
        """
        t, h = nums[0], nums[0]
        while True:
            t = nums[t]
            h = nums[nums[h]]
            if t == h:
                break
        t = nums[0]
        while t != h:
            t = nums[t]
            h = nums[h]
        return t


sol = Solution4()
tests = [
    ([1,3,4,2,2], 2),
    ([3,1,3,4,2], 3),
    ([1,1], 1),
    ([1,1,2], 1),
    ([3,1,3,4,2,3,3,3,3,3,3], 3),
    ([2,2,2,2,2], 2),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findDuplicate(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
