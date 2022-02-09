# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        """This one is not difficult. A simple DFS can obtain all the subtree
        sum. We store the sums directly in a counter. Eventually, we return the
        key of the counter with the highest frequency.

        O(N), 71 ms, 45% ranking.
        """
        counter = Counter()

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            cur_sum = node.val + dfs(node.left) + dfs(node.right)
            counter[cur_sum] += 1
            return cur_sum

        dfs(root)
        max_freq = max(counter.values())
        return [k for k, v in counter.items() if v == max_freq]
        

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
