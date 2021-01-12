# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Sort of cheating method. We obtain both numbers first, add them
        together, and then turn the result number into a linked list. I am
        pretty sure this is not how the question is supposed to be resolved.

        O(N), 76 ms, 28% ranking.
        """
        num1, i = 0, 0
        while l1:
            num1 += l1.val * 10**i
            l1 = l1.next
            i += 1
        num2, i = 0, 0
        while l2:
            num2 += l2.val * 10**i
            l2 = l2.next
            i += 1
        s = num1 + num2
        if s == 0:  # edge case
            return ListNode()
        dummy = ListNode()
        node = dummy
        while s:
            node.next = ListNode()
            node = node.next
            node.val = s % 10
            s //= 10
        return dummy.next


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """This is the more official solution, traversing and computing the
        sum simultaneously.

        O(N), 68 ms, 75% ranking.
        """
        dummy = ListNode()
        carry = 0
        node = dummy
        while l1 or l2 or carry:
            node.next = ListNode()
            node = node.next
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            node.val, carry = divmod(v1 + v2 + carry, 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
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
