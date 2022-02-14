# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """LeetCode 78

        I have done this one two times in the past, and I have a memory of how
        a power set is constructed. So I was able to solve this problem fairly
        fast.

        O(N * 2^N), 37 ms, 64% ranking.
        """
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                res.append(res[i] + [n])
        return res


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Bitmask method from the official solution
        """
        res = []
        N = len(nums)
        for i in range(1 << N):
            res.append([])
            for j, d in enumerate(f'{i:0{N}b}'):
                if d == '1':
                    res[-1].append(nums[j])
        return res


sol = Solution2()
tests = [
    ([1, 2, 3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
    ([0], [[], [0]]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.subsets(nums)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
