# from pudb import set_trace; set_trace()
from typing import List, Deque, Tuple
import math
from collections import defaultdict, deque


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        N = len(receiver)
        cycles = []  # [([a0, a1, a2....], cycle_start_idx), ...]
        which_cycles = [-1] * N
        which_scores = [
            [-1, -1] for _ in range(N)
        ]  # [[k-length array score, the array index of the last element]]
        res = 0

        def compute_cycle_score(cycle: List[int], cycle_start_idx: int) -> None: ...

        def compute_prefix_score(prefix: List[int], cycle_idx: int) -> None: ...

        def find_cycle(idx: int) -> None:
            if receiver[idx] < 0:
                return
            cur = idx
            arr = []
            arr_idx = {}
            while receiver[cur] >= 0:
                nex = receiver[idx]
                receiver[cur] = -1
                arr_idx[cur] = len(arr)
                arr.append(cur)
                cur = nex
            if which_cycles[cur] < 0:
                # new cycle identified
                for a in arr:
                    which_cycles[a] = len(cycles)
                cycles.append((arr, arr_idx[cur]))
                compute_cycle_score(arr, arr_idx[cur])
            else:
                # a cycle prefix is identified
                for a in arr:
                    which_cycles[a] = which_cycles[cur]
                compute_prefix_score(arr, which_cycles[cur])


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
