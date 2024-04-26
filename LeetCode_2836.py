# from pudb import set_trace; set_trace()
from typing import List, Deque, Tuple
import math
from collections import defaultdict, deque


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        cycles: List[Tuple[Deque[int], int]] = []  # cycles[i] = (deque, cycle_length)
        N = len(receiver)
        which_cycle = [-1] * N

        def build_cycle(idx: int) -> None:
            cur_cycle: Deque[int] = deque()
            which_idx = {}
            cur = idx
            while receiver[cur] >= 0:
                cur_cycle.append(cur)
                which_idx[cur] = len(cur_cycle) - 1
                nex = receiver[cur]
                receiver[cur] = -1
                cur = nex
            if which_cycle[cur] >= 0:
                for i in range(len(cur_cycle) - 1, -1, -1):
                    cycles[which_cycle[cur]][0].appendleft(cur_cycle[i])
                    which_cycle[cur_cycle[i]] = which_cycle[cur]
            else:
                cycles.append((cur_cycle, len(cur_cycle) - which_idx[cur]))
                for ele in cur_cycle:
                    which_cycle[ele] = len(cycles) - 1

        def compute_max_score(cycle_idx: int) -> int:
            arr, cycle_len = cycles[cycle_idx]
            cycle_st = len(arr) - cycle_len
            s = 0
            if k + 1 <= len(arr):
                for i in range(k + 1):
                    s += arr[i]
                hi = k
            else:
                sum_none_cycle = 0
                for i in range(cycle_st):
                    sum_none_cycle += arr[i]
                sum_cycle = 0
                for i in range(cycle_st, len(arr)):
                    sum_cycle += arr[i]
                q, r = divmod(k + 1 - len(arr) + cycle_len, cycle_len)
                sum_partial = 0
                for i in range(cycle_st, cycle_st + r):
                    sum_partial += arr[i]
                s = sum_none_cycle + sum_cycle * q + sum_partial
                hi = cycle_st + r - 1
            res = s
            for lo in range(1, len(arr)):
                s -= arr[lo - 1]
                hi += 1
                if hi == len(arr):
                    hi = cycle_st
                s += arr[hi]
                res = max(res, s)
            return res

        for i in range(N):
            if receiver[i] >= 0:
                build_cycle(i)
        res = 0
        for i in range(len(cycles)):
            res = max(res, compute_max_score(i))
        return res


sol = Solution()
tests = [
    ([1, 1, 1, 2, 3], 3, 10),
]

for i, (receiver, k, ans) in enumerate(tests):
    res = sol.getMaxFunctionValue(receiver, k)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
