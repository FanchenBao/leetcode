# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """LeetCode 503

        The same stack solution as in the easier version of this problem. The
        only trick is that we need to run the same algorithm twice to count for
        looping around.

        O(N), 228 ms, 61% ranking.
        """
        stack, N = [], len(nums)
        res = [-1] * N

        def find_next_greater(end_idx: int) -> None:
            for i in range(end_idx + 1):
                while stack and stack[-1][1] < nums[i]:
                    idx, _ = stack.pop()
                    if res[idx] < 0:
                        res[idx] = nums[i]
                stack.append((i, nums[i]))
        
        find_next_greater(N - 1)  # first round
        find_next_greater(N - 2)  # second round
        return res


sol = Solution()
tests = [
    ([1, 2, 1], [2, -1, 2]),
    ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.nextGreaterElements(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
