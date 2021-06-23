# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """LeetCode 92

        Slightly more complicated linked list reversal. The idea is the same
        as reversing the entire linked list, but we just need to record where
        the reversal starts. And at the end, we need to reconnect the reversed
        part with the rest of the linked list. Using a dummy node at the
        beginning is always recommended.

        O(N), 28 ms, 86% ranking.
        """
        dummy = ListNode(next=head)
        pre, cur = dummy, dummy.next
        for _ in range(left - 1):
            cur = cur.next
            pre = pre.next
        left_node = cur
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        left_node.next.next = pre
        left_node.next = cur
        return dummy.next


class Solution2:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """Recursion solution from the official solution. The idea is to create
        a backward pointer via recursion. The tricky part is to figure out the
        terminating condition, which is when the true_left_node is the same as
        the current node (odd number of nodes to reverse) or the true_left_node.next
        is the same as the current node (even number of nodes to reverse).

        O(N), 32 ms.
        """

        def helper(left_node: ListNode, node: ListNode, n: int) -> ListNode:
            true_left_node = left_node if n == right else helper(left_node, node.next, n + 1)
            if true_left_node:
                true_left_node.val, node.val = node.val, true_left_node.val
                if true_left_node == node or true_left_node.next == node:
                    return None
                else:
                    return true_left_node.next
            return None

        node = head
        for _ in range(left - 1):
            node = node.next
        helper(node, node, left)
        return head


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
