# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution1:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """Sorted nums2 and reorder nums1 according to the reordered indices
        in nums2. Then we know the maximum min in nums2 is sorted_nums2[-k].
        We also know at this point the sum of nums1 is sum(reordered_nums1[-k:])

        This is our starting point. Then we put the k values in nums1 into a
        heap. We move the pointer from -k left one at a time.

        We know that the min in nums2 is going smaller. Thus the only way to
        find a larger product is for the sum in nums1 to be big. Thus, we use
        the heap to keep the largest sum of k values in nums1. Specifically, at
        each step, we pop the top of the heap and add the new value. If the new
        sum is larger than the old sum, we keep the larger sum and compute a
        new possible product. Otherwise, we skip the new value.

        Do this until we exhaust all numbers and we are done.

        O(NlogN), 1102 ms, faster than 80.97%
        """
        sorted_nums2 = sorted((n, i) for i, n in enumerate(nums2))
        reordered_nums1 = [nums1[i] for _, i in sorted_nums2]
        heap = []
        j = len(nums1) - 1
        s = 0
        for _ in range(k):
            s += reordered_nums1[j]
            heapq.heappush(heap, reordered_nums1[j])
            j -= 1
        res = s * sorted_nums2[-k][0]
        while j >= 0:
            new_s = s - heap[0] + reordered_nums1[j]
            if new_s > s:
                heapq.heappop(heap)
                heapq.heappush(heap, reordered_nums1[j])
                res = max(res, new_s * sorted_nums2[j][0])
                s = new_s
            j -= 1
        return res


class Solution2:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """Inspired by lee215

        https://leetcode.com/problems/maximum-subsequence-score/discuss/3082106/JavaC%2B%2BPython-Priority-Queue

        1107 ms, faster than 79.99%
        """
        heap = []
        s = res = 0
        for b, a in sorted(zip(nums2, nums1), reverse=True):
            if len(heap) < k:
                heapq.heappush(heap, a)
                s += a
                if len(heap) == k:
                    res = s * b
            elif a > heap[0]:
                s -= heapq.heappop(heap)
                heapq.heappush(heap, a)
                s += a
                res = max(res, s * b)
        return res


sol = Solution2()
tests = [
    ([1,3,3,2], [2,1,3,4], 3, 12),
    ([4,2,3,1,1], [7,5,10,9,6], 1, 30),
]

for i, (nums1, nums2, k, ans) in enumerate(tests):
    res = sol.maxScore(nums1, nums2, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
