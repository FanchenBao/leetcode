# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        """LeetCode 234

        Straightforward solution with O(N) space.

        O(N), 808 ms, 30% ranking.
        """
        lst = []
        node = head
        while node:
            lst.append(node.val)
            node = node.next
        return lst == lst[::-1]


class Solution2:
    def get_length(self, head: ListNode):
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        return count

    def reverse(self, head: ListNode):
        pre, cur, nex = None, head, head.next
        while cur:
            cur.next = pre
            pre = cur
            cur = nex
            if nex is not None:
                nex = nex.next

    def isPalindrome(self, head: ListNode) -> bool:
        """O(1) space. We split the linked list into two halves, reverse the
        first half, and then compare the two halves.

        O(N), 916 ms, 7% ranking.
        """
        count = self.get_length(head)
        first_half_end = head
        for _ in range(count // 2 - 1):
            first_half_end = first_half_end.next
        middle = first_half_end.next
        second_half_start = middle.next if count % 2 else middle
        # cut out the first half linked list
        first_half_end.next = None
        self.reverse(head)
        node1, node2 = first_half_end, second_half_start
        res = True
        while node1 and node2:
            if node1.val != node2.val:
                res = False
                break
            node1 = node1.next
            node2 = node2.next
        # restore order
        self.reverse(first_half_end)
        first_half_end.next = middle
        return res


class Solution3:

    def reverse(self, head: ListNode):
        pre, cur, nex = None, head, head.next
        while cur:
            cur.next = pre
            pre = cur
            cur = nex
            if nex is not None:
                nex = nex.next
        return pre

    def isPalindrome(self, head: ListNode) -> bool:
        """This is using fast and slow pointers to traverse the linked list in
        one shot to identify the center position.

        This is with restoration
        """
        # Find the middle node
        dummy = ListNode(next=head)
        fast, slow, linker = head, head, dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            linker = linker.next
        if fast:
            second_half_start = slow.next
            linker = linker.next
        else:
            second_half_start = slow
        tail = self.reverse(second_half_start)
        l, r = head, tail
        res = True
        while l and r:
            if l.val != r.val:
                res = False
                break
            l = l.next
            r = r.next
        self.reverse(tail)  # restoration
        linker.next = second_half_start
        return res


class Solution4:

    def reverse(self, head: ListNode):
        pre, cur, nex = None, head, head.next
        while cur:
            cur.next = pre
            pre = cur
            cur = nex
            if nex is not None:
                nex = nex.next
        return pre

    def isPalindrome(self, head: ListNode) -> bool:
        """Without restoration
        """
        if head.next is None:
            return True
        # Find the middle node
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        l, r = head, self.reverse(slow)
        res = True
        while l and r:
            if l.val != r.val:
                res = False
                break
            l = l.next
            r = r.next
        return res


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
