# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode 142

        Suppose there are k steps from head to the start of the cycle.
        Suppose there are q steps from the start of the cycle to the node where
        slow and fast meet each other.
        Suppose the cycle has total steps p

        Then we have k + q is the total steps of the slow node when it reaches
        the meeting place.

        2(k + q) is the total steps taken by the fast node. Since slow and fast
        meet each other, we have

        (2(k + q) - k) % p = q
        (k + 2q) % p = q
        (k + q) % p = 0
        k + q = x * p
        k = x * p - q = (x - 1) * p + p - q
        
        (x - 1) * p is just a node going in the cycles x - 1 times. p - q is
        the number of steps from the meeting node to the start of the cycle.

        Thus if we have two nodes, one starting from the head, and the other
        starting from the meeting node, let them go at the same pace, then it
        is guaranteed that the two nodes will meet at the start of the cycle.

        Note: slow and fast must start from the head together in the first phase
        of the algo.

        O(N)
        """
        if not head or not head.next:  # edge cases
            return None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        if slow != fast:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast

        

# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
