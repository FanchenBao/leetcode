# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, deque, Counter


class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        """Failed.

        This solution came from https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/discuss/2897887/Simple-solution-with-Diagram-and-Intuition-or-C%2B%2B-or-O(n)-Time-and-Space

        The great intuition is that we move all the numbers on bad indices to
        index 0. Then, the job is to redistribute them to the spaces available
        such that we can create a new array that is not identical to nums2. The
        important thing is that this redistribution is free, because we come to
        index 0 first. Say the current bad index is i and j. Then we just need
        to redistribute to j and i, essentially making a swap between i and j,
        and we are done. Thus, after collecting all the bad indices at index 0,
        the cost of redistribution is just the sum of all the collected indices.

        Note that after collecting the bad indices, it is possible that we might
        not have enough available spots to make the distribution. For instance

        nums1 = [2, 2, 2, 3, 3]
        nums2 = [3, 2, 2, 3, 1]

        After collection, the numbers to be redistributed are 2, 2, 3. The total
        available spots is three. Since we have two 2s, the min number of spots
        needed to spread out the 2s in nums1 and nums2 is four. So we need to
        include some of the good indices to increase the number of available
        spots. We go from small to large in the available indices, skip the
        value that is the same as the value of the max frequency
        (because including the value of the max frequency does not make the
        situation any better), until the number of available spots is at least
        double that of the max frequency. Each time a new index is included, we
        update the answer.
        """
        c1 = Counter()
        rem_indices = []
        res = 0
        N = len(nums1)
        for i, n in enumerate(nums1):
            if n == nums2[i]:  # count the occurrences of bad indices on both
                c1[n] += 1
                res += i  # index i is inevitable cost
            else:
                rem_indices.append(i)  # record the good indices in order
        if not c1:  # no need to swap
            return 0
        ava_for_dis = N - len(rem_indices)
        k = c1.most_common(1)[0][0]  # only consider the most common value in c1
        # Not enough spots to redistribute the most common value in c1,
        # we need to include good indices as well
        for idx in rem_indices:
            if 2 * c1[k] > ava_for_dis:
                # skip the same value as most frequent
                if k != nums1[idx] and k != nums2[idx]:
                    res += idx
                    ava_for_dis += 1
            else:
                break
        # return -1 if after including all available good indices still cannot
        # bump up the count of available spots enough
        return res if 2 * c1[k] <= ava_for_dis else -1


sol = Solution()
tests = [
    ([1,2,3,4,5], [1,2,3,4,5], 10),
    ([2,2,2,1,3], [1,2,2,3,3], 10),
    ([1,2,2], [1,2,2], -1),
    ([2, 4, 3, 1, 1], [4, 4, 3, 1, 5], 6),
    ([1,2,3], [3,1,2], 0),
    ([1, 3, 2, 2, 2, 5, 2, 5, 1, 3], [1, 5, 5, 2, 2, 2, 2, 5, 1, 2], 28),
    ([3, 4, 4, 3, 5, 1, 2, 2, 3, 4], [4, 4, 2, 3, 4, 2, 5, 2, 5, 1], 11),
    ([3, 4, 1, 4, 1, 1, 2, 3, 2, 2], [4, 4, 5, 3, 4, 3, 1, 3, 2, 4], 16),
    ([2,1,2,2,1,4,1,5], [2,1,2,2,1,4,1,5], 28),
    ([5, 4, 4, 4, 2], [1, 4, 3, 4, 5], 8),
    ([1, 5, 1, 5, 1], [1, 2, 1, 3, 2], 6),
    ([3, 2, 1, 3, 1, 5, 5, 3, 4, 3], [3, 3, 3, 2, 5, 5, 4, 3, 1, 2], 16),
]

for i, (nums1, nums2, ans) in enumerate(tests):
    res = sol.minimumTotalCost(nums1, nums2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
