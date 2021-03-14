# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        """We have discussed that this problem can have a few cheat ways to
        solve, but most likely we won't be able to use the cheat method in an
        interview. So we wrote a "true" solution which is O(1) in space.

        The idea of this "true" solution is to identify the nodes to be swapped
        and then swap them. There are two tricks. First, if the nodes to be
        swapped are adjacent to each other, the algorithm for swapping is
        different from when they are not adjacent, or if they are the same node.
        Second, it is possible that k is a large value, and the "left" node
        could be to the right of the "right" node. Once we have handled these
        two tricks, the solution is not difficult.

        O(N), 1092 ms, 67% ranking.
        """
        # Find the total lenght of the linked list
        N, node = 0, head
        while node:
            N += 1
            node = node.next
        # Identify the nodes right before the target nodes
        dummy = ListNode(next=head)
        c, node = 0, dummy
        # nodes right before the ones to be swapped
        pre_left, pre_right = None, None
        while node and (not pre_left or not pre_right):
            if c == min(N - k, k - 1):  # locate the previous node before left
                pre_left = node
            if c == max(N - k, k - 1):  # locate the previous node before right
                pre_right = node
            node = node.next
            c += 1
        left, post_left = pre_left.next, pre_left.next.next
        right, post_right = pre_right.next, pre_right.next.next
        # special case is when left and right are adjacent
        if pre_left.next is pre_right:
            right.next = left
        else:  # there are at least one node between left and right
            right.next = post_left
            pre_right.next = left
        pre_left.next = right
        left.next = post_right
        return dummy.next


class Solution2:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        """One pass solution to identify the nodes to be swapped.

        This is apparently a much better way of finding the target node and
        making the swap. It avoids all the edge case checking I have to do. To
        fully understand it, we have to draw some diagrams.

        reference: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1054370/Python-3-or-Swapping-NODES-or-Swapping-Values-or-One-Pass-or-Fully-explained
        """
        dummy = ListNode(next=head)
        # One pass to find pre_left, left, and pre_right, right
        pre_left, left = dummy, head
        for _ in range(k - 1):
            pre_left = left
            left = left.next
        node = left
        pre_right, right = dummy, head
        while node.next:
            pre_right = right
            right = right.next
            node = node.next
        # Swapping without the need to check for edge cases.
        pre_left.next, pre_right.next = right, left
        left.next, right.next = right.next, left.next
        return dummy.next



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
