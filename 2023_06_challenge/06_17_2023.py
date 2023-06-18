# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math
from collections import Counter
from bisect import bisect_right
from functools import lru_cache


class Solution1:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """TLE
        """
        c2 = Counter(arr2)
        N = len(arr1)
        self.res = math.inf

        def helper(idx: int, ops: int) -> None:
            if idx >= N:
                self.res = min(self.res, ops)
                return
            # Do not swap
            if idx == 0 or arr1[idx] > arr1[idx - 1]:
                helper(idx + 1, ops)
            # Find the best option in arr2 to swap
            arr2_uniqs = sorted(c2)
            j = -1
            if idx == 0 and arr2_uniqs[0] < arr1[idx]:
                j = 0
            elif idx > 0:
                tmp = bisect_right(arr2_uniqs, arr1[idx - 1])
                if tmp < len(arr2_uniqs) and (arr1[idx] <= arr1[idx - 1] or arr2_uniqs[tmp] < arr1[idx]):
                    j = tmp
            
            if j >= 0:
                original = arr1[idx]
                arr1[idx] = arr2_uniqs[j]
                c2[arr2_uniqs[j]] -= 1
                if not c2[arr2_uniqs[j]]:
                    del c2[arr2_uniqs[j]]
                helper(idx + 1, ops + 1)
                # backtrack
                arr1[idx] = original
                c2[arr2_uniqs[j]] += 1

        helper(0, 0)
        return self.res if self.res < math.inf else -1


class Solution2:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """LeetCode 1187

        The general idea in solution1 is correct, but we used the wrong state
        for dp (technically speaking, I was not doing dp in solution1 but
        backtracking). The correct state is the current index of arr1 and the
        previous value in arr1.

        At each index of arr1, we have two choices. Either swap with the smallest
        value in arr2 that still satisfies arr1 being increasing. Or do not swap
        which can only happen if the current arr1 index value is larger than
        the previous one.

        O(N(M + N)log(M)), 881 ms, faster than 50.77%
        """
        arr2 = sorted(set(arr2))

        @lru_cache(maxsize=None)
        def helper(i: int, prev: int) -> int:
            if i >= len(arr1):
                return 0
            # option 1, always swap
            j = bisect_right(arr2, prev)
            if j < len(arr2):
                op1 = 1 + helper(i + 1, arr2[j])
            else:
                op1 = math.inf
            # option2, do not swap, but this only applies when arr1[i] > prev
            if arr1[i] > prev:
                op2 = helper(i + 1, arr1[i])
            else:
                op2 = math.inf
            return min(op1, op2)

        res = helper(0, -1)
        return res if res < math.inf else -1



sol = Solution2()
tests = [
    ([1,5,3,6,7], [1,3,2,4], 1),
    ([1,5,3,6,7], [4,3,1], 2),
    ([1,5,3,6,7], [1,6,3,3], -1),
    ([5,16,19,2,1,12,7,14,5,16], [6,17,4,3,6,13,4,3,18,17,16,7,14,1,16], 8),
]

for i, (arr1, arr2, ans) in enumerate(tests):
    res = sol.makeArrayIncreasing(arr1, arr2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
