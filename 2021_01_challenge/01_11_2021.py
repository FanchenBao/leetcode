# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Naive approach, direct insert using the slice trick.

        O(N^2), 60 ms, 5% ranking.
        """
        for _ in range(n):
            nums1.pop()
        nums1.append(10**9 + 1)   # dummy max value
        i, j = 0, 0
        while j < n:
            if nums1[i] > nums2[j]:
                nums1[i:i] = [nums2[j]]
                j += 1
            i += 1
        nums1.pop()


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Another cheating method. Use an additional array for merging sort.

        O(N), 40 ms, 35% ranking.
        """
        if n == 0:
            return
        if m == 0:
            for i, n in enumerate(nums2):
                nums1[i] = n
            return
        sorted_nums = []
        nums1[m] = 10**9 + 1  # dummy max value
        nums2.append(10**9 + 1)   # dummy max value
        i, j = 0, 0
        while i < m or j < n:
            if nums1[i] > nums2[j]:
                sorted_nums.append(nums2[j])
                j += 1
            else:
                sorted_nums.append(nums1[i])
                i += 1
        for i, t in enumerate(sorted_nums):
            nums1[i] = t


class Solution3:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """I got kinda stuck, on an EASY question. I checked the solution and
        the answer is very simple: start from the end!!!

        O(N), 44 ms, 14% ranking.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


sol = Solution3()
tests = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    ([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5, [1, 2, 3, 4, 5, 6]),
]

for i, (nums1, m, nums2, n, ans) in enumerate(tests):
    res = sol.merge(nums1, m, nums2, n)
    if nums1 == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {nums1}')
