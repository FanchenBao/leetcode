#! /usr/bin/env python3
"""07/18/2019

This is not a particularly difficult problem, but it does trigger some
interesting brainstorm. Solution 1 is iterative. Since I have worked out how
to reverse a linked list in one pass before, coming up with this solution is
not hard, yet one thing to keep in mind is that I need an anchor
node to record the position right before the reversal, such that it can
connect to the new tail after the reversal.

Much fun happens to Solution 2. I did not think about using recursion at the
beginning, but the Solution section mentioned recursion and provided a general
idea to achieve it. So without looking at the code, I managed to come up with
the recursion solution. The basic idea is like this: since we are swapping the
values between two nodes to achieve reversal, we must know the front and back
node at the same time. Front node is easy to get, but back node is a
bit tricky, since we only want O(N) complexity. With recursion, in order to
find the front and back nodes (at position m and n), we must first make sure
the nodes in between front and back are already reversed. So we can recursively
call the function on the smaller stretch of linked list from position m+1 to
n-1, reverse it, and return the node at position n. Then we will have the back
node. The anchor case is when m == n or n - m == 1.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy: ListNode = ListNode(0)
        dummy.next = head
        b: ListNode = dummy
        c: ListNode = head
        f: ListNode = c.next
        count: int = 1
        while count < m:
            b = b.next
            c = c.next
            f = f.next
            count += 1
        anchor: ListNode = b
        while count < n:
            b = c
            c = f
            f = f.next
            c.next = b
            count += 1
        anchor.next.next = f
        anchor.next = c
        return dummy.next


class Solution2:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        f: ListNode = head
        count: int = 1
        while count < m:
            f = f.next
            count += 1
        self.helper(f, m, n)
        return head

    def helper(self, front: ListNode, m: int, n: int) -> ListNode:
        """ locate the node at position n, swap its val with front,
            and return the node at position n + 1
        """
        temp: int = 0
        if m == n:
            return front.next
        elif n - m == 1:
            temp = front.val
            front.val = front.next.val
            front.next.val = temp
            return front.next.next
        else:
            # find the node at position n
            back: ListNode = self.helper(front.next, m + 1, n - 1)
            # swap value between b and f
            temp = front.val
            front.val = back.val
            back.val = temp
            return back.next
