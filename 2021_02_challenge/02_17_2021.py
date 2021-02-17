# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """LeetCode 11

        Most likely this is the official solution, as I have done this
        problem before. It was a tough one for me back then, and I remembered
        that the solution involved two pointers moving in opposite directions.
        I was able to figure out how the pointers move this time without too
        much trouble.

        Basically, we start from both ends and move the pointer with the smaller
        height towards the center, until a bigger height is encountered. This
        works, because only bigger height is possible to yield a larger area
        compared to the starting state. The slightly tricky part is when both
        pointers are at the same height. In this case, we need to move both
        pointers because the only possibility that a higher area will be found
        is when there are two heights in between that are larger. Thus, we have
        to move both pointers.

        O(N), 172 ms, 62% ranking.
        """
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            left_h, right_h = height[left], height[right]
            res = max(res, (right - left) * min(left_h, right_h))
            if left_h <= right_h:
                while left < len(height) and height[left] <= left_h:
                    left += 1
            if left_h >= right_h:
                while right >= 0 and height[right] <= right_h:
                    right -= 1
        return res


sol = Solution()
tests = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([4, 3, 2, 1, 4], 16),
    ([1, 2, 1], 2),
]

for i, (height, ans) in enumerate(tests):
    res = sol.maxArea(height)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
