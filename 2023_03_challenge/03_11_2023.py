# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution1:
    def sortedListToBST(self, head: Optional[ListNode], bound: int = math.inf) -> Optional[TreeNode]:
        """LeetCode 109

        Recursion. At each round, we find the middle node of the linked list by
        way of slow and fast node. Then we divide the linked list to left and
        right half. For each half, we repeat the same procedure.

        In order to know the boundary of each half, we introduce a bound value
        that indicates the value of the boundary node.

        O(NlogN), 134 ms, faster than 32.26%
        """
        if not head or head.val == bound:
            return None
        slow, fast = head, head
        while fast and fast.next and fast.val != bound and fast.next.val != bound:
            fast = fast.next.next
            slow = slow.next

        root = TreeNode(val=slow.val)
        root.left = self.sortedListToBST(head, bound=slow.val)
        root.right = self.sortedListToBST(slow.next, bound=bound)
        return root


class Solution2:
    def sortedListToBST(self, head: Optional[ListNode], tail: Optional[ListNode] = None) -> Optional[TreeNode]:
        """We can make the boundary a ListNode, which will simplify the logic.
        """
        if head == tail:
            return None
        slow, fast = head, head
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next

        return TreeNode(
            val=slow.val,
            left=self.sortedListToBST(head, slow),
            right=self.sortedListToBST(slow.next, tail)
        )



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
