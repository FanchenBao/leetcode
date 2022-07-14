# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


# class TreeNode:
#     def __init__(self, lo: int, hi: int) -> None:
#         self.lo = lo
#         self.hi = hi
#         self.count = 0
#         self.partial = False
#         self.left = None
#         self.right = None

#     def __repr__(self):
#         return f'({self.lo}, {self.hi})'


# class CountIntervals:

#     def __init__(self):
#         """This works, but TLE when there are A LOT of non-overlapping
#         intervals over a HUGE range.
#         """
#         self.root = TreeNode(1, 10**9)
#         self.is_last_add = False
#         self.cur_count = 0

#     def _update(self, node: TreeNode, lo: int, hi: int) -> None:
#         node.partial = True
#         if node.lo == lo and node.hi == hi:
#             node.count = hi - lo + 1
#             return
#         mid = (node.lo + node.hi) // 2
#         if not node.left:
#             node.left = TreeNode(node.lo, mid)
#         if not node.right:
#             node.right = TreeNode(mid + 1, node.hi)
#         if hi <= mid:
#             self._update(node.left, lo, hi)
#         elif lo > mid:
#             self._update(node.right, lo, hi)
#         else:
#             self._update(node.left, lo, mid)
#             self._update(node.right, mid + 1, hi)

#     def _query(self, node: TreeNode) -> int:
#         if not node or not node.partial:
#             return 0
#         if node.count:
#             return node.count
#         lr = self._query(node.left)
#         rr = self._query(node.right)
#         if node.left and node.left.count and node.right and node.right.count:
#             node.count = node.left.count + node.right.count
#         return lr + rr

#     def add(self, left: int, right: int) -> None:
#         self._update(self.root, left, right)
#         self.is_last_add = True

#     def count(self) -> int:
#         if self.is_last_add:
#             self.cur_count = self._query(self.root)
#         self.is_last_add = False
#         return self.cur_count


class CountIntervals:

    def __init__(self):
        """Finally got this done. The inspiration comes from here:
        https://leetcode.com/problems/count-integers-in-intervals/discuss/2039706/Merge-Intervals

        We use a dict to keep track of all current NON-overlapping intervals.
        The dict's key is the left interval and the value the right interval.
        Each time a new interval is added, we sort the keys and binary search
        to locate where the new left can be. Then we iterate through all the
        lefts bigger than the current one and see how many intervals can be
        popped. Eventually, we add the newly merged interval and update the
        total count along the way.

        O(NlogN) per add() call, O(1) per count() call.
        1379 ms, faster than 70.76% 
        """
        self.intervals = {}
        self.cur_count = 0
        self.max_right = -math.inf
        self.min_left = math.inf

    def add(self, left: int, right: int) -> None:
        if not self.intervals:
            self.intervals[left] = right
            self.max_right = right
            self.min_left = left
            self.cur_count = right - left + 1
        else:
            if right < self.min_left:
                self.intervals[left] = right
                self.min_left = left
                self.cur_count += right - left + 1
            elif left > self.max_right:
                self.intervals[left] = right
                self.max_right = right
                self.cur_count += right - left + 1
            else:
                lefts = sorted(self.intervals)
                idx = bisect_right(lefts, left)
                if idx and self.intervals[lefts[idx - 1]] >= left:
                    pre_left = lefts[idx - 1]
                    if self.intervals[pre_left] >= right:
                        # current inveral completely covered by previous interval
                        return
                    self.cur_count -= self.intervals.pop(pre_left) - pre_left + 1
                    left = pre_left
                for i in range(idx, len(lefts)):
                    l = lefts[i]
                    if l <= right:
                        if self.intervals[l] <= right:
                            self.cur_count -= self.intervals[l] - l + 1
                            self.intervals.pop(l)
                        else:
                            new_right = self.intervals.pop(l)
                            self.cur_count -= new_right - l + 1
                            right = new_right
                            break
                    else:
                        break
                self.intervals[left] = right
                self.cur_count += right - left + 1
                self.min_left = min(self.min_left, left)
                self.max_right = max(self.max_right, right)
            # print(self.intervals, self.cur_count, self.min_left, self.max_right)

    def count(self) -> int:
        return self.cur_count


actions = ["CountIntervals","add","add","add","count","count","count","add","add","add","count","add","count","add","count","count","count","count","count","add","add","add","add","count","add","count","add","count","count","add","count","count","add","count","count","count","add","add","add","count","add","add","add","add","count","add","count","count","add","add","add","add","add","count","count","add","add","count","count","count","add","add","add","add","count","add","add","add","count","count","count","count","add","count","count","add","add","count","add","count","count","add","add","count","add","add","add","count","add","add","add","add","count","count","count","add","count","add","add","count","add","add","count","add","add","add","count","add","add","add","count","count","count","add","count","add","add","add","count","add","count","count","count","add","count","count","count","add","count","count","add","count","add"]
values = [[],[365,897],[261,627],[781,884],[],[],[],[328,495],[224,925],[228,464],[],[416,451],[],[747,749],[],[],[],[],[],[740,757],[51,552],[20,896],[459,712],[],[383,670],[],[701,924],[],[],[392,591],[],[],[935,994],[],[],[],[398,525],[335,881],[243,517],[],[995,1000],[15,335],[430,490],[376,681],[],[733,841],[],[],[603,633],[974,978],[466,786],[241,753],[259,887],[],[],[410,514],[173,300],[],[],[],[805,957],[272,805],[723,858],[113,118],[],[426,987],[318,997],[741,978],[],[],[],[],[701,992],[],[],[562,766],[987,1000],[],[929,929],[],[],[926,931],[913,975],[],[930,962],[707,914],[688,757],[],[430,433],[452,683],[794,919],[799,991],[],[],[],[658,731],[],[328,686],[998,999],[],[455,938],[981,988],[],[92,699],[311,690],[916,920],[],[213,339],[605,961],[719,902],[],[],[],[129,833],[],[844,926],[940,956],[148,182],[],[163,885],[],[],[],[532,886],[],[],[],[306,906],[],[],[948,963],[],[116,853]]
answers = [None,None,None,None,637,637,637,None,None,None,702,None,702,None,702,702,702,702,702,None,None,None,None,906,None,906,None,906,906,None,906,906,None,966,966,966,None,None,None,966,None,None,None,None,977,None,977,977,None,None,None,None,None,977,977,None,None,977,977,977,None,None,None,None,986,None,None,None,986,986,986,986,None,986,986,None,None,986,None,986,986,None,None,986,None,None,None,986,None,None,None,None,986,986,986,None,986,None,None,986,None,None,986,None,None,None,986,None,None,None,986,986,986,None,986,None,None,None,986,None,986,986,986,None,986,986,986,None,986,986,None,986,None]
ci = CountIntervals()
for act, val, ans in zip(actions[1:], values[1:], answers[1:]):
    if act == 'add':
        ci.add(*val)
    else:
        res = ci.count()
        if res != ans:
            print(f'Failed: {res=}, {ans=}')

