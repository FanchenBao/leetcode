from pudb import set_trace; set_trace()
from typing import List, Tuple
import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution1:
    """Use merge sort. 37% ranking.
    
    This is the top down approach, which according to the standard solution is
    not constant space, because we are using log(N) space for storing the
    intermediate callstack due to the recusion calls.
    """

    def count_length(self, head: ListNode) -> int:
        node, count = head, 0
        while node:
            node = node.next
            count += 1
        return count

    def split(self, head: ListNode, count: int) -> ListNode:
        node = head
        for _ in range(count // 2 - 1):
            node = node.next
        right_head = node.next
        node.next = None
        return right_head

    def merge(self, sort_left: ListNode, sort_right: ListNode) -> ListNode:
        dummy = ListNode(-math.inf)
        node = dummy
        while sort_left and sort_right:
            if sort_left.val < sort_right.val:
                node.next = sort_left
                sort_left = sort_left.next
            else:
                node.next = sort_right
                sort_right = sort_right.next
            node = node.next
        node.next = sort_left if sort_left else sort_right
        return dummy.next

    def sortList(self, head: ListNode) -> ListNode:
        count = self.count_length(head)
        if count <= 1:  # edge case
            return head
        left, right = head, self.split(head, count)
        return self.merge(self.sortList(left), self.sortList(right))


class Solution2:
    """Use merge sort. Bottom up approach.

    This is not intellectually difficult, but the actual implementation of the
    bottom up solution is tricky to say the least. Use of a dummy node
    simplifies the implementation tremendously.
    """

    def split_n_merge(self, head: ListNode, n: int):
        """This is split and merge combined. We select the first
        n nodes as left (from ls to le), and the next n nodes as right (from
        rs to re). Due to the bottom up nature, left and right must be sorted
        respectively. We then merge the two and return the start of the
        merged (and sorted) bigger list, the end of the merged list, and the
        next starting position.

        The tricky part is to handle cases where there are not enough nodes
        to form the left, or not enough nodes to form the right. In the first
        case, a split and merge cannot be done and we simply return. In the
        second case, merge can still be done despite the right not having the
        required length.
        """
        ls, le = head, head
        for _ in range(n - 1):
            if le:
                le = le.next
            else:
                break
        if not le:  # not enough nodes to split and merge
            return ls, None, None
        rs, re = le.next, le.next
        le.next = None  # seal off the left list
        for _ in range(n - 1):
            if re:
                re = re.next
            else:
                break
        if re:
            next_start = re.next
            re.next = None  # seal off the right list
        else:  # although the right has not enough nodes, we can still merge
            next_start = None
        sort_start = self.merge(ls, rs)
        return sort_start, le if le.next is None else re, next_start

    def count_length(self, head: ListNode) -> int:
        node, count = head, 0
        while node:
            node = node.next
            count += 1
        return count

    def merge(self, sort_left: ListNode, sort_right: ListNode) -> ListNode:
        dummy = ListNode(-math.inf)
        node = dummy
        while sort_left and sort_right:
            if sort_left.val < sort_right.val:
                node.next = sort_left
                sort_left = sort_left.next
            else:
                node.next = sort_right
                sort_right = sort_right.next
            node = node.next
        node.next = sort_left if sort_left else sort_right
        return dummy.next

    def sortList(self, head: ListNode) -> ListNode:
        count = self.count_length(head)
        if count <= 1:  # edge case
            return head

        n = 0
        dummy = ListNode(val=-math.inf, next=head)
        sort_end = dummy
        next_start = dummy.next
        while (1 << n) <= count:
            while next_start:
                ss, se, next_start = self.split_n_merge(next_start, 1 << n)
                sort_end.next = ss
                sort_end = se
            n += 1
            sort_end = dummy
            next_start = dummy.next
        return dummy.next


dummy = ListNode()
node = dummy
for v in [23,54,32,65,45,765]:
    node.next = ListNode(v)
    node = node.next

sol = Solution2()
sol.sortList(dummy.next)
# tests = [
#     # ([1, 2, 3, 1], 3, 0, True),
#     # ([1, 0, 1, 1], 1, 2, True),
#     ([1, 5, 9, 1, 5, 9], 2, 3, False),
#     # ([1, 4, 9, 1, 4, 9], 1, 3, True),
#     # ([-1, -1], 1, -1, False),
#     # ([1, 3, 6, 2], 1, 2, True),
# ]

# for i, (nums, k, t, ans) in enumerate(tests):
#     res = sol.containsNearbyAlmostDuplicate(nums, k, t)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
