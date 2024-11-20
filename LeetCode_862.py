# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq
from collections import deque


class Solution1:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        This is the official solution using Priority Queue. We produce a prefix
        sum. Then for psum[i], we know that if psum[j] can make the subarray
        nums[j + 1:i] sum not smaller than k, psum[j] <= psum[i] - k.

        We can use a min heap to keep track of all the psums. We can check the
        top of the min heap, and if its psum satisfies the requirement, we
        poll it and use it to find the size of the subarray. The important
        trick here is that once an element is polled from the heap, it does
        not come back. This is because if a later psum can also use the already
        polled psum, it is not necessary to consider this situation because
        the subarray thus produced will always be longer than when the polled
        psum is used for the first time.

        O(NlogN), 410 ms, faster than 12.46%
        """
        min_heap = [[0, -1]]
        psum = 0
        MAX = 10**6
        res = MAX
        for i, n in enumerate(nums):
            psum += n
            while min_heap and min_heap[0][0] <= psum - k:
                res = min(res, i - heapq.heappop(min_heap)[1])
            heapq.heappush(min_heap, [psum, i])
        return res if res < MAX else -1


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        We can use a monotonic increasing deque to keep track of all the small
        prefix sums. We can prove that for each current psum, the best previous
        psums must exist in the monotonic increasing deque in its current form.
        This is because if some psum gets popped during the build-up of the
        monotonic increasing deque, and we assume it is the best psum, then
        the new psum that gets it popped will always be better because it has
        a larger index.

        O(N), 203 ms, faster than 52.66%
        """
        mon = deque([[0, -1]])
        psum = 0
        MAX = 10**6
        res = MAX
        for i, n in enumerate(nums):
            psum += n
            while mon and mon[0][0] <= psum - k:
                res = min(res, i - mon.popleft()[1])
            while mon and mon[-1][0] >= psum:
                mon.pop()
            mon.append([psum, i])
        return res if res < MAX else -1


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
