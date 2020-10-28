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

        Mathematics proof: suppose it takes S steps for slow (one step at a
        time) and fast (two steps at a time) to meet,
        suppose there are a steps before the cycle start, suppose there are b
        steps in the cycle, and suppose slow and fast meets at kth step within
        the circle.

        We have:

        S - a = mb + k
        2S - a = nb + k

        Thus S = (n - m)b

        Consider the number of steps before we can reach the cycle start from
        the point where slow and fast meet: b - k, and consider a = S - mb - k
        = (n - 2m)b - k. We discover that (b - k) mod b = ((n - 2m)b - k) mod b
        This means if we set a node at the meeting node, and set another node
        at the head, and have them move both at one step at a time, they will
        eventually meet at the cycle start.
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
