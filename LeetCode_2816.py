# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Solution1: get the actual number, double it, and create a new linked
        list from the double

        This solution would error: exceeds the limit (4300 digits) for integer
        string conversion. So the lazy method doesn't work. We will have to
        reverse.
        """
        ori = 0
        node = head
        while node:
            ori = ori * 10 + node.val
            node = node.next
        db = str(ori * 2)
        dummy = ListNode()
        node = dummy
        for d in db:
            node.next = ListNode(val=int(d))
            node = node.next
        return dummy.next


class Solution2:
    def reverse(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        pre, cur = dummy, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        head.next = None
        return pre

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        We reverse the linked list

        O(N), 354 ms, faster than 25.13%
        """
        tail = self.reverse(head)
        dummy = ListNode()
        node = dummy
        ori_node = tail
        c = 0
        while ori_node:
            c, v = divmod(ori_node.val * 2 + c, 10)
            node.next = ListNode(val=v)
            node = node.next
            ori_node = ori_node.next
        if c > 0:
            node.next = ListNode(val=c)
            node = node.next
        self.reverse(dummy.next)
        return node


class Solution3:
    def reverse(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        pre, cur = dummy, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        head.next = None
        return pre

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Try to modify in place

        Much faster: 241 ms, faster than 56.28%
        """
        tail = self.reverse(head)
        node = tail
        c = 0
        while True:
            c, v = divmod(node.val * 2 + c, 10)
            node.val = v
            if node.next:
                node = node.next
            else:
                break
        if c > 0:
            node.next = ListNode(val=c)
            node = node.next
        self.reverse(tail)
        return node


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
