# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math
import heapq


class Solution:
    def left_to_right(self, l_wait, r_cpu, time, tick) -> Tuple[int, int]:
        cur = heapq.heappop(l_wait)
        tick += time[-cur[2]][0]
        cur[0] = tick + time[-cur[2]][1]
        heapq.heappush(r_cpu, cur)
        return tick, cur

    def right_to_left(self, r_wait, l_cpu, time, tick) -> Tuple[int, int]:
        cur = heapq.heappop(r_wait)
        tick += time[-cur[2]][2]
        cur[0] = tick + time[-cur[2]][3]
        heapq.heappush(l_cpu, cur)
        return tick, cur

    def check_cpu(self, cpu, wait, tick) -> None:
        while cpu and cpu[0][0] <= tick:
            cur = heapq.heappop(cpu)
            cur[0] = 0
            heapq.heappush(wait, cur)

    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        l_wait = [[0, -time[i][0] - time[i][2], -i] for i in range(k)]
        heapq.heapify(l_wait)
        l_cpu = []
        r_wait = []
        r_cpu = []
        tick = 0
        while n:
            self.check_cpu(l_cpu, l_wait, tick)
            self.check_cpu(r_cpu, r_wait, tick)
            if l_wait and not r_wait:
                tick, cur = self.left_to_right(l_wait, r_cpu, time, tick)
                n -= 1
            elif r_wait:
                tick, cur = self.right_to_left(r_wait, l_cpu, time, tick)
            else:  # l_wait and r_wait are both empty
                tick = min(l_cpu[0][0] if l_cpu else math.inf, r_cpu[0][0] if r_cpu else math.inf)
            # print('left wait', l_wait, 'left cpu', l_cpu)
            # print('right wait', r_wait, 'right cpu', r_cpu)
            # print(tick, cur)
            # print()
        while r_cpu or r_wait:
            self.check_cpu(r_cpu, r_wait, tick)
            if r_wait:
                tick, cur = self.right_to_left(r_wait, l_cpu, time, tick)
            else:
                tick = max(tick, r_cpu[0][0])
            # print('right wait', r_wait, 'right cpu', r_cpu)
            # print(tick, cur)
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
