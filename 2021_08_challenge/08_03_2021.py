# from pudb import set_trace; set_trace()
from typing import List, Set, Tuple
from itertools import product, chain
from collections import Counter, combinations


class Solution1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """LeetCode 90

        This is a cheating method. We basically use combinations to get all
        combinations from nums. Then use set to sieve out the duplicates, and
        then add the non-duplicate combinations to the result.

        40 ms, 51% ranking.
        """
        res = [[], nums]
        for size in range(1, len(nums)):
            res += [list(s) for s in set(tuple(sorted(c)) for c in combinations(nums, size))]
        return res


class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """The same idea as Solution1, but we are writing the combination part
        by hand.

        40 ms.
        """
        nums.sort()

        def comb(idx: int) -> Set[Tuple]:
            if idx == len(nums) - 1:
                return {(nums[idx],)}
            remains = comb(idx + 1)
            temp = {(nums[idx], *tup) for tup in remains}
            temp.add((nums[idx],))
            return remains.union(temp)

        return [list(tup) for tup in comb(0)] + [[]]


class Solution3:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """This must be the smart way. I had this solution more than two years
        ago. I think this is also the standard method to obtain combinations of
        an array of ALL sizes.

        36 ms
        """
        counter = Counter(nums)
        res = [[]]
        for k, v in counter.items():
            for i in range(len(res)):
                for j in range(1, v + 1):
                    res.append(res[i] + [k] * j)
        return res


class Solution4:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """One liner. Note the smart use of `chain`. If an empty list is in a
        chain, it will be combined with other lists.

        Reference: https://leetcode.com/problems/subsets-ii/discuss/1380314/Python-Oneliner-with-product-explained
        """
        return [list(chain(*p)) for p in product(*[[[k] * i for i in range(v + 1)] for k, v in Counter(nums).items()])]


class Solution5:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Use bit mask to identify which values in nums need to be included
        for each entry in the final power set.

        O(2^N * N)
        """
        n = len(nums)
        nums.sort()
        res = set()
        for mask in range(1 << n):
            temp = []
            for i in range(n):
                if (1 << i) & mask:  # check if the i-th bit in the mask is 1
                    temp.append(nums[i])
            res.add(tuple(temp))
        return [list(tup) for tup in res]


sol = Solution5()
tests = [
    ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
    ([0], [[], [0]]),
    ([1, 2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.subsetsWithDup(nums)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
