# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """LeetCode 109

        The idea is to always find the center node of a given list, and use
        that as the current root. After picking the current root, we treat the
        left portion of the linked list as the left subtree, and the right
        portion the right subtree. We perform recursion on both portions.

        The trickly part, for me, is to identify the condition for the fast node
        to stop. We use the fast-slow node trick to find the center. The fast
        node can stop either when the tail is None or not None. This requires
        two types of check, hence the extremely long check in the while
        condition. We can check for val because the values in the linked list
        are unique, due to the requirement of strict increasing order.

        O(Nlog(N)), 152 ms, 9% ranking.
        """
        def helper(head: ListNode, tail: ListNode) -> TreeNode:
            if head.next is None or (tail is not None and head.next.val == tail.val):
                return None
            slow, fast = head, head
            while (tail is None and fast and fast.next) or (tail is not None and fast.val != tail.val and fast.next.val != tail.val):
                fast = fast.next.next
                slow = slow.next
            return TreeNode(val=slow.val, left=helper(head, slow), right=helper(slow, tail))

        return helper(ListNode(val=-math.inf, next=head), None)


class Solution2:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """Same concept but better implementation.

        Reference: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/discuss/35476/Share-my-JAVA-solution-1ms-very-short-and-concise.
        """
        def helper(head: ListNode, tail: ListNode) -> TreeNode:
            if head == tail:
                return None
            slow, fast = head, head
            while fast != tail and fast.next != tail:
                fast = fast.next.next
                slow = slow.next
            return TreeNode(val=slow.val, left=helper(head, slow), right=helper(slow.next, tail))

        return helper(head, None)
# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
