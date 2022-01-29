# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """LeetCode 84

        This is a classic problem. I have solved it two times and got stuck
        on a problem similar to this another couple of times.

        I did remember the method is monotonal stack, but I was not sure until
        I saw monotonal stakc was one of the topics of this problem. This put
        me on the right track. The key idea is that while building a monotonic
        inscreasing array, each time a big value is popped, what can be
        computed is the max rectangle area with the popped element's height
        being the actual height. The width can be approached by finding the
        difference in indices of the values before or after the value being
        popped. The nature of monotonically increasing array is all the
        elements between the current value and its previous value (in the
        stack) have higher value than the current value. The same also holds
        for all the values between the current value and the new value to be
        appended.

        In total, this algo runs in O(N). 828 ms, 62% ranking.
        """
        stack, res = [-1], 0
        for i, h in enumerate(heights + [-1]):
            while stack and stack[-1] != -1 and heights[stack[-1]] > h:
                res = max(res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        return res


sol = Solution()
tests = [
    ([2,1,5,6,2,3], 10),
    ([2,4], 4),
    ([1], 1),
]

for i, (heights, ans) in enumerate(tests):
    res = sol.largestRectangleArea(heights)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
