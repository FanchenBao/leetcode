# from pudb import set_trace; set_trace()
from typing import List
import math
from random import randint


class Solution1:
    def trap(self, height: List[int]) -> int:
        """LeetCode 42

        One of the classics. This is the fourth time that I have done it. The
        method is monotonic decreasing array. Once we encounter a height that
        is larger than the top of the stack, we know that the top of the stack
        must be in between some height to its left that is higher and some
        height to its right that is higher, provided that the size of the stack
        is larger or equal to two. Then we can compute the amount of water that
        can be held with the top of the stack being the bottom level. Thus, we
        use the min of the left height and right height, deduct from it the
        top of the stack, and multiply by the distance between the left height
        and right height. We keep doing this until all top of the stack that
        is smaller than the current right height has been popped. Then we
        append the right height. Note that, we don't have to append the actual
        height. We just need to append the index.

        O(N), 162 ms, faster than 77.78%
        """
        stack = [0]
        res = 0
        for i in range(1, len(height)):
            while stack and height[i] > height[stack[-1]]:
                j = stack.pop()
                if stack:
                    res += (min(height[stack[-1]], height[i]) - height[j]) * (i - stack[-1] - 1)
            stack.append(i)
        return res


class Solution2:
    def trap(self, height: List[int]) -> int:
        """Two pointer solution.

        I don't like the solution on 2021-07-31, because it has a hidden
        assumption that height[lo] or height[hi] points to the current max on
        low or high. I like the solution below because it explicitly specifies
        the current max on low or high.

        lo and hi point to the start and end of height. We move towards the
        center. We move lo if lmax <= hmax. Whenever height[lo] < lmax, we are
        certain that we can trap lmax - height[lo] amount of water above
        height[lo]. However, if height[lo] >= lmax, we cannot track water above
        height[lo]. Instead, we update lmax. We do the same thing on hi.

        The only tricky part is that the exit condition is lo <= hi, instead of
        lo < hi

        O(N), 253 ms, faster than 31.53%
        """
        res = 0
        lo, hi = 0, len(height) - 1
        lmax, hmax = height[lo], height[hi]
        while lo <= hi:
            if lmax <= hmax:
                if height[lo] < lmax:
                    res += lmax - height[lo]
                else:
                    lmax = height[lo]
                lo += 1
            else:
                if height[hi] < hmax:
                    res += hmax - height[hi]
                else:
                    hmax = height[hi]
                hi -= 1
        return res


sol0 = Solution1()
sol = Solution2()
tests = [[randint(0, 1000) for _ in range(10)] for _ in range(100)]
# tests = [
#     ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
#     ([4,2,0,3,2,5], 9),
# ]

for i, height in enumerate(tests):
    ans = sol0.trap(height)
    res = sol.trap(height)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}, Test: {height}')
