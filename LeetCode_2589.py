# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq
from collections import defaultdict


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        heap = []
        starts = defaultdict(set)
        ends = defaultdict(set)
        task_durs = {}
        for i, (s, e, d) in enumerate(tasks):
            starts[s].add(i)
            ends[e].add(i)
            task_durs[i] = d

        def get_min_task_length(_tasks, s: int) -> int:
            res = math.inf
            for task in _tasks:
                e = tasks[task][1]
                allowed = e - s + 1
                res = min(res, min(task_durs[task], allowed))
            return res

        overlap = set()
        for t in range(1, 2001):
            if t in ends:
                heapq.heappush(
                    heap,
                    (-len(overlap), -get_min_task_length(overlap, t), t, list(overlap)),
                )
                overlap = overlap - ends[t]
            if t in starts:
                overlap = overlap.union(starts[t])
                heapq.heappush(
                    heap,
                    (-len(overlap), -get_min_task_length(overlap, t), t, list(overlap)),
                )

        res = 0
        while task_durs:
            _, _, t, _tasks = heapq.heappop(heap)
            new_tasks = [task for task in _tasks if task in task_durs]
            if not new_tasks:
                continue
            if len(new_tasks) != len(_tasks):
                heapq.heappush(
                    heap,
                    (-len(new_tasks), -get_min_task_length(new_tasks, t), t, new_tasks)
                )
            else:
                d = -get_min_task_length(_tasks, t)
                rem_tasks = []
                for task in list(task_durs.keys()):
                    task_durs[task] -= d
                    if not task_durs[task]:
                        del task_durs[task]
                    else:
                        rem_tasks.append(task)
                res += d
                if rem_tasks:
                    heapq.heappush(
                        heap,
                        (-len(rem_tasks), -get_min_task_length(rem_tasks, t + d), t + d, rem_tasks)
                    )
        return res



sol = Solution()
tests = [
    ([[2,3,1],[4,5,1],[1,5,2]], 2),
    # ([[1,3,2],[2,5,3],[5,6,2]], 4),
]

for i, (tasks, ans) in enumerate(tests):
    res = sol.findMinimumTime(tasks)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
