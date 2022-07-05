# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
import heapq


class Solution1:
    def candy(self, ratings: List[int]) -> int:
        """LeetCode 135

        We always start from the kid with the lowest rating and going to his/her
        left and right. This guarantees that the candies assigned are
        deterministic. We use a min heap to pop up min rating, and update the
        left and right neighbors of the current min rating.

        O(NlogN), 378 ms, faster than 8.13%
        """
        indices = defaultdict(list)
        for i, r in enumerate(ratings):
            indices[r].append(i)
        candies = [1] * len(ratings)
        min_heap = list(indices.keys())
        heapq.heapify(min_heap)
        while min_heap:
            min_r = heapq.heappop(min_heap)
            for i in indices[min_r]:
                # go left
                for j in range(i - 1, -1, -1):
                    if ratings[j] > ratings[j + 1] and candies[j] <= candies[j + 1]:
                        candies[j] = candies[j + 1] + 1
                    else:
                        break
                # go right
                for k in range(i + 1, len(ratings)):
                    if ratings[k] > ratings[k - 1] and candies[k] <= candies[k - 1]:
                        candies[k] = candies[k - 1] + 1
                    else:
                        break
        return sum(candies)


class Solution2:
    def candy(self, ratings: List[int]) -> int:
        """This is from the official solution.

        Go left to right to satisfy the requirements of left neighbors.
        Go right to left to satisfy the requirements of right neighbors.

        O(N), 289 ms, faster than 32.20%
        """
        N = len(ratings)
        candies = [1] * N
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for j in range(N - 2, -1, -1):
            if ratings[j] > ratings[j + 1] and candies[j] <= candies[j + 1]:
                candies[j] = candies[j + 1] + 1
        return sum(candies)


sol = Solution2()
tests = [
    ([1,0,2], 5),
    ([1, 2, 2], 4),
    ([1, 0, 0, 0, 0, 0, 2], 9),
    ([1], 1),
    ([1,3,2,2,1], 7),
    ([0,1,2,3,2,1], 13),
    ([1,6,10,8,7,3,2], 18),
]

for i, (ratings, ans) in enumerate(tests):
    res = sol.candy(ratings)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
