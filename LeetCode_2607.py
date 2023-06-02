# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict
from itertools import accumulate


class DSU:
    def __init__(self, N: int) -> None:
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rnk[px] > self.rnk[py]:
                self.par[py] = px
            elif self.rnk[px] < self.rnk[py]:
                self.par[px] = py
            else:
                self.par[py] = px
                self.rnk[px] += 1
            return True
        return False


class Solution1:
    def find_min_op_to_make_all_ele_equal(self, arr: List[int]) -> int:
        arr.sort()
        presum = list(accumulate(arr))
        res = math.inf
        N = len(arr)
        for i, a in enumerate(arr):
            left = 0 if i == 0 else a * i - presum[i - 1]
            right = 0 if i == N - 1 else presum[-1] - presum[i] - a * (N - i - 1)
            res = min(res, left + right)
        return res

    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        """The solution feels a bit overkill. We first use union find to locate
        which elements in arr must be equal. Then we find the optimal value that
        these elements must be equate to such that the total operations are
        minimal.

        O(N * O(union-find)), 2027 ms, faster than 5.11%
        """
        N = len(arr)
        dsu = DSU(N)
        for i in range(N):
            dsu.union(i, (k + i) % N)
        groups = defaultdict(list)
        for i in range(N):
            groups[dsu.find(i)].append(arr[i])
        return sum(self.find_min_op_to_make_all_ele_equal(g) for g in groups.values())


class Solution2:
    def find_min_op_to_make_all_ele_equal(self, arr: List[int]) -> int:
        arr.sort()
        median = arr[len(arr) // 2]
        return sum(abs(a - median) for a in arr)

    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        """Still union-find, but use median to quickly find the min operations
        to turn an array of values into the same value

        1735 ms, faster than 6.30%
        """
        N = len(arr)
        dsu = DSU(N)
        for i in range(N):
            dsu.union(i, (k + i) % N)
        groups = defaultdict(list)
        for i in range(N):
            groups[dsu.find(i)].append(arr[i])
        return sum(self.find_min_op_to_make_all_ele_equal(g) for g in groups.values())


class Solution3:
    def find_min_op_to_make_all_ele_equal(self, arr: List[int]) -> int:
        arr.sort()
        median = arr[len(arr) // 2]
        return sum(abs(a - median) for a in arr)

    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        """Not using Union-Find. Just find all i, (i + k) % N, (i + 2k) % N, ...

        1039 ms, faster than 36.77%
        """
        N = len(arr)
        res = 0
        for i in range(N):
            equals = []
            j = i
            while arr[j] > 0:
                equals.append(arr[j])
                arr[j] = 0
                j = (j + k) % N
            if equals:
                res += self.find_min_op_to_make_all_ele_equal(equals)
        return res


sol = Solution3()
tests = [
    ([1,4,1,3], 2, 1),
    ([2,5,5,7], 3, 5),
    ([2,4,2,10,3], 1, 10),
]

for i, (arr, k, ans) in enumerate(tests):
    res = sol.makeSubKSumEqual(arr, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
