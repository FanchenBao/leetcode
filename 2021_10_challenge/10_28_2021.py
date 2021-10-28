# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """I thought I knew how to do this, given that this is my third try at
        this problem. Unfortunately, although I passed the OJ, the run time was
        abyssmal. The idea is to keep one value, and check the remaining nums
        for a 2sum problem. Lot of time is spend on preventing duplication.

        O(N^2), 7652 ms, 5% ranking.
        """
        counter = Counter(nums)
        res = set()
        N = len(nums)
        for i, n in enumerate(nums):
            target = 0 - n
            counter[n] -= 1
            for j in range(i + 1, N):
                counter[nums[j]] -= 1
                if counter[target - nums[j]] > 0:
                    res.add(tuple(sorted([n, nums[j], target - nums[j]])))
                counter[nums[j]] += 1
        return [list(r) for r in res]


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """I had to check my solution a year ago to obtain the insight. I got
        very close to this solution, but I was stuck at trying to make the
        solution O(NlogN), but in fact the correct solution is still O(N^2), but
        with a much smaller N since we are using uniques.

        Sorting is important, because it allows us to create unique triplets as
        we search for them, i.e. we can create triplets that are already sorted.
        Another benefit of sorting is that we can determine on the min and max
        of a potential triplet, and then as we shrink on the max, we can break
        out whenever the max drops below 0, or the medium value becomes bigger
        than max. This saves a lot of time.

        O(N^2), 1732 ms, 35% ranking.
        """
        counter = Counter(nums)
        res = []
        N = len(counter)
        uniques = sorted(counter)
        for i, n in enumerate(uniques):
            if n > 0:
                break
            for j in range(N - 1, i - 1, -1):
                target = 0 - n - uniques[j]
                if uniques[j] < 0 or target > uniques[j]:
                    break
                counter[n] -= 1
                counter[uniques[j]] -= 1
                if counter[target] > 0 and target >= n:
                    res.append([n, target, uniques[j]])
                counter[n] += 1
                counter[uniques[j]] += 1
        return res


sol = Solution2()
tests = [
    ([-1,0,1,2,-1,-4],[[-1,-1,2],[-1,0,1]]),
    ([], []),
    ([0], []),
    ([0, 0], []),
    ([0, 0, 0], [[0, 0, 0]])
]

for i, (nums, ans) in enumerate(tests):
    res = sol.threeSum(nums)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
