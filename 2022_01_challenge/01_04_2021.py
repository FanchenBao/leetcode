# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def bitwiseComplement(self, n: int) -> int:
        mask = (1 << (len(bin(n)) - 2)) - 1
        return n ^ mask


class Solution2:
    def bitwiseComplement(self, n: int) -> int:
        """LeetCode 1009

        We know that ~n produces the complement of n, i.e. each bit in n is
        XOR with 1. However, the result of ~n is interpreted as a two's
        complement value. Thus, ~n itself is not the solution. Hence, we need
        to produce the unsigned binary representation of ~n. To do that, we
        use the formula ~(~n ^ mask). This produces the unsigned binary
        representation of ~n, which is the answer.
        """
        mask = (1 << (len(bin(n)) - 2)) - 1
        return ~(~n ^ mask)


# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
