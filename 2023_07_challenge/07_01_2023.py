# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        """LeetCode 2305

        Binary search and backtracking. The size of cookies is a strong hint
        that we need to brute force the combinations for distribution. The min
        max requirement is a strong hint that the solution might involve binary
        search.

        However, there is still one more trick, that is to sort cookies in
        reverse. This is because when we start backtracking with the largest
        bag, we automatically cut out a lot of the branches during backtracking,
        so it can make the search much faster.

        O(N^K * log(S)), where N = len(cookies), S = sum(cookies).
        46 ms, faster than 97.76%
        """

        cookies.sort(reverse=True)
        
        def is_possible(idx: int, children: List[int], limit: int) -> bool:
            if idx == len(cookies):
                return True
            for i, c in enumerate(children):
                if c + cookies[idx] <= limit:
                    children[i] += cookies[idx]
                    if is_possible(idx + 1, children, limit):
                        return True
                    children[i] -= cookies[idx]
            return False

        lo, hi = 0, sum(cookies)
        while lo < hi:
            mid = (lo + hi) // 2
            verdict = is_possible(0, [0] * k, mid)
            if verdict:
                hi = mid
            else:
                lo = mid + 1
        return lo


class Solution2:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        """This is the official solution, where we just brute force it via
        backtracking.

        The important trick is to quit early when there are not enough bags left
        for all the children.

        O(N^K), 405 ms, faster than 58.21%
        """
        children = [0] * k
        self.res = math.inf

        def backtrack(idx: int) -> None:
            if len(cookies) - idx < children.count(0):  # not enough bags left
                return
            if idx == len(cookies):
                self.res = min(self.res, max(children))
            else:
                for i in range(k):
                    children[i] += cookies[idx]
                    if children[i] <= self.res:
                        backtrack(idx + 1)
                    children[i] -= cookies[idx]

        backtrack(0)
        return self.res


sol = Solution1()
tests = [
    ([8,15,10,20,8], 2, 31),
    ([6,1,3,2,2,4,1,2], 3, 7),
    ([64,32,16,8,4,2,1,1000], 8, 1000),
]

for i, (cookies, k, ans) in enumerate(tests):
    res = sol.distributeCookies(cookies, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
