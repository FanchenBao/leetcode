# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """LeetCode 429

        Basic BFS.

        O(N), 78 ms, faster than 55.87% 
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            temp = []
            res.append([])
            for node in queue:
                res[-1].append(node.val)
                for child in node.children:
                    if child:
                        temp.append(child)
            queue = temp
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
