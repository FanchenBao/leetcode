# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def detectCycle(self, head: ListNode) -> ListNode:
        """62% ranking.
        This is not O(1) memory.
        """
        seen = set()
        while id(head) not in seen:
            seen.add(id(head))
            head = head.next
        return head


class Solution2:
    def detectCycle(self, head: ListNode) -> ListNode:
        """This is O(1)

        Mathematics proof: suppose there are m steps before the start of the
        cycle. Suppose there are n steps between the start of the cycle and the
        point where the slow and fast nodes first meet. Suppose the number of
        steps between where the fast and slow nodes meet and the start of the
        cycle is p (i.e. the cycle size l = p + n). Suppose k is the number of
        times the fast node has cycled.

        2(m + n) = m + n + kl = m + n + k(p + n)

        We get m = k(p + n) - n = p + (k - 1)l

        In other words, the number of steps from the root node to the start of
        the cycle is the same as the number of steps from where the slow and
        fast nodes first meet to the start of the cycle plus a multiple of the
        cycle size. This means, if we place the slow node back at the root, and
        let the slow and fast both move one step at a time. They will eventually
        meet at the start of the cycle (note that the fast node might have to
        go through the cycle multiple times, but the final meeting place is
        always the start of the cycle).

        A special case is when k = 1, which means the fast node initially has
        only gotten through the cycle once. This can help us visialize the more
        generic situation where k > 1.
        """
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


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
