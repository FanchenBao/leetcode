# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution1:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """LeetCode 2542

        Sort nums2 and rearange nums1 accordingly. We find the kth largest value
        in nums2, which serves as the largest smallest value in any chosen k
        values. We then put the last k values of rearranged nums1 into a heap.

        Each time we move the pointer on nums2 leftward, we check whether the
        corresponding value in nums1 is larger than the top of the heap. If it
        is larger, we swap the larger value in such that we ensure that the
        heap always holds the largest k values in nums1 so far.

        If it is not larger, we do not swap, but we still need to take it to
        compute the current score. This means we have to temporarily deduct the
        smallest value in the heap from the sum of nums1, because we have to add
        the current nums1 value.

        O(NlogN), 1098 ms, faster than 32.44% 
        """
        N = len(nums1)
        sorted_nums2 = sorted((n, i) for i, n in enumerate(nums2))
        aranged_nums1 = [nums1[i] for n, i in sorted_nums2]
        heap = []
        for i in range(N - k, N):
            heapq.heappush(heap, aranged_nums1[i])
        s1 = sum(heap)
        res = s1 * sorted_nums2[N - k][0]
        for i in range(N - k - 1, -1, -1):
            if aranged_nums1[i] > heap[0]:
                s1 -= heapq.heappop(heap)
                heapq.heappush(heap, aranged_nums1[i])
                s1 += aranged_nums1[i]
                res = max(res, s1 * sorted_nums2[i][0])
            else:
                res = max(res, (s1 - heap[0] + aranged_nums1[i]) * sorted_nums2[i][0])
        return res


class Solution2:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """We can zip nums1 and nums2, and build the heap along the way. Also
        note that we don't have to consider the condition where n1 <= heap[0],
        because if that happens, s1 and n2 will not be bigger than before, which
        means their product cannot be the bigger.

        O(NlogN), 972 ms, faster than 97.33%
        """
        heap = []
        res = s1 = 0
        for n2, n1 in sorted(zip(nums2, nums1), reverse=True):
            if len(heap) < k:
                heapq.heappush(heap, n1)
                s1 += n1
                if len(heap) == k:
                    res = s1 * n2
            elif n1 > heap[0]:
                s1 -= heapq.heappop(heap)
                heapq.heappush(heap, n1)
                s1 += n1
                res = max(res, s1 * n2)
        return res


sol = Solution2()
tests = [
    ([1,3,3,2], [2,1,3,4], 3, 12),
    ([4,2,3,1,1], [7,5,10,9,6], 1, 30),
    ([1,4], [3,1], 2, 5),
]

for i, (nums1, nums2, k, ans) in enumerate(tests):
    res = sol.maxScore(nums1, nums2, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
