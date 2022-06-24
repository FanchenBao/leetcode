# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        """LeetCode 1354

        The concept of going from target back to the beginning is not hard. But
        the trickiness of edge cases is quite challenging. Also, there is a
        trick where we can massively reduce the largest value by division,
        instead of iteration, because if a currently largest value remains the
        largest after it is replaced by its replacement, we can continue the
        same operation on the replacement until it drops below the largest in
        the remaning. This is the key to avoid TLE in edge case [1, 1000000000]

        O(NlogN), 532 ms, faster than 18.82% 
        """
        s, N = sum(target), len(target)
        if N == 1 and s != 1:  # edge case [2]
            return False
        heap = [-t for t in target]
        heapq.heapify(heap)
        while s > N:
            m = -heapq.heappop(heap)
            # remove as much s - m as possible until heap[0] becomes the
            # largest value. Otherwise, the value popped out initially remains
            # the largest value.
            k, r = divmod(m + heap[0], s - m)
            k += r != 0
            rep = m - k * (s - m)
            if rep <= 0 or k == 0:  # k == 0 checks for edge case [9, 9, 9]
                return False
            heapq.heappush(heap, -rep)
            s += rep - m
        return True

sol = Solution()
tests = [
    ([9,3,5], True),
    ([1, 1, 1, 2], False),
    ([8, 5], True),
    ([1,1000000000], True),
    ([9,9,9], False),
    ([2], False),
    ([1], True),
]

for i, (target, ans) in enumerate(tests):
    res = sol.isPossible(target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
