# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def findPairs(self, nums: List[int], k: int) -> int:
        """LeetCode 532

        We use counter to handle the part where we search for the partner of
        the current number under consideration. An important trick is to sort
        the numbers, and then go from small to large and only consider n + k
        situation. This is to avoid duplicates, because if n and n + k are a
        pair, there is no need to check n + k - k situation.

        O(NlogN), 81 ms, 70% ranking.
        """
        counter = Counter(nums)
        res = 0
        for n in sorted(counter):
            counter[n] -= 1
            res += bool(counter[n + k])
        return res


class Solution2:
    def findPairs(self, nums: List[int], k: int) -> int:
        """This is the solution from the last time I did this problem. It is
        better than the one I had today. It uses backtracking idea, and does
        not require sorting.

        O(N)
        """
        counter = Counter(nums)
        res = 0
        for n in counter:
            counter[n] -= 1
            res += bool(counter[n + k])
            counter[n] += 1  # finish considering n, return it to norml
        return res

        
sol = Solution2()
tests = [
    ([3,1,4,1,5], 2, 2),
    ([1,2,3,4,5], 1, 4),
    ([1,3,1,5,4], 0, 1),
    ([1,2,4,4,3,3,0,9,2,3], 3, 2),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.findPairs(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
