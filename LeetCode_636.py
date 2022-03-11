# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """This is not difficult, but quite tricky, because the timestamp
        has different meaning depending on whether a job starts or ends. To
        standardize the meaning of timestamp, we can arbitrarily decide that
        timestamp always means the end of an execution. Thus, for all the
        job starts, when we first record it on the stack, we mark its execution
        time already at 1. This trick works because the problem requirement
        specifies that no two job id has the same timestamp, which guarantees
        that any job start definitely will execute for at least one time tick.

        Another trick is to keep track of the execution time of the job at the
        top of the stack whenever a new job start is pushed to it. Also, when
        the job is later terminated, its execution time is NOT the difference
        between the start and end time of the job, but the accumulated
        execution time and the execution time until the job ends.

        O(N), 87 ms, 72% ranking.
        """
        stack = []  # store job id, ending timestamp, and executed time so far
        hashmap = defaultdict(int)
        pre = -1
        for log in logs:
            idx, status, ts = log.split(':')
            ts = int(ts)
            if status == 'start':
                if stack:
                    stack[-1][2] += ts - pre - 1
                stack.append([idx, ts, 1])  # tricky part
            else:
                pidx, pts, exe_t = stack.pop()
                hashmap[pidx] += exe_t + ts - pre
            pre = ts
        res = [0] * n
        for k, v in hashmap.items():
            res[int(k)] = v
        return res


sol = Solution()
tests = [
    (2, ["0:start:0","1:start:2","1:end:5","0:end:6"], [3, 4]),
    (1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"], [8]),
    (2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"], [7, 1]),
    (2, ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"], [8, 1]),
]

for i, (n, logs, ans) in enumerate(tests):
    res = sol.exclusiveTime(n, logs)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
