# from pudb import set_trace; set_trace()
from typing import List
from random import randint


class Solution0:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """TLE"""
        res = 0
        for h in heights:
            cur_max, cur = 0, 0
            for h_ in heights:
                if h_ >= h:
                    cur += h
                else:
                    cur_max = max(cur_max, cur)
                    cur = 0
            res = max([res, cur_max, cur])
        return res


class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """This is a hard problem and I have solved it before on 07/05/2019.
        Apparently I have completely forgotten about the solution, so this is
        solved from scratch. The idea is to keep pushing larger heights to a
        stack until we encounter a smaller height. Then we pop the top of the
        stack until the current height is larger than the top. Each time we pop
        a height, we compute the rectangle starting from the popped height until
        the current height using the popped height as the height and the index
        difference between the popped height and current height as the width.
        I call this "look to the right".

        We then repeat the same procedure in reverse order, which I call it look
        to the left.

        We combine the two results to get the max rectangle at each index.

        O(N), 124 ms, 15% ranking.
        """
        n = len(heights)
        totals = [0] * n
        stack = []
        # look to the right
        for i in range(n):
            h = heights[i]
            while stack and stack[-1][1] > h:
                j, cur_h = stack.pop()
                totals[j] += cur_h * (i - j)
            stack.append((i, h))
        while stack:
            j, cur_h = stack.pop()
            totals[j] += cur_h * (n - j)
        # look to the left
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while stack and stack[-1][1] > h:
                j, cur_h = stack.pop()
                totals[j] += (cur_h * (j - i) - cur_h)
            stack.append((i, h))
        while stack:
            j, cur_h = stack.pop()
            totals[j] += (cur_h * (j + 1) - cur_h)
        return max(totals) if totals else 0


class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """The improved one pass version.

        First, we only need to put indices in the stack, because the heights
        can be retrieved easily from indices.

        Second, when a height is popped, the width of the rectangle that can use
        the popped height as height extends from the previous index in the stack
        and the current index encountered. This is because the way the stack is
        maintained guarantees that the indices between consecutive indices in
        the stack point to higher heights. For example, if we have heights:

        0, 6, 2, 4, 3

        We push indices 0, 1 to the stack. When index 2 is encountered, we pop
        1. The rectangle for index 1 is of height 6 and width 2 - 0 - 1 = 1.

        Now we have stack 0, 2, and we know that the indices between 0 and 2
        point to height higher than both. So if index 2 is popped, the left
        edge of the rectangle will be index 0 instead of index 2. Let's keep the
        example going.

        We push index 3. At index 4, we need to pop index 3. The rectangle
        height is 4, width is 4 - 2 - 1.

        We are at the end of heights, so we pop each index in the stack.

        We pop index 4, height is 3, width is 5 - 2 - 1.
        We pop index 2, height is 2, width is 5 - 0 - 1.
        We pop index 0, height is 0, width is 5 - (-1) - 1.

        In practice, we add -1 to the stack as a dummy value, and a negative
        height at the end of heights as another dummy value.

        O(N), 96 ms, 92% ranking.
        """
        stack = [-1]  # only store index. -1 is a dummy value
        heights.append(-1)  # add a min at the end of heights as dummy
        res = 0
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                res = max(res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        return res


sol0 = Solution0()
sol = Solution2()

tests = [
    [randint(0, 10) for _ in range(5)] for _ in range(10)
]

tests += [[], [1]]

for i, heights in enumerate(tests):
    ans = sol0.largestRectangleArea(heights)
    res = sol.largestRectangleArea(heights)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}, heights: {heights}')

# print(sol.largestRectangleArea([10, 4, 4, 10, 9]))
