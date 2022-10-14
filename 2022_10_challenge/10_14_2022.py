# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode 2095

        Use slow and fast node to find the node right before the one to be
        deleted. A little tricky to identify where the fast node shall start,
        but overall it's the same slow-fast node idea to locate the center.

        O(N), 4867 ms, faster than 6.07%
        """
        dummy = ListNode(next=head)
        slow = dummy
        fast = head.next
        while fast:
            fast = fast.next
            fast = fast.next if fast else None
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


class Solution2:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """From the official solution without using a dummy node. It turns out
        that the solution is much cleaner if we ditch the dummy node.

        O(N), 1923 ms, faster than 88.44%

        LeetCode does not like ifs
        """
        if not head.next:
            return None
        slow = head
        fast = head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        

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
