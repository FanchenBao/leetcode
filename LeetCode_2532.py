# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math
import heapq


class Solution:
    def left_to_right(self, lh, rh, time) -> Tuple[int, int]:
        cur = heapq.heappop(lh)
        cur[0] += time[-cur[2]][1]
        heapq.heappush(rh, cur)
        return time[-cur[2]][0], cur

    def right_to_left(self, lh, rh, time) -> Tuple[int, int]:
        cur = heapq.heappop(rh)
        cur[0] += time[-cur[2]][3]
        heapq.heappush(lh, cur)
        return time[-cur[2]][2], cur

    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        lh = [[0, -time[i][0] - time[i][2], -i] for i in range(k)]
        heapq.heapify(lh)
        rh = []
        cross_time = 0
        print(lh, rh)
        while n:
            if (lh and not rh) or (lh and rh and lh[0][0] < rh[0][0]):
                cur_cross_time, cur = self.left_to_right(lh, rh, time)
                n -= 1
            else:
                cur_cross_time, cur = self.right_to_left(lh, rh, time)
            cross_time += cur_cross_time
            print('left', lh)
            print('right', rh)
            print(cross_time, cur)
            print()
        cur_cross_time, cur = self.right_to_left(lh, rh, time)
        cross_time += cur_cross_time
        print('left', lh)
        print('right', rh)
        print(cross_time, cur)
        return cur[0] - time[-cur[2]][3] + cross_time


sol = Solution()
tests = [
    # (1, 3, [[1,1,2,1],[1,1,3,1],[1,1,4,1]], 6),
    # (3, 2, [[1,9,1,8],[10,10,10,10]], 50),
    (10, 6, [[2,10,5,8],[3,5,2,2],[5,8,10,10],[7,8,8,5],[5,6,6,10],[6,10,6,2]], 149),
]

for i, (n, k, time, ans) in enumerate(tests):
    res = sol.findCrossingTime(n, k, time)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
