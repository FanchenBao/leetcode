# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """I try to not use an array. Instead, we use two pointers to identify
        the center of the linked list, and then take advantage of recursion to
        go backwards on the linked list.

        O(N), 1873 ms, 5%
        """
        self.res = 0
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        def helper(node: ListNode) -> ListNode:
            if node == slow:
                self.res = max(self.res, node.val + node.next.val)
                return node.next.next
            twin = helper(node.next)
            self.res = max(self.res, node.val + twin.val)
            return twin.next

        helper(head)
        return self.res


class Solution2:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """Use extra space, to store everything from the linked list to a
        randomly-accessible storage room.

        1857 ms, 5% ranking.
        """
        res = 0
        node, vals = head, []
        while node:
            vals.append(node.val)
            node = node.next
        lo, hi = 0, len(vals) - 1
        while lo < hi:
            res = max(res, vals[lo] + vals[hi])
            lo += 1
            hi -= 1
        return res
        


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
