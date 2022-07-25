# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """LeetCode 86

        Cut out the bigger nodes into its own list, and then merge the smaller
        and bigger lists together.

        O(N), 52 ms, faster than 54.09% 
        """
        dummy_small = ListNode(next=head)
        dummy_big = ListNode()
        bigger = dummy_big
        pre, cur = dummy_small, head
        while cur:
            if cur.val >= x:
                pre.next = cur.next
                bigger.next = cur
                cur.next = None
                cur = pre.next
                bigger = bigger.next
            else:
                cur = cur.next
                pre = pre.next
        pre.next = dummy_big.next
        return dummy_small.next

        


# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
