# from pudb import set_trace; set_trace()
from typing import List
import math


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
        """Separate k is even and k is odd. When k is even, it's hard to reason
        with. Thus, we use BFS still. However, when k is odd, it's relatively
        easier to deal with. So we analyze it.
        """
        res = [-1] * n
        res[p] = 0
        banned_set = set(banned)
        if k % 2 == 0:
            queue = [p]
            steps = 0
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
        # k is odd. We can only set every other position. First go from left to
        # right
        pre = cur = p
        for i in range(pre + 2, n, 2):
            extra = (k - (i - pre + 1 )) // 2
            if extra < 0:
                break
            if pre - extra >= 0 and i + extra < n and i not in banned_set:
                res[i] = res[pre] + 1
                cur = i
            if 0 <= res[cur] < res[pre] or extra == 0:
                pre = cur
        # go from right to left, but we start from the first filled position to
        # the right of p
        post = cur = p
        for i in range(p + 2, n, 2):
            if res[i] > 0:
                post = cur = i
                break
        for i in range(post - 2, -1, -2):
            extra = (k - (post - i + 1)) // 2
            if extra < 0:
                break
            if post + extra < n and i - extra >= 0 and i not in banned_set:
                res[i] = (res[post] + 1) if res[i] < 0 else min(res[i], res[post] + 1)
                cur = i
            print(res)
            print(cur, post, extra)
            if 0 <= res[cur] < res[post] or extra == 0:
                post = cur
        # go from left to right again to fill in the positions to the left of p
        # that cannot be filled earlier
        pre = cur = p
        for i in range(p - 2, -1, -2):
            if res[i] > 0:
                pre = cur = i
                break
        for i in range(pre + 2, p, 2):
            extra = (k - (i - pre + 1 )) // 2
            if extra < 0:
                break
            if pre - extra >= 0 and i + extra < n and i not in banned_set:
                res[i] = (res[pre] + 1) if res[i] < 0 else min(res[i], res[pre] + 1)
                cur = i
            if 0 <= res[cur] < res[pre] or extra == 0:
                pre = cur
        return res



sol = Solution2()
tests = [
    # (4, 0, [1,2], 4, [0,-1,-1,1]),
    # (5, 0, [2,4], 3, [0,-1,-1,-1,-1]),
    # (4, 2, [0,1,3], 1, [-1,-1,0,-1]),
    # (3, 0, [], 1, [0, -1, -1]),
    # (5, 2, [4], 5, [-1, -1, 0, -1, -1]),
    # (6, 5, [2, 0, 4], 5, [-1, 1, -1, 2, -1, 0]),
    (9, 4, [8,3,7], 7, [2,-1,1,-1,0,-1,1,-1,-1]),
]

for i, (n, p, banned, k, ans) in enumerate(tests):
    res = sol.minReverseOperations(n, p, banned, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
