# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """Couldn't solve this problem, despite being able to solve it a year
        ago. I have the idea of creating three states, but got confused about
        where the three states are applied. They should be applied in the
        return value. But my earlier attempt was trying to apply them at the
        start.
        """
        def dfs(node) -> List[int]:
            """The return value is [c0, c1, c2].
            c0 is the min count of cameras of the subtree when node has no camera no coverage from its parent.
            c1 is the min count of cameras of the subtree when node has no camera but coverage from its parent.
            c2 is the min count of cameras of the subtree when node has camera from its parent.
            """
            if not node:
                return 0, 0, math.inf
            L, R = dfs(node.left), dfs(node.right)
            return [
                # cannot include L[1] and R[1] because the children cannot have
                # coverage when the node does not have camera
                min(L[2] + min(R[0], R[2]), R[2] + min(L[0], L[2])),
                min(L[0], L[2]) + min(R[0], R[2]),
                # must add one because the node must have camera
                min(L[1], L[2]) + min(R[1], R[2]) + 1,
            ]
            
        res = dfs(root)
        return min(res[0], res[2])


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
