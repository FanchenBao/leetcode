# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """Very interesting problem. The breakthrough was the realization that
        we should go from (tx, ty) backwards. This is because from (tx, ty),
        there is always only one way to go, either to (tx - ty, ty) or
        (tx, ty - tx), depending on whether tx > ty or ty < tx, respectively.
        Note that if tx == ty, it is mostly likely a deadend unless it happens
        at the very beginning and sx == tx == sy == ty.

        The difficulty is to realize that we should not just to tx -= ty or
        ty -= tx at each step, because that is super slow. We should use mod
        to remove as many ty from tx (or tx from ty). However, we also must not
        remove too much such that we miss (sx, sy). Thus, my strategy is to
        remove as many as possibe, then replenish the smallest amount to tx or
        ty, such that the new tx or ty is larger than sx or sy. Of course,
        there are a few small errors during implementation, but they can be
        fixed rather easily.

        59 ms, faster than 19.00% 
        """
        while tx >= 0 and ty >= 0:
            if sx == tx and sy == ty:
                return True
            if tx == ty:
                break
            if tx > ty:
                tmp = tx % ty + (sx // ty + 1) * ty
                if tmp >= tx:
                    tx -= ty
                else:
                    tx = tmp
            else:
                tmp = ty % tx + (sy // tx + 1) * tx
                if tmp >= ty:
                    ty -= tx
                else:
                    ty = tmp
        return False


class Solution2:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """Inspired by lee215's solution

        https://leetcode.com/problems/reaching-points/discuss/114856/JavaC%2B%2BPython-Modulo-from-the-End

        A very neat trick is that if a < b, a % b == a. Thus, we don't have to
        compare tx and ty before modding.

        Another important observation is that if throughout the tx % ty
        oberation, the remainder is smaller than sx, then it is impossible to
        end up at sx, because we will overshoot no matter what.

        Once the while loop exists, we must have sx == tx and sy <= ty or
        sy == ty and sx <= tx for it to work. In either case, we can either
        move vertically down tx at a time, or horizontally left ty at a time.
        Hence, we must check (ty - sy) % tx or (tx - sx) % ty

        O(log(max(tx, ty))), 32 ms, faster than 93.35% 
        """
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx
        return sx == tx and sy <= ty and (ty - sy) % tx == 0 or \
            sy == ty and sx <= tx and (tx - sx) % ty == 0


sol = Solution2()
tests = [
    (1, 1, 3, 5, True),
    (1, 1, 2, 2, False),
    (1, 1, 1, 1, True),
    (1, 1, 1000000000, 1, True),
    (9, 5, 12, 8, False),
]

for i, (sx, sy, tx, ty, ans) in enumerate(tests):
    res = sol.reachingPoints(sx, sy, tx, ty)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
