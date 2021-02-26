# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """LeetCode 946

        Straightforward solution. We use a stack to maintain the current
        stack state based on the pushed list. And check whether the top of the
        stack matches the current value to pop. If the two matches, we increment
        the pointer on popped. Otherwise, we keep pushing. A false return
        happens when the top of the stack does not match the current value to
        pop, and we have exhausted all values to push.

        O(N), 72 ms, 63% ranking.
        """
        i, j = 0, 0
        stack = []
        while j < len(popped):
            if not stack or popped[j] != stack[-1]:
                if i < len(pushed):
                    stack.append(pushed[i])
                    i += 1
                else:
                    return False
            else:
                stack.pop()
                j += 1
        return True


class Solution2:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """This is the official solution. It views the problem from the
        perspective of pushed, instead of popped. From a design point of view,
        this is clearly the better solution, because it's cleaner and shorter.

        O(N), 68 ms, 84% ranking.
        """
        j = 0
        stack = []
        for p in pushed:
            stack.append(p)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)


class Solution3:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """O(1) space. Use pushed as the stack. I have thought about it, but was
        not able to come up with a good scheme for it. This O(1) solution was
        from the post in lee215:

        https://leetcode.com/problems/validate-stack-sequences/discuss/197685/C%2B%2BJavaPython-Simulation-O(1)-Space

        O(N), 64 ms, 94% ranking.
        """
        i = j = 0
        for p in pushed:
            pushed[i] = p
            while i >= 0 and pushed[i] == popped[j]:
                i -= 1
                j += 1
            i += 1
        return i == 0


sol = Solution3()
tests = [
    ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
    ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
    ([1, 2], [1, 2], True),
    ([], [], True),
]

for i, (pushed, popped, ans) in enumerate(tests):
    res = sol.validateStackSequences(pushed, popped)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
