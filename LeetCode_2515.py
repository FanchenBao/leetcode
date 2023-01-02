# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        """
        Just go left and right until we encounter target for the first time.
        Choose the smaller steps.

        The only trick is that target might not exist in words.

        O(N), 52 ms, faster than 76.93%
        """
        N = len(words)
        # go right
        sr = 0
        while sr < N and words[(startIndex + sr) % N] != target:
            sr += 1
        if sr == N:
            return -1
        # go left
        sl = 0
        while words[(startIndex - sl + N) % N] != target:
            sl += 1
        return min(sl, sr)


sol = Solution()
tests = [
    (["hello","i","am","leetcode","hello"], "hello", 1, 1),
    (["a","b","leetcode"], "leetcode", 0, 1),
    (["i","eat","leetcode"], "ate", 0, -1),
]

for i, (words, target, startIndex, ans) in enumerate(tests):
    res = sol.closetTarget(words, target, startIndex)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
