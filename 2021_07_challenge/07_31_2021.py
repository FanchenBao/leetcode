# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def trap(self, height: List[int]) -> int:
        """LeetCode 42

        This is the third time I have solved this problem. It's one of the
        nightmares for me and I am glad that we figured it out. We use a
        monotonic stack. We keep the heights in the stack in decreasing order.
        If a new height is smaller than the top of the stack, we push both its
        height and index in. Else, we need to pop the stack. But each time we
        pop, we need to compute the amount of water that can be held above
        stack[-1] between stack[-2] and the current height. This depends on the
        height difference between stack[-1] and the smaller of stack[-2] and
        the current height. Once we obtain the height difference, we can compute
        the amount of water by multiplying the height difference and the
        distance between stack[-2] and the current height using their indices.

        O(N), 56 ms, 62% ranking.
        """
        stack, res = [], 0
        for i, h in enumerate(height):
            while stack and stack[-1][1] < h:
                if len(stack) == 1:
                    stack.pop()
                else:
                    diff = min(stack[-2][1], h) - stack.pop()[1]
                    res += diff * (i - stack[-1][0] - 1)
            stack.append((i, h))
        return res


class Solution2:
    def trap(self, height: List[int]) -> int:
        """The two pointers solution from the offical solution.
        https://leetcode.com/problems/trapping-rain-water/discuss/?currentPage=1&orderBy=hot&query=

        The idea is that given any height, we want to compute how much water
        can be held above the current height. This is determined by the smaller
        of the max height to the left of the current height and the max height
        to the right of the current height. If we use two pointers, one at the
        start and the other at the end. If height[lo] < height[hi], that means
        for the current height in consideration, we must use the left max for
        computation of the amount of water held above the current height.
        Otherwise, we use the right max. So basically, we switch between the
        left and right pointers to compute the amount of water held above each
        height, until the two pointers meet in the middle.
        """
        lo, hi = 0, len(height) - 1
        lmax, rmax = 0, 0
        res = 0
        while lo < hi:
            if height[lo] < height[hi]:
                lmax = max(height[lo], lmax)
                res += lmax - height[lo]
                lo += 1
            else:
                rmax = max(height[hi], rmax)
                res += rmax - height[hi]
                hi -= 1
        return res


sol = Solution2()
tests = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
]

for i, (height, ans) in enumerate(tests):
    res = sol.trap(height)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
