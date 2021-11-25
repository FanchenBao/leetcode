# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Create prefix and suffix product lists. This allows us to solve the
        problem in O(N) without using the division operator.

        O(N), 241 ms, 59% ranking.
        """
        pref, suf = [1], [1]
        N = len(nums)
        for i in range(N):
            pref.append(nums[i] * pref[-1])
        for j in range(N - 1, -1, -1):
            suf.append(nums[j] * suf[-1])
        return [pref[k] * suf[N - k - 1] for k in range(N)]


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """O(1) extra space not counting the return value.

        It is the same logic as Solution1, but we perform prefix and suffix
        product along the way and we compute the suffix product from back to
        front such that it resembles a prefix product procedure.

        234 ms, 81% ranking.
        """
        N = len(nums)
        res = [1] * N
        pref = nums[0]
        for i in range(1, N):
            res[i] *= pref
            pref *= nums[i]
        suf = nums[-1]
        for i in range(N - 2, -1, -1):
            res[i] *= suf
            suf *= nums[i]
        return res


sol = Solution2()
tests = [
    ([1,2,3,4], [24,12,8,6]),
    ([-1,1,0,-3,3], [0,0,9,0,0]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.productExceptSelf(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
