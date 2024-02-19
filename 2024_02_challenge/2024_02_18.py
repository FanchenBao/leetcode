# from pudb import set_trace; set_trace()
from typing import List, Sequence, Tuple
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
        end_times: List[Tuple[int, int]] = []  # record the (end times, room number)
        unoccupied = list(range(n))  # record the room numbers of the unoccupied rooms
        count = [0] * n
        meetings.sort()
        # keep track of the previous start time
        # Notice that we are manipulating the start time in the loop below. It
        # might happen that the manipulated current start time is bigger than
        # the next start time. To avoid that from happening, we use pre_st to
        # keep track of the start time
        pre_st = 0
        for st, ed in meetings:
            diff = ed - st
            st = max(pre_st, st)
            ed = st + diff
            if end_times and end_times[0][0] > st and len(end_times) == n:
                # the current start is smaller than the smallest end of all
                # the ongoing meetings AND all the rooms are occupied
                st, ed = end_times[0][0], end_times[0][0] + diff
            while end_times and end_times[0][0] <= st:
                _, popped_ri = heapq.heappop(end_times)
                heapq.heappush(unoccupied, popped_ri)
            ri = heapq.heappop(unoccupied)
            heapq.heappush(end_times, (ed, ri))
            count[ri] += 1
            pre_st = st
        max_count = 0
        res = -1
        for i in range(n):
            if count[i] > max_count:
                max_count = count[i]
                res = i
        return res


sol = Solution()
tests = [
    (
        4,
        [
            [48, 49],
            [22, 30],
            [13, 31],
            [31, 46],
            [37, 46],
            [32, 36],
            [25, 36],
            [49, 50],
            [24, 34],
            [6, 41],
        ],
        0,
    ),
    (
        2,
        [[16, 22], [14, 15], [17, 19], [10, 17], [12, 21], [6, 15], [20, 27], [7, 15]],
        0,
    ),
    (
        3,
        [
            [5, 10],
            [15, 16],
            [17, 19],
            [11, 17],
            [14, 18],
            [7, 10],
            [4, 13],
            [8, 15],
            [2, 11],
        ],
        2,
    ),
]

for i, (n, meetings, ans) in enumerate(tests):
    res = sol.mostBooked(n, meetings)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")


# from random import randint, sample
#
# num_test_cases = 100
# all_starts = list(range(1, 21))
#
# for _ in range(num_test_cases):
#     n = randint(1, 5)
#     starts = sample(all_starts, randint(1, 10))
#     meetings = [[st, st + randint(1, 10)] for st in starts]
#     print(n)
#     print(meetings)
