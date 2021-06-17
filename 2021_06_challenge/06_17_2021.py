# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        """LeetCode 795

        Two observations. First, anytime a value larger than right is
        encountered, it splits the array into two parts. Or in other words, the
        values to the right of the large value has no impact on the values to
        the left of the large value. This means we can isolate each segment of
        subarray surrounded by large values.

        Second, within each viable subarray segment, we need to find out the
        consecutive subarrays of small values. All subarray from these small
        values must be deducted from the total subarrays of the viable segment.
        This can be achieved by keeping track of the indices of the small
        values encountered, and count the length of contiguous subarray
        containing only small values.

        Once we find the length of the viable subarray (M), and a list of
        lengths (List) of the small value subarrays within the viable
        subarray, the computation is straightforward:
        (M + 1) * M / 2 - sum((m + 1) * m / 2 for m in List)

        We then add up all the computations of each viable subarray segment and
        reach the result.

        O(N), 340 ms, 54% ranking.
        """
        smalls = []
        start = -1
        res = 0
        nums.append(math.inf)
        for i, n in enumerate(nums):
            if n < left:
                if smalls and smalls[-1][1] + 1 == i:
                    smalls[-1][0] += 1
                    smalls[-1][1] = i
                else:
                    smalls.append([1, i])
            elif n > right:
                seg_len = i - start - 1
                num_small_subarr = sum(c * (c + 1) // 2 for c, _ in smalls)
                res += seg_len * (seg_len + 1) // 2 - num_small_subarr
                start = i
                smalls = []
        return res


class Solution2:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        """This is the same idea as mine, but much better implementation.
        Ref: https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/1278426/JS-Python-Java-C%2B%2B-or-Easy-Triangular-Number-Solution-w-Explanation

        Note that the exact implementation is different.
        """
        res = 0
        vc = 0  # count of consecutive valid numbers
        sc = 0  # count of consecutive numers that are too small
        nums.append(math.inf)
        for n in nums:
            if n <= right:
                vc += 1
            if n < left:
                sc += 1
            if n >= left:
                res -= sc * (sc + 1) // 2  # exclude all too small subarrays
                sc = 0
            if n > right:
                res += vc * (vc + 1) // 2  # include all potentially valid subarrays
                vc = 0
        return res


class Solution3:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        """This is another solution from here:
        https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/1278743/C%2B%2BJavaPython-Easy-to-understand-solution-Clean-and-Concise-O(N)

        The idea is that we find the total number of subarrays that are smaller
        or equal to right. Then we find the total number of subarrays that are
        smaller than left. The answer is the difference between the two.

        332 ms.
        """

        def count(bound):
            res, c = 0, 0
            for n in nums:
                c += 1 if n <= bound else -c
                res += c  # note that we are not using formula here
            return res

        return count(right) - count(left - 1)


sol = Solution3()
tests = [
    ([2, 1, 4, 3], 2, 3, 3),
]

for i, (nums, left, right, ans) in enumerate(tests):
    res = sol.numSubarrayBoundedMax(nums, left, right)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
