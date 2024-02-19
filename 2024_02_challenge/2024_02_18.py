# from pudb import set_trace; set_trace()
from typing import List, Sequence
import math
import heapq
from collections import Counter


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        LeetCode 2402
        
        min heap for the end times and room number to keep track of the room
        that will be empty next.

        min heap for the unoccupied room numbers to keep track of the room that
        will be occupied next.
        """
        end_times = []  # record the (end times, room number)
        unoccupied = list(range(n))  # record the room numbers of the unoccupied rooms
        count = [0] * n
        for st, ed in sorted(meetings):
            if end_times and end_times[0][0] > st and len(end_times) == n:
                # the current start is smaller than the smallest end of all
                # the ongoing meetings AND all the rooms are occupied
                st, ed = end_times[0][0], end_times[0][0] + ed - st
            while end_times and end_times[0][0] <= st and (not unoccupied or unoccupied[0] > end_times[0][1]):
                _, popped_ri = heapq.heappop(end_times)
                heapq.heappush(unoccupied, popped_ri)
            ri = heapq.heappop(unoccupied)
            heapq.heappush(end_times, (ed, ri))
            count[ri] += 1
        max_count = 0
        res = -1
        for i in range(n):
            if count[i] > max_count:
                max_count = count[i]
                res = i
        return res




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
