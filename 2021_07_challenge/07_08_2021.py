# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """LeetCode 718

        1D array DP solution. O(N1 * N2), 3156 ms, 73% ranking.
        """
        res = 0
        n1, n2 = len(nums1), len(nums2)
        dp = [0] * (n1 + 1)
        for i in range(n2):
            temp = [0] * (n1 + 1)
            for j in range(n1):
                if nums1[j] == nums2[i]:
                    temp[j + 1] = dp[j] + 1
                    res = max(res, temp[j + 1])
            dp = temp
        return res


class Solution2:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """Pre-build a mapping for nums1 to speed things up. But overall run
        time is the same as Solution1.
        """
        nums1_map = defaultdict(list)
        for i, n in enumerate(nums1):
            nums1_map[n].append(i)
        res, n1 = 0, len(nums1)
        dp = [0] * (n1 + 1)
        for n in nums2:
            temp = [0] * (n1 + 1)
            for j in nums1_map[n]:
                temp[j + 1] = dp[j] + 1
                res = max(res, temp[j + 1])
            dp = temp
        return res


class Solution3:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """Courtesy to Mr. Pochmann:

        https://leetcode.com/problems/maximum-length-of-repeated-subarray/solution/131304

        This is the binary search solution suggested by the official solution.
        However, Mr. Pochmann tweaked it such that we build strings for
        comparison instead of tuples. The fact that the values in the arrays are
        between 0 and 100 allows us to transform each value to an ASCII char.

        116 ms. Lightning fast
        """
        str1 = ''.join(chr(n) for n in nums1)
        str2 = ''.join(chr(n) for n in nums2)

        def check(length):
            set1 = set(str1[i:i + length] for i in range(len(str1) - length + 1))
            set2 = set(str2[i:i + length] for i in range(len(str2) - length + 1))
            return any(s2 in set1 for s2 in set2) if len(set2) < len(set1) else any(s1 in set2 for s1 in set1)

        lo, hi = 0, min(len(str1), len(str2)) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1


sol = Solution3()
tests = [
    ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7], 3),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 5),
    ([], [1, 2, 3], 0),
]

for i, (nums1, nums2, ans) in enumerate(tests):
    res = sol.findLength(nums1, nums2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
