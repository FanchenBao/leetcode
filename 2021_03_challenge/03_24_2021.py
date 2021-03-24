# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        """LeetCode 870

        Use greedy-ish solution. We sort both A and B. For B, we go from
        largested to smallest. For each value in B, we look in A for the current
        largest value. If the current largest A is bigger than the current
        largest B, we have a match. We use that large A value immediately.
        Otherwise, we do not have a match, in which case we pair B with the
        smallest in A to maximally extend the probablity that some other A can
        match to some B.

        O(Nlog(N)), 348 ms, 83% ranking.
        """
        res = [-1] * len(A)
        B_ = sorted(((b, i) for i, b in enumerate(B)), reverse=True)
        A_ = sorted(A)
        left, right = 0, len(A) - 1
        for b, i in B_:
            if A_[right] > b:
                res[i] = A_[right]
                right -= 1
            else:
                res[i] = A_[left]
                left += 1
        return res


sol = Solution()
tests = [
    ([2, 7, 11, 15], [1, 10, 4, 11], [2, 11, 7, 15]),
    ([12, 24, 8, 32], [13, 25, 32, 11], [24, 32, 8, 12]),
]

for i, (A, B, ans) in enumerate(tests):
    res = sol.advantageCount(A, B)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
