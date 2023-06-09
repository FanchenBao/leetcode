# from pudb import set_trace; set_trace()
from typing import List
import math
from sortedcontainers import SortedList


class Solution1:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        """TLE
        """
        res = [-1] * n
        res[p] = 0
        queue = [p]
        steps = 0
        banned_set = set(banned)
        while queue:
            tmp = []
            for i in queue:
                lo = max(0, i - k + 1)
                while lo <= i and lo + k - 1 < n:
                    j = lo + k - 1 - (i - lo)
                    if res[j] == -1 and j not in banned_set:
                        res[j] = steps + 1
                        tmp.append(j)
                    lo += 1
            steps += 1
            queue = tmp
        return res


class Solution2:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        """Very tough problem to make it faster. The following solution is
        inspired by https://leetcode.com/problems/minimum-reverse-operations/discuss/3369888/C%2B%2B-or-100-or-Understandable-(very-detailed)

        The basic idea is still BFS, but instead of looping through the k-sized
        window for each element, we loop through the remaining unbanned
        positions that can be reached by the current node. And since for each
        node, the reachable positions must all be even-indexed or odd-indexed,
        we place the unbanned positions in two sets. Each time a position is
        taken, we remove it from the set.

        Another very important trick is to find the index of the begin and end
        of the reachable positions from the current node. The trick is that if
        there are not enough positions to the left or right to extend a window,
        we can wrap back via absolute value to obtain the real begin and end.

        Unfortunately, this one still TLE, because using a set is still not the
        best option.
        """
        res = [-1] * n
        res[p] = 0
        unbanned = [set(), set()]
        banned_set = set(banned)
        for i in range(n):
            if i != p and i not in banned_set:
                unbanned[i % 2].add(i)
        queue = [p]
        steps = 0
        while queue:
            tmp = []
            for i in queue:
                lo = abs(i - (k - 1))  # the left-most position that can be reached
                hi = n - 1 - abs((n - 1 - i) - (k - 1))  # the right-most position that can be reached
                # instead of traversing the entire window of size k, we go
                # through whatever unbanned set we have at the moment. If the
                # node in the unbanned set is within our range lo to hi, we can
                # include it in the next round. And we also delete it to reduce
                # the size of the unbanned set. This way, we can go through each
                # node only once.
                for j in sorted(unbanned[lo % 2]):
                    if lo <= j <= hi:
                        res[j] = steps + 1
                        tmp.append(j)
                        unbanned[lo % 2].remove(j)
                    elif j > hi:
                        break
            steps += 1
            queue = tmp
        return res


class Solution3:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        """Using SortedList to quickly pick out all the unbanned values from
        lo to hi. If we want to do this from scratch, we need to implement a
        self-balanced binary tree. Yet, SortedList is a short cut

        O(NlogN), 2737 ms, faster than 67.57%
        """
        res = [-1] * n
        res[p] = 0
        unbanned = [SortedList(), SortedList()]
        banned_set = set(banned)
        for i in range(n):
            if i != p and i not in banned_set:
                unbanned[i % 2].add(i)
        queue = [p]
        steps = 0
        while queue:
            tmp = []
            for i in queue:
                lo = abs(i - (k - 1))  # the left-most position that can be reached
                hi = n - 1 - abs((n - 1 - i) - (k - 1))  # the right-most position that can be reached
                # instead of traversing the entire window of size k, we go
                # through whatever unbanned set we have at the moment. If the
                # node in the unbanned set is within our range lo to hi, we can
                # include it in the next round. And we also delete it to reduce
                # the size of the unbanned set. This way, we can go through each
                # node only once.
                for j in list(unbanned[lo % 2].irange(lo, hi)):
                    res[j] = steps + 1
                    tmp.append(j)
                    unbanned[lo % 2].remove(j)
            steps += 1
            queue = tmp
        return res
        



sol = Solution3()
tests = [
    (4, 0, [1,2], 4, [0,-1,-1,1]),
    (5, 0, [2,4], 3, [0,-1,-1,-1,-1]),
    (4, 2, [0,1,3], 1, [-1,-1,0,-1]),
    (3, 0, [], 1, [0, -1, -1]),
    (5, 2, [4], 5, [-1, -1, 0, -1, -1]),
    (6, 5, [2, 0, 4], 5, [-1, 1, -1, 2, -1, 0]),
    (9, 4, [8,3,7], 7, [2,-1,1,-1,0,-1,1,-1,-1]),
]

for i, (n, p, banned, k, ans) in enumerate(tests):
    res = sol.minReverseOperations(n, p, banned, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
