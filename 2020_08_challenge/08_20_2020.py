# from pudb import set_trace; set_trace()
from typing import List, Tuple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def helper(self, n: int, is_odd: bool, head: ListNode) -> Tuple[ListNode, ListNode]:
        """Recursion.

        For each current nth node, we order the n + 1 till N - n nodes by 
        calling the recursion function, which returns the head node of the inner
        ordered nodes, and the tail node that the inner ordered nodes originally
        point to. This tail node is the one to be moved next to the nth node.

        Eventually, the function returns the head node of the current ordering,
        which is the nth node itself, and the tail node that the current
        ordering originally points to, which is the next node of the previously
        returned inner tail node.
        
        :param n: The current node is the nth node in the original order,
            starting from 1.
        :param is_odd: Whether the total number of nodes is odd.
        :param node: The current node.
        :return: The head node of the current ordering and the tail node that
            the current ordering originally points to.
        """
        if n == 1:  # base case
            if is_odd:
                tail = head.next
                head.next = None
                return head, tail
            else:
                tail = head.next.next
                head.next.next = None
                return head, tail
        else:
            inner_head, inner_tail = self.helper(n - 1, is_odd, head.next)
            tail = inner_tail.next
            head.next = inner_tail
            inner_tail.next = inner_head
            return head, tail

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        num = 0
        node = head  # count number of nodes
        while node:
            num += 1
            node = node.next
        if num > 2:  # if two nodes or less, no change
            self.helper((num + 1) // 2, num % 2, head)


class Solution2:
    def reorderList(self, head: ListNode) -> None:
        """
        Three-step method: find middle node, reverse post middle nodes, merge.
        """
        if not head or not head.next or not head.next.next:
            return
        # find the middle node
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse the post middle nodes
        pre = slow
        rev_tail = slow.next
        cur = slow.next
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        rev_tail.next = None
        slow.next = None
        # Merge the first and second half
        first = head
        second = pre
        while second:
            temp_f = first.next
            temp_s = second.next
            first.next = second
            second.next = temp_f
            second = temp_s
            first = temp_f




