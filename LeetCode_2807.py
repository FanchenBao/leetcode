# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Recursion is the way to go.

        O(N), 65 ms, faster than 83.28%
        """
        if head.next:
            head.next = ListNode(
                val=math.gcd(head.val, head.next.val),
                next=self.insertGreatestCommonDivisors(head.next),
            )
        return head


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
