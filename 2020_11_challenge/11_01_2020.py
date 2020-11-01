# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def getDecimalValue(self, head: ListNode) -> int:
        """93% ranking"""
        bin_str = ''
        while head:
            bin_str += str(head.val)
            head = head.next
        return int(bin_str, 2)


class Solution2:
    def getDecimalValue(self, head: ListNode) -> int:
        """I like this one better, no need to record the binary number
        but compute the value directly.
        """
        res = 0
        while head:
            res = (res << 1) + head.val
            head = head.next
        return res


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
