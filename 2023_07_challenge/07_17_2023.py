# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Reverse the input first.

        O(M + N), 82 ms, faster than 61.63%
        """

        def reverse(root: Optional[ListNode]) -> ListNode:
            dummy = ListNode(next=root)
            pre, cur = dummy, root
            while cur:
                tmp = cur.next
                cur.next = pre
                pre, cur = cur, tmp
            dummy.next.next = None
            return pre

        rl1, rl2 = reverse(l1), reverse(l2)
        carry = 0
        dummy = ListNode()
        node = dummy
        while rl1 and rl2:
            v = rl1.val + rl2.val + carry
            carry, r = divmod(v, 10)
            node.next = ListNode(val=r)
            node = node.next
            rl1 = rl1.next
            rl2 = rl2.next
        while rl1:
            v = rl1.val + carry
            carry, r = divmod(v, 10)
            node.next = ListNode(val=r)
            node = node.next
            rl1 = rl1.next
        while rl2:
            v = rl2.val + carry
            carry, r = divmod(v, 10)
            node.next = ListNode(val=r)
            node = node.next
            rl2 = rl2.next
        if carry:  # DON'T FORGET THE CARRY!!
            node.next = ListNode(val=carry)
        return reverse(dummy.next)


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Without reversing the inputs.

        My idea is to use recursion (or basically stack) to visit the tail first
        and then gradually build the answer list from right to left.

        But to make recursion work, I need to first fill in zeros to the left of
        the smaller linked list.

        O(M + N), 87 ms, faster than 33.81% 
        """
        def count(node: ListNode) -> int:
            c = 0
            while node:
                c += 1
                node = node.next
            return c

        def solve(node1: ListNode, node2: ListNode) -> Tuple[ListNode, int]:
            if node1.next is None and node2.next is None:
                v = node1.val + node2.val
                carry, r = divmod(v, 10)
                return ListNode(val=r), carry
            next_node, carry = solve(node1.next, node2.next)
            v = node1.val + node2.val + carry
            carry, r = divmod(v, 10)
            return ListNode(val=r, next=next_node), carry


        c1, c2 = count(l1), count(l2)
        if c1 > c2:
            dummy = ListNode()
            node = dummy
            k = c1 - c2
            while k:
                node.next = ListNode()
                node = node.next
                k -= 1
            node.next = l2
            l2 = dummy.next
        elif c1 < c2:
            dummy = ListNode()
            node = dummy
            k = c2 - c1
            while k:
                node.next = ListNode()
                node = node.next
                k -= 1
            node.next = l1
            l1 = dummy.next

        res, carry = solve(l1, l2)
        if carry > 0:
            return ListNode(val=carry, next=res)
        return res


        

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
