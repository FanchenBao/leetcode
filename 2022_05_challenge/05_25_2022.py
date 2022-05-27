# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
from bisect import bisect_left


class Solution1:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """TLE
        """
        hw = defaultdict(list)
        for w, h in envelopes:
            hw[w].append(h)
        for hs in hw.values():
            hs.sort()
        ws = sorted(hw)
        dp = {}
        for i, w in enumerate(ws):
            for h in hw[w]:
                dp[(w, h)] = 1
                for ii in range(i - 1, -1, -1):
                    idx = bisect_left(hw[ws[ii]], h)
                    if idx > 0:
                        dp[(w, h)] = max(dp[(w, h)], 1 + dp[(ws[ii], hw[ws[ii]][idx - 1])])
        return max(dp.values())


class Solution2:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        LeetCode 354

        This is a tough one. I cannot resolve it without TLE. The intuition
        is to sort envelopes with width ascending and height descending per each
        width. Now the problem is converted to: take one height per width,
        what is the longest increasing height arrangement we can find. This is
        equivalent to finding the longest increasing subsequence in the
        descending sorted heights.

        The algo to find the longest increasing subsequence is very smart. We
        maintain a monotonic increasing stack. Each time a new height is larger
        then the largest in the stack, we append it for sure. Otherwise, we
        find the index of the height in the stack that is the smallest that is
        larger than the current height, and we replace that value with the
        current height. What we are doing is to ensure that the monotonic stack
        increase as slowly as possible. This is not to say that our final
        solution would include the newly added smaller heights, but the total
        number of heights in the stack is correct. All we are doing is to
        provide a better chance for future extension while not modifying the
        number of values on the stack at the moment.

        O(NlogN), 1574 ms, faster than 55.93%
        """
        envelopes.sort(key=lambda tup: (tup[0], -tup[1]))
        stack = [-1]
        for _, h in envelopes:
            idx = bisect_left(stack, h)
            if idx == len(stack):
                stack.append(h)
            elif stack[idx] > h:
                stack[idx] = h  # make stack increase slower to increase chance of extending the stack
        return len(stack) - 1


sol = Solution2()
tests = [
    ([[5,4],[6,4],[6,7],[2,3]], 3),
    ([[1,1],[1,1],[1,1]], 1),
]

for i, (envelopes, ans) in enumerate(tests):
    res = sol.maxEnvelopes(envelopes)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
