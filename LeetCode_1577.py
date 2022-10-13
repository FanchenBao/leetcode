# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
from bisect import bisect_right


class Solution1:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """This is naive O(M^2 + N^2) solution. M = len(nums1), N = len(nums2)

        It works because the length of
        input nums1 and nums2 are not longer than 1000.

        1729 ms, faster than 20.00%
        """

        def helper(a: List[int], b: List[int]) -> int:
            ac = Counter(a)
            bmc = Counter()
            for i in range(len(b)):
                for j in range(i + 1, len(b)):
                    bmc[b[i] * b[j]] += 1
            return sum(v * bmc[k * k] for k, v in ac.items())

        return helper(nums1, nums2) + helper(nums2, nums1)


class Solution2:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """Might be faster?? Yes it is.

        O(M + N + MlogM + NlogN + MNlogN + NMlogM)
        = O(MN(logM + logN))

        265 ms, faster than 89.38%

        UPDATE: no need to binary search. Two-sum is sufficient.

        O(MN), 114 ms, faster than 98.75%
        """
        n1_c = Counter(nums1)
        n2_c = Counter(nums2)
        n1_uniq = sorted(n1_c)
        n2_uniq = sorted(n2_c)

        def helper(ac, bc, buniq) -> int:
            res = 0
            for a, a_count in ac.items():
                for b in buniq:
                    q, r = divmod(a * a, b)
                    if q < b:
                        break
                    if r == 0 and q in bc:
                        res += a_count * (bc[b] * bc[q] if b != q else bc[b] * (bc[b] - 1) // 2)
            return res

        return helper(n1_c, n2_c, n2_uniq) + helper(n2_c, n1_c, n1_uniq)


sol = Solution2()
tests = [
    ([7,4], [5,2,8,9], 1),
    ([1,1], [1,1,1], 9),
    ([7,7,8,3], [1,2,9,7], 2),
]

for i, (nums1, nums2, ans) in enumerate(tests):
    res = sol.numTriplets(nums1, nums2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
