# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """LeetCode 19

        I remember that to find the nth node from the last, we just need to use
        the nth node from the start, and have two nodes moving at the same time
        Then when one node reaches the end, the other node would reach the nth
        position from the end.

        Of course, in actual implementation, we want to land at one node prior
        to the nth node from the end. And we need to use a dummy node. But
        these are just implementation details.

        O(N) 63 ms, faster than 33.98%
        """
        dummy = ListNode(next=head)
        pre = cur = dummy
        while n:
            cur = cur.next
            n -= 1
        while cur.next:
            cur = cur.next
            pre = pre.next
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        return dummy.next


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
