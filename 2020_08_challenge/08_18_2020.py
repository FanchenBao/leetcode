# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        """This is BFS in disguise"""
        # special case
        if N == 1:
            return list(range(10))
        if K == 0:
            return [int(str(i) * N) for i in range(1, 10)]
        # regular case
        ref = [[] for _ in range(10)]  # build a reference for all digits
        for i in range(10):
            if 0 <= i + K <= 9:
                ref[i].append(i + K)
            if 0 <= i - K <= 9:
                ref[i].append(i - K)
        res = []
        for j in range(1, 10):
            temp = [j]
            for _ in range(N - 1):  # construct the remaining digits using ref
                new_temp = []
                for t in temp:
                    for dig in ref[t % 10]:
                        new_temp.append(t * 10 + dig)
                temp = new_temp
            res += temp
        return res


class Solution2:
    def dfs(self, pre_val, res, N, K):
        if not N:
            res.append(pre_val)
            return
        if pre_val != 0 and 0 <= pre_val % 10 + K <= 9:
            self.dfs(pre_val * 10 + pre_val % 10 + K, res, N - 1, K)
        if K != 0 and 0 <= pre_val % 10 - K <= 9:
            self.dfs(pre_val * 10 + pre_val % 10 - K, res, N - 1, K)

    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        """Traditional DFS"""
        res = []
        for i in range(10):
            temp = []
            self.dfs(i, temp, N - 1, K)
            res += temp
        return res


class Solution3:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        """Traditional BFS"""
        queue = list(range(10))
        while N - 1:
            new_queue = []
            while queue:
                pre_val = queue.pop()
                if pre_val != 0 and 0 <= pre_val % 10 + K <= 9:
                    new_queue.append(pre_val * 10 + pre_val % 10 + K)
                if K != 0 and 0 <= pre_val % 10 - K <= 9:
                    new_queue.append(pre_val * 10 + pre_val % 10 - K)
            queue = new_queue
            N -= 1
        return queue



sol = Solution3()

print(sol.numsSameConsecDiff(3, 3))
