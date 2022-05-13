# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """LeetCode 47

        This is the naive solution, using a set to identify duplicates.

        291 ms, faster than 23.01%
        """
        
        def permute(idx: int) -> List[List[int]]:
            if idx == len(nums) - 1:
                return [[nums[idx]]]
            return [p[:i] + [nums[idx]] + p[i:] for p in permute(idx + 1) for i in range(len(p) + 1)]

        return [list(sp) for sp in set(tuple(p) for p in permute(0))]


class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """Backtracking. Directly producing unique permutations, because each
        time a number is put down in a permute, the state of the counter of all
        numbers is always unique. Thus, it is not possible to have two identical
        sequences of numbers.

        80 ms, faster than 62.84% 
        """
        counter = Counter(nums)
        N = len(nums)
        res = []

        def backtrack(cur: List[int]) -> None:
            if len(cur) == N:
                res.append(cur[:])
            else:
                for k, v in counter.items():
                    if v:
                        cur.append(k)
                        counter[k] -= 1
                        backtrack(cur)
                        cur.pop()
                        counter[k] += 1

        backtrack([])
        return res


sol = Solution2()
tests = [
    ([1,1,2], [[1,1,2],[1,2,1],[2,1,1]]),
    ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.permuteUnique(nums)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
