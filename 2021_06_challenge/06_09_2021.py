# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter, deque
import heapq


class Solution1:
    def maxResult(self, nums: List[int], k: int) -> int:
        """LeetCode 1696

        The DP idea is fairly straightforward. In fact it is exactly the same
        as the one we handled on the past Monday. The tricky part is that k is
        also a variable, which means if we iterate through all k values in the
        DP table for each new n, the runtime would be O(NK). This will time out
        given the size of N and K. Therefore, the problem to solve is how to
        acquire the max value in a sliding window of size k in less than linear
        time.

        My solution is to use a heap, which tracks the max value in logarithm
        time. The trick is to prune the heap when the heap size grows larger
        than the allowed k. Since we can only prune the max value in the heap,
        we need to also record the indices of each value pushed into the heap.
        Once the heap size is larger than k, AND the top of the heap has index
        outside the current sliding window range, we pop it. This way, it is
        guaranteed that each value in the heap is only popped once.

        O(Nlog(K)), 1652 ms, very bad runtime.
        """
        heap = []
        N = len(nums)
        for i in range(N - 1):
            # remove the top of heap if its index suggests that it is no longer
            # in range
            while len(heap) > k and i - heap[0][1] > k:
                heapq.heappop(heap)
            cur = nums[i] + (-heap[0][0] if heap else 0)
            heapq.heappush(heap, (-cur, i))
        # Must prune the heap one more time
        while len(heap) > k and N - 1 - heap[0][1] > k:
            heapq.heappop(heap)
        return nums[-1] + (-heap[0][0] if heap else 0)


class Solution2:
    def maxResult(self, nums: List[int], k: int) -> int:
        """O(N) solution, 1676 ms. Although the runtime seems bad, but this is
        a brilliant solution. While I used a heap to solve the problem of
        maintaining the max value in a sliding window, this solution uses a
        non increasing (monotonic) deque to solve the same problem. The idea is to always
        keep the max value on the left of the deque. This requires that each
        time a new value gets pushed into the deque, we pop out, from the right
        side, all the values that are smaller than the new one. Also, we check
        the left side to see if the index is out of range. If it is, we pop from
        the left.

        The runtime is bad probably because I am using a tuple for the deque.
        Or it could be because LeetCode has increased test cases.
        """
        scores = deque([(nums[0], 0)])
        for i in range(1, len(nums)):
            while i - scores[0][1] > k:
                scores.popleft()
            cur = nums[i] + scores[0][0]
            while scores and scores[-1][0] < cur:
                scores.pop()
            scores.append((cur, i))
        return scores[-1][0]


class Solution3:
    def maxResult(self, nums: List[int], k: int) -> int:
        """Speed up version of solution2

        Courtesy: https://leetcode.com/problems/jump-game-vi/discuss/978462/C%2B%2B-DP-%2B-Monoqueue-O(n)

        1228 ms.
        """
        indices = deque([0])
        scores = [0] * len(nums)
        scores[0] = nums[0]
        for i in range(1, len(nums)):
            while i - indices[0] > k:
                indices.popleft()
            cur = nums[i] + scores[indices[0]]
            while indices and scores[indices[-1]] < cur:
                indices.pop()
            indices.append(i)
            scores[i] = cur
        return scores[-1]


sol = Solution3()
tests = [
    ([1, -1, -2, 4, -7, 3], 2, 7),
    ([10, -5, -2, 4, 0, 3], 3, 17),
    ([1, -5, -20, 4, -1, 3, -6, -3], 2, 0),
    ([1], 1, 1),
    ([100, -1, -100, -1, 100], 2, 198),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.maxResult(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
