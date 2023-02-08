# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math
import heapq


class Solution:
    def cross(self, wait, cpu, time, tick, is_left_to_right) -> int:
        cur = heapq.heappop(wait)
        i = 0 if is_left_to_right else 2
        tick += time[-cur[2]][i]
        cur[0] = tick + time[-cur[2]][i + 1]
        heapq.heappush(cpu, cur)
        return tick

    def check_cpu(self, cpu, wait, tick) -> None:
        while cpu and cpu[0][0] <= tick:
            cur = heapq.heappop(cpu)
            cur[0] = 0
            heapq.heappush(wait, cur)

    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        """This is basically a CPU scheduler. We have two tasks, one on the left
        and the other on the right. When a task is done, the worker needs to
        wait for his turn to cross the bridge. Thus, we create four heaps.

        l_wait: left wait queue. Workers here have completed their tasks and
        wait for cross.
        l_cpu: left CPU queue. Workers here are actively doing the task
        r_wait: same as l_wait, but for the workers waiting on the right
        r_cpu: same as l_cpu, but for the workers doing the task on the right

        A worker is represented by an array

        [available_time_tick, efficiency, idx]

        available_time_tick is the time tick at which the worker finishes the
        task and is able to join l_wait or r_wait. Note that all the workers in
        the wait queue have available_time_tick equal to 0

        efficiency is the sum of left to right time and right to left time. In
        the implementation, efficiency must be the negative of the sum.

        idx is the index of the worker. In the implementation, idx must be
        negative as well.

        Thus, in the heap, the worker with the smallest available_time_tick,
        i.e., the worker who will finish the earlieset gets to the top. If the
        available_time_tick are the same (e.g. in the wait queue), the worker
        with the larger negative efficiency, i.e., lower efficiency, gets to
        the top. If the efficiency are the same, the worker with the larger
        negative index, gets to the top.

        We also use a variable tick to keep track of the current time.

        The work flow goes like this. First, we need to check if anyone on the
        CPU queue has completed their tasks. The check is to compare the current
        tick with available_time_tick on each worker. If the tick is larger
        than available_time_tick, the worker has completed the task and shall
        join the wait queue. We do this for both l_cpu and r_cpu

        Then, we grab workers from the wait queue. If only l_wait is available,
        as in the case at the beginning, we pop the worker from there and have
        him cross the bridge. The time spent crossing the bridge is the time
        everyone has to wait. We update tick for that. Once the worker is on the
        right side, we compute its available_time_tick as current tick plus the
        time needed for him to complete the task on the right. Then we put him
        in r_cpu.

        If r_wait is available, then regardless of whether l_wait is available,
        we always pop workers from r_wait, and have him cross the bridge from
        right to left. We update tick for the current time, and compute the
        available_time_tick for the worker working on the task on the left. Then
        we put him in l_cpu.

        Last case, if neither l_wait nor r_wait is available, that means the
        current tick is smaller than available_time_tick from the top worker on
        both l_cpu and r_cpu. Then we need to fast forward tick to the smaller
        of the two and then repeat the process.

        One complication is that once all jobs have been picked up, we need to
        terminate the process above. At this point, there are still workers on
        r_cpu, but we don't care about l_cpu or l_wait anymore. We just want to
        get workers from r_cpu to r_wait to crossing the bridge.

        O(NlogK), 731 ms, faster than 35.31%
        """
        l_wait, l_cpu, r_wait, r_cpu = [], [], [], []
        # All workers on l_wait at the beginning
        for i in range(k):
            heapq.heappush(l_wait, [0, -time[i][0] - time[i][2], -i])
        tick = 0
        while n:
            self.check_cpu(l_cpu, l_wait, tick)
            self.check_cpu(r_cpu, r_wait, tick)
            if l_wait and not r_wait:
                tick = self.cross(l_wait, r_cpu, time, tick, True)
                n -= 1
            elif r_wait:
                tick = self.cross(r_wait, l_cpu, time, tick, False)
            else:  # l_wait and r_wait both empty
                tick = min(l_cpu[0][0] if l_cpu else math.inf, r_cpu[0][0] if r_cpu else math.inf)

        # Move all remaining workers from right to left
        while r_cpu or r_wait:
            self.check_cpu(r_cpu, r_wait, tick)
            tick = self.cross(r_wait, l_cpu, time, tick, False) if r_wait else r_cpu[0][0]
        return tick


sol = Solution()
tests = [
    (1, 3, [[1,1,2,1],[1,1,3,1],[1,1,4,1]], 6),
    (3, 2, [[1,9,1,8],[10,10,10,10]], 50),
    (10, 6, [[2,10,5,8],[3,5,2,2],[5,8,10,10],[7,8,8,5],[5,6,6,10],[6,10,6,2]], 149),
    (3, 2, [[3,2,4,1],[4,10,1,3]], 22),
]

for i, (n, k, time, ans) in enumerate(tests):
    res = sol.findCrossingTime(n, k, time)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
