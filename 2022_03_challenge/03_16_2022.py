# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """LeetCode 946

        My idea is to simulate the stack operation. We always push first, and
        then check the popped array. If the front of the popped array is equal
        to the top of the stack, we pop the stack and move the pointer forward
        in popped array. Keep doing this until the entire popped array is
        exhausted, at which time we can say the stack sequence is valid. If
        during this process, pushed is exhausted ahead of popped, then the
        sequence is inaccurate.

        O(N) time and O(N) space, 159 ms, 7% ranking.
        """
        stack = [pushed[0]]
        i, j = 1, 0
        N = len(pushed)
        while j < N:
            if stack and popped[j] == stack[-1]:
                stack.pop()
                j += 1
            elif i < N:
                stack.append(pushed[i])
                i += 1
            else:
                return False
        return True


class Solution2:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """Solution from lee215. Similar to the simulation above, but without
        the need to create a new stack.
        """
        i = j = 0  # pointers on the current position in pushed and popped
        for p in pushed:
            pushed[i] = p  # simulate pushing to stack
            while i >= 0 and pushed[i] == popped[j]:  # simulate popping stack
                j += 1
                i -= 1
            i += 1
        return i == 0



sol = Solution2()
tests = [
    ([1,2,3,4,5], [4,5,3,2,1], True),
    ([1,2,3,4,5], [4,3,5,1,2], False),
    ([4,0,1,2,3], [4,2,3,0,1], False),
]

for i, (pushed, popped, ans) in enumerate(tests):
    res = sol.validateStackSequences(pushed, popped)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
