# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left


class Solution1:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """Very convoluted my solution is.

        We keep track of the best two numbers we have seen so far in tup, such
        that tup[0] < tup[1] and both are the best candidate so far.

        To maintain the best candidate state of tup, we check each pair of
        numbers and denote them as l and r.

        If r > tup[1], then we already have the result tup[0] < tup[1] < r.

        If r <= tup[1], there are two cases, either l < r or l >= r.
            If l < r, l has two cases. either l > tup[0] or l <= tup[0]. If
            l > tup[0], we have the result tup[0] < l < r. If l <= tup[0], we
            replace tup with [l, r]

            If l >= r.
                if r > tup[1], no need to update tup.
                If tupe[1] > r > tup[0], r is currently a better candidate than
                tup[1], so we replace tup[1] with r.
                If r < tup[0] and tup[0] < l < tup[1], l is a better candidate
                than tup[1], so we replace tup[1] with l.
                if l < tup[0], no need to update tup.

        O(N), 56 ms, 47% ranking.
        """
        tup = [math.inf, math.inf]
        for i in range(len(nums) - 1):
            l, r = nums[i], nums[i + 1]
            if r > tup[1]:
                return True
            if l < r:
                if tup[0] < l:
                    return True
                else:
                    tup = [l, r]
            else:
                if r > tup[0]:
                    tup[1] = r
                elif tup[0] < l < tup[1]:
                    tup[1] = l
        return False


class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """Similar idea as Solution1, but MUCH MUCH better implemented.
        from https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3570/discuss/78995/Python-Easy-O(n)-Solution
        """
        lst = [math.inf, math.inf]  # keep track the smallest two numbers
        for n in nums:
            if n <= lst[0]:
                lst[0] = n
            elif n <= lst[1]:
                lst[1] = n
            else:
                return True
        return False


class Solution3:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """Generalized method using binary search to update a list of smallest
        values encountered so far
        """
        lst = [math.inf] * 2  # if the requirement is k-sequence, use k - 1 here
        for n in nums:
            idx = bisect_left(lst, n)  # find the appropriate position for n
            if idx == 2:  # or k - 1
                return True
            lst[idx] = n  # replace with n, which is a better option
        return False


sol = Solution3()
tests = [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], False),
    ([2, 1, 5, 0, 4, 6], True),
    ([5, 1, 5, 5, 2, 5, 4], True),
    ([1], False),
    ([1, 2], False),
    ([3, 2], False),
    ([1, 2, 1, 2, 1, 2, 1], False),
    ([-51, -64, 78, 58, 31, 39, 16, 91, -88, -69, -90, 72, 61, -55, 78, -39, 69, 15, -64, -52, 92, -81, 54, -65, -96, -4, -54, 3, -33, -87, -56, 23, -44, 3, 67, 99, 13, 19, 53, -35, 35, 84, 54, -98, 46, 37, 58, -65, 97, 91, 42, 30, 15, -5, -96, 46, -18, 35, -49, 95, 81, 65, -64, -70, -71, 56, -33, -40, -5, -5, -37, 55, 54, 98, -18, -11, -96, -73, -33, -71, -10, -34, 75, 33, 10, 59, 35, -15, -10, -64, 94, -18, -27, -91, 79, -38, -27, -93, 37, -56, -79, 89, -6, -87, 13, 61, 9, -98, 46, -28, 9, -18, 54, -11, 37, 91, -98, 84, 46, -79, -79, 96, -60, -59, 53, -9, -63, 84, -92, 59, -83, 84, 3, -19, -74, 53, 31, 61, 7, -35, -53, 17, -12, 95, 25, 30, 48, 40, -86, -39, 20, 82, 63, 50, -67, 94, 31, -58, 58, 96, 98, 1, 9, -70, -20, -8, 77, -26, 50, -90, 37, 68, -21, 84, -32, -45, 37, -48, -81, 18, 41, -86, -66, 90, 45, -92, 21, 35, 2, 63, 98, 55, 64, 20, 47, 1, 76, -64, -21, 24, -6, -60, 77, 76, -25, -42, 35, 96, 41, 80, 28, -17, -50, 61, -90, -73, 28, 90, -20, -100, -22, 36, -81, 33, 56, -70, 42, 54, 91, 45, 40, 92, 41, 6, 69, 67, -83, 78, 24, -92, 80, -56, 50, 69, -47, -57, -24, -89, -82, -88, 51, -19, 0, 68, -61, -84, -74, -18, -36, 67, -28, -89, -97, 11, -89, 27, -36, -53, -9, -9, 14, 43, 21, -36, 21, 90, -86, 21, 71, 29, 10, -68, -61, -79, 10, -35, 38, -30, 17, 85, -13, -53, -3, 92, -43, 30, 98, -17, -67, -89, -55, -77, 36, -10, -94, -8, 45, 31, 80, 35, -79, 32, 2, -73, -63, 18, -6, 70, -62, -25, 99, -49, -4, -70, 99, -64, 54, -44, -4, -77, 24, -89, 44, -17, 37, 50, 57, 19, 47, -58, 3, -74, 73, 92, 17, 61, 50, -98, -90, -81, -64, -21, 53, -3, 8, -56, -96, 62, -46, -31, -77, -47, 26, 13, -28, 96, -76, 53, -19, -98, 43, -91, 44, -67, -35, -42, 87, 5, -22, -47, 98, -32, -93, 80, -64, 95, -78, -92, -64, 24, -100, -4, -12, -76, -8, -21, -4, 40, 52, -27, -27, -32, -11, -79, 93, -96, -19, 52, 59, 86, -8, 68, 5, -41, -18, 91, 89, -94, -38, -99, 50, -87, 91, 21, 10, 48, 71, -35, 85, -59, -91, -65, -26, 18, -45, -19, 29, -47, -52, -75, 54, -80, 57, -45, 13, -92, 27, 41, 70, -9, -17, -67, -36, 64, -19, 20, 25, 33, -41, -40, -85, 74, 71, 75, 62, 24, -33, 29, 27, 64, -25, -81, -46, 61, -13, 37, -52, 74, 56, -4, -98, 24, 52, -9, 73, -71, -41, -36, 56, -6, 12, -50, 44, 42, 94, -51, 76, 75, 9, -20, -82, -40, -70, 49, -80, 100, 14, 69, -70, -56, 42, -97, 37, 54, 68, -44, 84, -45, -12, 86, 79, -94, -63, -21, 25, 92, -70, -92, -41, 84, -25, 69, 80, 96, -43, -96, 35, -62, -10, -60, 92, -71, -53, -17, 68, -18, 12, -8, -46, 78, 46, -84, 78, -77, -78, 61, 43, -20, -31, -100, -1, -76, -83, -29, 73, 88, -10, 38, 92, 91, 82, 91, 59, -76, 23, -55, 70, -44, 47, 78, 40, 4, 78, -89, 46, 59, -94, 8, -49, 33, -71, 4, 68, 75, 17, 74, 90, -53, 53, -4, 87, 7, 8, -29, -48, -73, -3, -73, -41, -72, -84, -67, 54, 63, -21, 20, -25, 14, 92, -38, 14, -71, -75, 95, -3, 70, 54, -83, -100, -80, 17, 13, 29, 28, 98, -28, -44, -98, 100, -53, 12, -95, 70, -18, 73, -92, -46, 9, -89, -90, -63, 84, 76, -15, -57, 27, -92, -66, -4, -22, 23, -77, 23, 79, 87, 92, 3, 54, 61, 74, -3, -96, 59, -60, 50, -68, 37, -36, 44, 53, 56, -63, -34, -29, 63, -72, 39, 16, -95, -25, -36, -91, -37, 31, -25, 59, -8, 88, 43, 14, -15, 22, -62, 81, -53, 16, -47, -63, -57, -92, -60, 35, -7, -64, 31, -66, -66, -99, 80, 2, -28, 17, -75, 98, -34, 47, -21, 33, -9, -90, 24, -6, -45, -18, 46, 57, 68, -72, -9, 56, -36, -82, -47, 51, -28, 76, 75, 46, 68, -40, 90, 15, -94, 10, 1, -68, 68, -90, -24, -55, 43, 3, 56, -60, 7, -93, -1, 10, 9, 69, 100, -61, 37, 29, 37, 99, 72, -52, 21, -73, 47, -44, -82, 69, -42, -72, -46, -52, -47, -42, -15, 39, -14, -84, 42, 85, -34, -11, 63, -32, -68, 44, 47, -41, 68, -72, 65, -4, -11, -34, -72, -49, 72, -21, -13, 80, 43, -50, 18, -80, 18, 69, -31, 24, -23, 76, -11, -12, 17, -36, -58, -74, -33, 8, 53, -33, -76, -3, -84, -90, 40, -17, -37, 36, -78, -68, -22, -6, -87, 5, -1, -72, 2, 59, -54, 47, 38, 83, 83, -32, 54, -16, -33, 40, 21, 10, -42, 41, 57, -8, 84, -75, -50, 48, 92, 92, -60, -86, 27, 58, 66, -31, -44, -100, 76, 20, 37, 79, -42, 82, 11, -45, -45, 27, 95, 43, 58, 72, 11, 37, 33, 6, -65, -12, 92, -66, 75, -84, -21, 6, -52, 4, 24, 13, -61, 6, 10, 97, -87, 45, -25, -43, 0, 77, 31, 62, 60, -46, 74, 93, -71, 45, 72, 26, 8, 21, 16, 8, 94, -98, 65, 59, 2, 89, -19, 18, 92, 66, -53, -88, -26, 68, -51, 49, -96, 30, -86, 88, -1, 2, 40, -47, -60, -14, -69, 97, -93, -9, -67, 39, -7, 78, -46, 49, -67, 15, -76, -14, -34, -22, 34, -56, 49, 71, -93, 99, -61, 8, -80, -90, -52, -53, -39, -25, -24, -28, 8, -13, -16, -46], True),
    ([1, 1, 1, 1, 1, 1], False),

]

for i, (nums, ans) in enumerate(tests):
    res = sol.increasingTriplet(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
