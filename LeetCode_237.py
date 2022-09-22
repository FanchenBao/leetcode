# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        The hint is that we don't have to remove the node from memory. So we
        just update the values by moving the next node's value to the current
        node, until we reach the node before the last node. Then we just close
        the linked list there.

        O(N), 76 ms, faster than 27.63%
        """
        while node.next.next:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None


class Solution2:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        This is from the official solution. Just delete the next node, and
        then update the current node's value with the next node's value.

        So dumb of me.

        O(1)
        """
        node.val, node.next = node.next.val, node.next.next
        


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
