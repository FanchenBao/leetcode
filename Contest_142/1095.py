# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

"""
Date: 06/23/2019

I realized that this was going to be some sort of binary search pretty fast, yet the implementation took quite a while and I timed out for the contest. I then used trial-and-error (not recommended to be honest) to test the correctness of the code and eventually got it passed. The intuition was straightforward: pick two spots on the array, if the first one is smaller than the second one, then we are on the rising edge and we can be sure the left side of the array must be increasing while the right side could be a new mountain array. We would then binary search the left side first, and then recursively search the mountain array on the right. Similarly, if the first one is larger than the second one, then we must be on the falling edge on the right side. Then we recursively search the left side mountain array first, and if that didn't return anything, we do the binary search on the right side.

Two obstacles I faced in this problem was: one, I used too many .get() calls, and two, the index I returned was the not first appearance of the target. To tackle these two issues, I wrote some speghetti code where I tried to eliminate as many .get() calls as possible without improving the logic of the algorithm. While I was reducing .get() calls, I sometimes messed up with the logic and the second problem popped up. Fortunately, this code passed OJ eventually, but I suspected that there could be some improvements.


Update: I read the top solution from the discussion and found that a more intuitive solution was to first locate the peak using binary search, then search the target on the left and right slopes. The way to find the peak was similar to my method. First find the mid value, and the value after the mid value. If midVal < rightMidVal, peak must be on the right side; similarly if midVal > rightMidVal, peak must be on the left side. For code of finding the peak, check out my Java answer at "https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/". The python answer was for the lols.
"""


class Solution:
    def findInMountainArray(self, target, mountain_arr):
        return self.auxSearch(
            mountain_arr, 0, mountain_arr.length() - 1, target
        )

    def auxSearch(self, mountain_arr, start, end, target):
        if start > end:  # anchor case
            return -1

        mid = (start + end) // 2
        midVal = mountain_arr.get(mid)
        if (
            mid == end
        ):  # using midVal and rightVal makes edge case checking a bit easier, because there is only one situation where mid could be the same as end: start == end
            return mid if midVal == target else -1

        rightMidVal = mountain_arr.get(mid + 1)
        if midVal < rightMidVal:  # we are on rising slope
            if (
                target > rightMidVal
            ):  # target will not be on the rising slope. So directly searching the mountain_arr on the right
                return self.auxSearch(mountain_arr, mid + 2, end, target)
            else:
                pos = self.binSearch(
                    mountain_arr, start, mid + 1, target, True
                )
                if pos >= 0:
                    return pos
                else:
                    return self.auxSearch(mountain_arr, mid + 2, end, target)

        else:  # we are on falling slope
            pos = self.auxSearch(
                mountain_arr, start, mid - 1, target
            )  # no matter what, search the left side first
            if pos >= 0:
                return pos
            if (
                target > midVal
            ):  # target not on the left side, but also larger than leftMidVal, target is not in the array
                return -1
            else:  # target has to be on the right side
                return self.binSearch(mountain_arr, mid, end, target, False)

    def binSearch(self, mountain_arr, start, end, target, rising):
        res = -1
        while start <= end:
            mid = (start + end) // 2
            midVal = mountain_arr.get(mid)  # reduce total .get() call
            if target < midVal:
                if rising:
                    end = mid - 1
                else:
                    start = mid + 1
            elif target > midVal:
                if rising:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                res = mid
                break
        return res
