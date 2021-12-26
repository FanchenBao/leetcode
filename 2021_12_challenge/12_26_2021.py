# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """LeetCode 973

        I don't know where this problem is going. Maybe it is trying to test
        a specific concept, but for me, it's as straightforward as sorting.

        O(NlogN), 648 ms, 83% ranking.
        """
        return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]


class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Heap solution. Very good. And this shall be the standard for us
        going forward. Anytime if the requirement is to find the k smallest or
        k larget values in a list, we shall use heap.

        O(Nlogk)
        """
        heap = []  # max heap
        for i, (x, y) in enumerate(points):
            dist = x**2 + y**2
            if len(heap) < k:
                heap.heappush(heap, (-dist, i))
            elif -dist < -heap[0][0]:
                heapq.heappushpop(heap, (-dist, i))
        return [points[i] for _, i in heap]


class Solution3:
    def dist(self, point: List[List[int]]) -> int:
        return point[0]**2 + point[1]**2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Technically O(N) solution using quick select. According to the
        official solution, quick select should be the FIRST algo that comes to
        mind when we want to find the first k smallest or biggest values
        without them being sorted.

        O(N)
        """
        left, right = 0, len(points) - 1
        rem = k
        while left < right:
            mid = (left + right) // 2
            pivot_dist = self.dist(points[mid])
            points[left], points[mid] = points[mid], points[left]
            lo, hi = left + 1, right
            while lo < hi:
                if self.dist(points[lo]) < pivot_dist:
                    lo += 1
                else:
                    points[lo], points[hi] = points[hi], points[lo]
                    hi -= 1
            if self.dist(points[lo]) > pivot_dist:
                lo -= 1
            points[left], points[lo] = points[lo], points[left]  # put pivot in place
            if lo - left + 1 == rem:  # include pivot in consideration
                break
            if lo - left + 1 > rem:
                right = lo - 1
            else:
                rem -= (lo - left + 1)
                left = lo + 1
        return points[:k]


sol = Solution3()
tests = [
    ([[1,3],[-2,2]], 1, [[-2,2]]),
    ([[3,3],[5,-1],[-2,4]], 2, [[-2,4],[3,3]]),
    ([[0,1],[1,0]], 2, [[0,1],[1,0]]),
    ([[1,3],[-2,2],[2,-2]], 2, [[-2,2], [2, -2]]),
    ([[32,-20],[34,-34],[34,-31],[-53,52],[-98,-70],[-15,73],[-41,-94],[95,-78],[-42,-7],[-11,-37],[-94,26],[-74,-53],[68,72],[2,-80],[-58,-94],[48,-80],[-57,-35]],10, [[32,-20],[-11,-37],[-42,-7],[34,-31],[34,-34],[-57,-35],[-53,52],[-15,73],[2,-80],[-74,-53]]),
]

for i, (points, k, ans) in enumerate(tests):
    res = sol.kClosest(points, k)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {sorted(ans)}, Res: {sorted(res)}')
