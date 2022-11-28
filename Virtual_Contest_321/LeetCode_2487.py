# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """This is more or less a cheating method? Because we basically turn the
        linkedlist into a monotonic decreasing array, and then turn the array
        back to linked list.

        O(N), but space complexity is also O(N).
        """
        stack = []
        while head:
            val = head.val
            while stack and stack[-1] < val:
                stack.pop()
            stack.append(val)
            head = head.next
        if not stack:
            return None
        dummy = ListNode()
        node = dummy
        for v in stack:
            node.next = ListNode()
            node = node.next
            node.val = v
        return dummy.next


class Solution2:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """This is lee215's solution: https://leetcode.com/problems/remove-nodes-from-linked-list/discuss/2852139/JavaC%2B%2BPython-3-Line-Recursion-Solution

        The result is a linkedlist with monotonic decreasing characteristics.
        If we process the linkedlist from right to left, it is guaranteed that
        each time a node is under consideration, all the nodes to its right must
        have formed the monotonic decreasing property. Thus, the current node
        only needs to be compared to its next to determine whether it itself
        shall be removed.

        This can be achieved using recursion
        """

        def helper(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node:
                return None
            nex_node = helper(node.next)
            if not nex_node or node.val >= nex_node.val:
                node.next = nex_node
                return node
            return nex_node

        return helper(head)

        

# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
