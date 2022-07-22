# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """LeetCode 92

        We only need to do one pass. First, we reach the left node. Then we
        perform the normal linked list reversal operation. But, instead of
        checking whether we have reached the end of the list, we count how many
        steps have been taken. We should take right - left + 1 number of steps
        for the reversal operation, starting from the left node. The only other
        trick is to use a dummy node at the front.

        O(N), 39 ms, faster than 77.04%
        """
        dummy = ListNode(next=head)
        up, lnode = dummy, head
        additional = right - left + 1
        while left - 1:
            up = up.next
            lnode = lnode.next
            left -= 1
        pre, cur = up, lnode
        while additional:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            additional -= 1
        up.next.next = cur
        up.next = pre
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
