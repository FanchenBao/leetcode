# from pudb import set_trace; set_trace()
from typing import List
import heapq
from collections import defaultdict
import math
import bisect


class Solution1:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        """LeetCode 1383

        TLE, but the logic is sound
        """
        heap = [(-s, e) for s, e in zip(speed, efficiency)]
        heapq.heapify(heap)
        res, curr_e_i, M = 0, 0, len(efficiency)
        efficiency.sort()
        while heap and curr_e_i < M:
            temp = []
            speed_sum = 0
            min_used_e = math.inf
            j = 0
            while j < k:
                if heap:
                    cand_s, cand_e = heapq.heappop(heap)
                    if cand_e >= efficiency[curr_e_i]:
                        speed_sum += -cand_s
                        if cand_e > efficiency[curr_e_i]:
                            temp.append((cand_s, cand_e))
                        min_used_e = min(min_used_e, cand_e)  # leep frog to next efficiency
                        j += 1
                else:
                    break
            res = max(res, min_used_e * speed_sum)
            curr_e_i = bisect.bisect_right(efficiency, min_used_e)
            heap = list(heapq.merge(heap, temp))
        return res % 1000000007


class ListNode:
    def __init__(self, s: int = 0, e: int = 0):
        self.spd = s
        self.eff = e
        self.next = None


class Solution2:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        """Linked list solution. TLE as well.
        """
        dummy = ListNode()
        node = dummy
        for s, e in sorted(((s, e) for s, e in zip(speed, efficiency)), reverse=True):
            node.next = ListNode(s, e)
            node = node.next
        res, curr_e_i, M = 0, 0, len(efficiency)
        efficiency.sort()
        while curr_e_i < M:
            speed_sum = 0
            min_used_e = math.inf
            j = 0
            pre, cur = dummy, dummy.next
            while j < k and cur:
                cand_s, cand_e = cur.spd, cur.eff
                if cand_e >= efficiency[curr_e_i]:
                    speed_sum += cand_s
                    min_used_e = min(min_used_e, cand_e)  # leep frog to next efficiency
                    j += 1
                if cand_e <= efficiency[curr_e_i]:  # remove nodes if eff has been covered already
                    pre.next = cur.next
                else:
                    pre = pre.next
                cur = cur.next
            res = max(res, min_used_e * speed_sum)
            curr_e_i = bisect.bisect_right(efficiency, min_used_e, lo=curr_e_i + 1)
        return res % 1000000007


class Solution3:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        """The official solution:
        https://leetcode.com/problems/maximum-performance-of-a-team/solution/

        The basic concept is exactly the same. We fix the person with the min
        efficiency, and then we find the k people whose efficiency is larger
        than the currently fixed one and also have the max speeds. The difference
        is that the solution uses a very smart way to ensure that we don't have
        to traverse k times for each fixed efficiency. They sort the people by
        efficiency in reverse order. Thus, for each current efficiency, the
        people with higher efficiency are the ones that have been visited before.
        Then we only need to keep a heap of size k on the visited people to
        ensure that those k people have the highest speeds.

        In my implementation, for each fixed efficiency, I have to iterate k
        times to find the k maximum speeds. Although I am already pruning, the
        run time is inevitably O(NK). But with the official solution, since we
        have already traversed all the possible candidates, we only incur log(K)
        for each fixed efficiency, thus reaching O(Nlog(K)) in the traversal.

        The final runtime is O(N(log(N) + log(K))), where the first O(Nlog(N))
        is for the sorting.
        """
        # sort based on the first element
        speed_heap = []
        res, speed_sum = 0, 0
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            if len(speed_heap) == k:
                speed_sum -= heapq.heappop(speed_heap)
            heapq.heappush(speed_heap, s)
            speed_sum += s
            res = max(res, e * speed_sum)
        return res % 1000000007


sol = Solution3()
tests = [
    (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2, 60),
    (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3, 68),
    (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4, 72),
    (6, [1, 1, 1, 1, 1, 1], [100, 1, 1, 1, 1, 1], 6, 100),
    (4, [8, 9, 5, 9], [1, 2, 6, 9], 2, 84),
]

for i, (n, speed, efficiency, k, ans) in enumerate(tests):
    res = sol.maxPerformance(n, speed, efficiency, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
