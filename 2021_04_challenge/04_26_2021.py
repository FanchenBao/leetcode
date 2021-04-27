# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution1:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """LeetCode 1642

        TLE
        """
        N = len(heights)
        if N == 1:
            return 0
        options = [[-N + 1, [0, ladders], [0, bricks]]]
        for i in range(N - 2, 0, -1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                temp = []
                while options:
                    bd, (lmin, lmax), (bmin, bmax) = heapq.heappop(options)
                    if lmin < ladders:  # try user ladder
                        heapq.heappush(
                            temp, [bd, [lmin + 1, min(ladders, lmax + 1)], [bmin, bmax]],
                        )
                    if bmin + diff <= bricks:  # try use bricks
                        heapq.heappush(
                            temp, [bd, [lmin, lmax], [bmin + diff, min(bricks, bmax + diff)]],
                        )
                heapq.heappush(temp, [-i, [0, 0], [0, diff - 1]])
                options = temp
                print(i, options)
        # Return the answer from the perspective of the first building
        diff = heights[1] - heights[0]
        while options:
            bd, (lmin, lmax), (bmin, bmax) = heapq.heappop(options)
            if lmin < ladders or bmin + diff <= bricks:
                return -bd
        return 0


class Solution2:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """This is from the Hint. The hint is a bit hard to understand, but it
        does make sense after some thought. As we are moving through buildings,
        we either use ladder or brick. Let's assume that we use only bricks and
        go as far as we can. When we get stuck, we can unstuck ourselves by
        using ladder on one of the climb. The most efficient use of ladder in
        this situation is on the highest climb. Therefore, we keep track of all
        the climbs until we get stuck. And swap the highest climb with the
        ladder and replenish our bricks. We can use a priority queue to keep
        track of the highest climb so far. We continue doing this until we run
        out of ladder or do not have sufficient bricks.

        O(Nlog(N)), 580 ms, 76% ranking.

        This problem can also be solved by always using ladders, and then swap
        with bricks.
        """
        diff = []
        for i in range(len(heights) - 1):
            cur_diff = heights[i + 1] - heights[i]
            if cur_diff > 0:
                heapq.heappush(diff, -cur_diff)
                if cur_diff <= bricks:
                    bricks -= cur_diff
                else:
                    ladders -= 1
                    bricks = bricks - heapq.heappop(diff) - cur_diff
                if ladders < 0 or bricks < 0:  # cannot move to i + 1
                    return i
        return i + 1


sol = Solution2()
tests = [
    ([4, 2, 7, 6, 9, 14, 12], 5, 1, 4),
    ([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2, 7),
    ([14, 3, 19, 3], 17, 0, 3),
    ([1, 2], 0, 0, 0),
]

for i, (heights, bricks, ladders, ans) in enumerate(tests):
    res = sol.furthestBuilding(heights, bricks, ladders)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
