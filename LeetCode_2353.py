# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq
from collections import defaultdict


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        """This is a typical problem with dynamic heap. I used to have a system
        for dynamic heap, where I keep track of each heap item in a separate
        list or dict. Each time when some value changes, I change it in that
        list or dict, and then call heapify on the actual heap. This works, but
        most of time it is slow.

        The standard method to handle dynamic heap is to keep pushing updated
        items to the heap, but keep a record of the most up-to-date signature of
        the item. Then, when we need to query the heap, we check the signature
        in the heap against the up-to-date signature. If the two do not match,
        the top of heap is outdated and should be popped.

        In this problem, the signature is the rating. The up-to-date signature
        is stored in self.food_map.

        O(logN) for changeRating
        O(N) for highestRated
        2125 ms, faster than 43.59%
        """
        self.food_map = {}
        self.cuisine_heap = defaultdict(list)
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_map[f] = [c, r]
            heapq.heappush(self.cuisine_heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_map[food][1] = newRating
        heapq.heappush(self.cuisine_heap[self.food_map[food][0]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while True:
            neg_rating, food = self.cuisine_heap[cuisine][0]
            if -neg_rating != self.food_map[food][1]:
                heapq.heappop(self.cuisine_heap[cuisine])
            else:
                return food




# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
