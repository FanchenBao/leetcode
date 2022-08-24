# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(next=head)
        pre, cur = dummy, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        dummy.next.next = None
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """LeetCode 234

        Find the second half, reverse it, compare, reverse back, return.

        O(N) time and O(1) space, 1438 ms, faster than 24.12%
        """
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        rev_head = self.reverse(slow.next)
        res = True
        n1, n2 = head, rev_head
        while n2:
            if n1.val != n2.val:
                res = False
                break
            n1 = n1.next
            n2 = n2.next
        self.reverse(rev_head)
        return res


sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
