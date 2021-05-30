# from pudb import set_trace; set_trace()
from typing import List
import itertools


class Solution1:
    def maximumGap(self, nums: List[int]) -> int:
        """LeetCode 164

        This is O(Nlog(N)), not exactly what is required.

        52 ms, 81% ranking.
        """
        nums.sort()
        return max([n2 - n1 for n1, n2 in zip(nums, nums[1:])] or [0])


class Solution2:
    def maximumGap(self, nums: List[int]) -> int:
        """Use radix sort to achieve O(N) time complexity
        92 ms. There is a lot of overhead creating radix sort, but technically
        it is O(N)
        """
        N = len(nums)
        if N == 1:
            return 0
        order = range(N)
        for i in range(10):
            buckets = [[] for _ in range(10)]
            all_zero = True
            for j in order:
                q = nums[j] // (10**i)
                d = q % 10
                buckets[d].append(j)
                if q:
                    all_zero = False
            order = itertools.chain(*buckets)
            if all_zero:
                break
        order = list(order)
        return max(nums[i2] - nums[i1] for i1, i2 in zip(order, order[1:]))


class Solution3:
    def maximumGap(self, nums: List[int]) -> int:
        """Bucket sort based on min value of the max gap between sorted numbers.
        The idea is to group all numbers into bins. The width of the bin is the
        average gap of the N numbers given its min and max value. This average
        gap is also the smallest max gap available (which occurs if all N numbers
        are evenly distributed from min to max)

        Once the numbers are placed in each bin, we don't have to worry about
        the gap within each bin, because that will always be smaller than the
        gap between bins. So we find the min and max within each bin, and compute
        the answer by the difference of the max of the current bin and the min
        of the next bin.

        Ref: https://leetcode.com/problems/maximum-gap/discuss/50643/bucket-sort-JAVA-solution-with-explanation-O(N)-time-and-space
        """
        N = len(nums)
        if N == 1:
            return 0
        min_num, max_num = min(nums), max(nums)
        bin_size = (max_num - min_num) // (N - 1) + 1
        bins = [[] for _ in range(N - 1)]
        for n in nums:
            b = (n - min_num) // bin_size
            if not bins[b]:
                bins[b] = [10**9 + 1, -1]
            bins[b][0] = min(bins[b][0], n)
            bins[b][1] = max(bins[b][1], n)
        bins = [bi for bi in bins if bi]  # remove all the empty bins
        res = bins[0][1] - bins[0][0]
        for b1, b2 in zip(bins, bins[1:]):
            res = max(res, b2[0] - b1[1])
        return res


sol = Solution3()
tests = [
    # ([3, 6, 9, 1], 3),
    # ([10], 0),
    # ([1, 100], 99),
    # ([1, 1, 1, 1], 0),
    ([100, 3, 2, 1], 97),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.maximumGap(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
