# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        """LeetCode 20

        Use stack. Pay attention to the case where the loop all passes, but
        there are elements remaining in stack.

        O(N), 54 ms, 28% ranking.
        """
        stack = []
        paren = {'(': ')', '[': ']', '{': '}'}
        for le in s:
            if le in '([{':
                stack.append(le)
            else:
                if not stack or paren[stack[-1]] != le:
                    return False
                stack.pop()
        return not stack  # if paren is valid, stack must be empty at the end


# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
