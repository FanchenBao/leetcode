# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        """
        This is one of the easier hard problems. It is nothing more than a
        stack, which has certain resemblance of the process of constructing
        a monotonic stack.

        We sort the positions from small to large and go from left to right.
        For each robot going right, we immediately push its index to the
        stack. For each robot going left, we check with the top of the stack
        and perform collision logic. As collision happens, we modify healths
        array in place.

        Once we iterate through the entire positions, we will have the updated
        health of each robot. The answer is the healths array WITHOUT the ones
        with 0 health.

        O(NlogN), 1137 ms, faster than 75.71%
        """
        stack = []
        for _, i in sorted((p, i) for i, p in enumerate(positions)):
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and healths[i]:
                    if healths[i] > healths[stack[-1]]:
                        healths[stack.pop()] = 0
                        healths[i] -= 1
                    elif healths[i] == healths[stack[-1]]:
                        healths[stack.pop()] = 0
                        healths[i] = 0
                    else:
                        healths[i] = 0
                        healths[stack[-1]] -= 1
        return [h for h in healths if h > 0]




sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
