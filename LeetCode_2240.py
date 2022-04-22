# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        """865 ms, faster than 31.49% 

        The ranking seems low, maybe there is a pure math solution.
        """
        res = 0
        for w1 in range(total // cost1 + 1):
            res += (total - w1 * cost1) // cost2 + 1
        return res


class Solution2:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        """Exactly the same solution, but we make sure the iteration happens
        on the larger cost, thus reducing the number of iterations needed.

        527 ms, faster than 85.93% 
        """
        res = 0
        if cost2 > cost1:
            cost1, cost2 = cost2, cost1
        for w1 in range(total // cost1 + 1):
            res += (total - w1 * cost1) // cost2 + 1
        return res


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
