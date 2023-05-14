# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq
from collections import defaultdict


class Solution1:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        """HINT

        The hint works marvelously! Sort the tasks by end time. We start from
        the task with the earliest end time. To maximize parallel work, we want
        to draw a line from the first task's end time through all the other
        tasks. Any task that gets crossed by this line can be paralleled with
        the first task. Then we check the seocnd to the end time of the first
        task and do exactly the same thing. We try to maximize parallelism for
        the first task until the first task is done.

        Then we start from the second task and repeat the same procedure.

        One thing to note is that each second can only be consumed once. Thus
        we use a set to keep track of all the seconds consumed. The final
        solution is the length of the consumed set.

        O(NlogN + N^2 * T), where N = len(tasks), T is the average length of
        each task. 3461 ms, faster than 5.76%
        """
        tasks.sort(key=lambda tup: tup[1])
        consumed = set()
        # print(tasks)
        for i in range(len(tasks)):
            # print(consumed)
            t = tasks[i][1]
            while tasks[i][2]:
                if t not in consumed:
                    consumed.add(t)
                    for j in range(i, len(tasks)):
                        if tasks[j][0] <= t <= tasks[j][1] and tasks[j][2]:
                            tasks[j][2] -= 1
                t -= 1
        return len(consumed)


class Solution2:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        """Ref: https://leetcode.com/problems/minimum-time-to-complete-all-tasks/discuss/3286244/Number-Line

        I think this is exactly the same idea as Solution1, but seems to have
        a better implementation.

        1010 ms, faster than 69.05%
        """
        consumed = [0] * 2001
        tasks.sort(key=lambda tup: tup[1])
        for s, e, d in tasks:
            # check if any time points have been consumed. If so, we can deduct
            # from the current task's duration, because when that time point has
            # been consumed previously, the current task could have been done
            # in parallel as well.
            for i in range(s, e + 1):
                if not d:
                    break
                d -= consumed[i]
            t = e
            while d:
                if not consumed[t]:
                    consumed[t] = 1
                    d -= 1
                t -= 1
        return sum(consumed)


sol = Solution2()
tests = [
    ([[2,3,1],[4,5,1],[1,5,2]], 2),
    ([[1,3,2],[2,5,3],[5,6,2]], 4),
    ([[2,8,2],[4,20,7],[8,20,2]], 7),
    ([[10,16,3],[10,20,5],[1,12,4],[8,11,2]], 6),
]

for i, (tasks, ans) in enumerate(tests):
    res = sol.findMinimumTime(tasks)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
