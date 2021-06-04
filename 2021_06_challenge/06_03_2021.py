# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """LeetCode 1465

        The intuition is to find the largest height and the largest width
        in all the cuts, and their product is the solution. Since the given
        horizontalCuts and verticalCuts are prefix sums after they are sorted,
        it is trivial to find the length of each height and width.

        O(Nlog(N) + Mlog(M)), where N, M are lengths of horizontalCuts and
        verticalCuts, respectively.

        412 ms, 5% ranking.
        """

        def find_max(end_val: int, lst: List[int]) -> int:
            lst.sort()
            lst.append(end_val)
            max_val = lst[0]
            for i in range(1, len(lst)):
                max_val = max(max_val, lst[i] - lst[i - 1])
            return max_val

        return find_max(h, horizontalCuts) * find_max(w, verticalCuts) % 1000000007


class Solution2:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """Using zip to speed things up. Same complexity, but runtime shrinks to
        304 ms, 71% ranking.
        """
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        max_h = max(h2 - h1 for h1, h2 in zip(horizontalCuts, horizontalCuts[1:]))
        max_w = max(w2 - w1 for w1, w2 in zip(verticalCuts, verticalCuts[1:]))
        return max(max_h, horizontalCuts[0]) * max(max_w, verticalCuts[0]) % 1000000007


sol = Solution2()
tests = [
    (5, 4, [1, 2, 4], [1, 3], 4),
    (5, 4, [3, 1], [1], 6),
    (5, 4, [3], [3], 9),
]

for i, (h, w, horizontalCuts, verticalCuts, ans) in enumerate(tests):
    res = sol.maxArea(h, w, horizontalCuts, verticalCuts)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
