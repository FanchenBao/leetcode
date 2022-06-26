# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_left


class Solution1:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        """The trick is that we always want the carpet to land at the end of
        a set of tiles, because that is the only time when we might be able to
        get to maximum coverage. As the right side of the carpet moves forward
        away from the end of a set of tiles, the total number of coverage
        either decreases or stays the same. As the carpet moves onto a new tile
        the total coverage either increases or stays the same. Thus the max
        happens when the carpet reaches the end of a set of tiles.

        Now the question becomes how to calculate the number of tiles covered,
        when we know the exact position of the carpet. This method uses binary
        search to find where the left of the carpet is, and use prefix sum to
        quickly compute the number of tiles covered. It is slow, because we
        hit 3115 ms, faster than 5.00%. This is O(NlogN)

        This also hints that there should be an O(N) solution.

        UPDATE: we can terminate the search earlier if the res == carpetLen
        2569 ms, faster than 8.14%
        """
        ts = [[-100, 0], [-10, 0]]
        presum = [0, 0]
        res = 0
        for l, r in sorted(tiles):
            if ts[-1][0] == l - 1:
                ts[-1][0] = r
                presum[-1] += r - l + 1
            else:
                ts.append([l, 0])
                ts.append([r, 1])
                presum.append(presum[-1])
                presum.append(presum[-1] + r - l + 1)
        for j in range(3, len(ts), 2):
            lab = ts[j][0] - carpetLen + 1
            i = bisect_left(ts, lab, key=lambda tup: tup[0])
            if ts[i][1] == 1:
                res = max(res, presum[j] - presum[i] + ts[i][0] - lab + 1)
            else:
                res = max(res, presum[j] - presum[i])
            if res == carpetLen:
                break
        return res


class Solution2:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        """This is from the solution:

        https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/discuss/2038534/Sliding-Window

        The idea is similar, but its implementation is quite clean. Solution1
        says we must have the carpet land at the end of a tile set. But it is
        also true that we must land the left of the carpet at the start of a
        tile set. The logic is the same. But the benefit of this way of
        thinking is that the implementation can avoid binary search and the
        expansion of the original array.

        We keep one pointer going through tiles at each step. If the right of
        the carpet hasn't been reached, we keep moving the pointer forward.
        Otherwise, we compute the current length, and jump the carpet forward.

        O(NlogN), but much faster because we don't have to expand on the array.
        1164 ms, faster than 96.20%
        """
        tiles.sort()
        s = res = 0
        i = j = 0  # i points to the tile where the left of the carpet is.
        while i <= j < len(tiles) and res != carpetLen:  # j points to the tile set on the right
            cp_r = tiles[i][0] + carpetLen - 1
            if tiles[j][0] <= cp_r <= tiles[j][1]:
                res = max(res, s + cp_r - tiles[j][0] + 1)
                s -= tiles[i][1] - tiles[i][0] + 1
                i += 1
            elif cp_r < tiles[j][0]:
                s -= tiles[i][1] - tiles[i][0] + 1
                res = max(res, s)
                i += 1
            else:
                s += tiles[j][1] - tiles[j][0] + 1
                res = max(res, s)
                j += 1
        return res



sol = Solution2()
tests = [
    ([[1,5],[10,11],[12,18],[20,25],[30,32]], 10, 9),
    ([[10,11],[1,1]], 2, 2),
    ([[3745,3757],[3663,3681],[3593,3605],[3890,3903],[3529,3539],[3684,3686],[3023,3026],[2551,2569],[3776,3789],[3243,3256],[3477,3497],[2650,2654],[2264,2266],[2582,2599],[2846,2863],[2346,2364],[3839,3842],[3926,3935],[2995,3012],[3152,3167],[4133,4134],[4048,4058],[3719,3730],[2498,2510],[2277,2295],[4117,4128],[3043,3054],[3394,3402],[3921,3924],[3500,3514],[2789,2808],[3291,3294],[2873,2881],[2760,2760],[3349,3362],[2888,2899],[3802,3822],[3540,3542],[3128,3142],[2617,2632],[3979,3994],[2780,2781],[3213,3233],[3099,3113],[3646,3651],[3956,3963],[2674,2691],[3860,3873],[3363,3370],[2727,2737],[2453,2471],[4011,4031],[3566,3577],[2705,2707],[3560,3565],[3454,3456],[3655,3660],[4100,4103],[2382,2382],[4032,4033],[2518,2531],[2739,2749],[3067,3079],[4068,4074],[2297,2312],[2489,2490],[2954,2974],[2400,2418],[3271,3272],[3628,3632],[3372,3377],[2920,2940],[3315,3330],[3417,3435],[4146,4156],[2324,2340],[2426,2435],[2373,2376],[3621,3626],[2826,2832],[3937,3949],[3178,3195],[4081,4082],[4092,4098],[3688,3698]], 1638, 822),
]

for i, (tiles, carpetLen, ans) in enumerate(tests):
    res = sol.maximumWhiteTiles(tiles, carpetLen)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
