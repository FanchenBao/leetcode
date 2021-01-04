# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Simple merge sort.

        O(N), 40 ms, 44% ranking.
        """
        dummy = ListNode()
        dummy.next = l2
        n2_l, n2_r = dummy, dummy.next
        n1 = l1
        while n1 and n2_r:
            if n1.val <= n2_r.val:
                temp = n1
                n1 = n1.next
                n2_l.next = temp
                temp.next = n2_r
            else:
                n2_r = n2_r.next
            n2_l = n2_l.next
        if not n2_r:
            n2_l.next = n1
        return dummy.next


class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """A better in-place solution.

        O(N), 28 ms, 98% ranking.
        """
        dummy = ListNode()
        dummy.next = l1
        cur, n1, n2 = dummy, l1, l2
        while n1 and n2:
            if n1.val <= n2.val:
                cur.next = n1
                n1 = n1.next
            else:
                cur.next = n2
                n2 = n2.next
            cur = cur.next
        cur.next = n1 or n2
        return dummy.next


# sol = Solution3()
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
