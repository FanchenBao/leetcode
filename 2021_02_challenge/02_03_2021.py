# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        """I vaguely remembered that I had done similar problem before. And this
        solution was the traditional two pointer solution, with a slow node and
        a fast node. The slow node goes one at a time, while the fast two at
        a time. If there is a cycle in the linked-list, then the slow and the
        fast will meet each other somewhere during iteration.

        I checked the official solution, and this method is called "Floyd's
        Cycle".

        O(N), 80 ms, 10% ranking.
        """
        n1 = n2 = head
        while n2 and n2.next:
            n1 = n1.next
            n2 = n2.next.next
            if n1 == n2:
                return True
        return False


class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        """Try to use Mr. Pochmann's EAFP method to improve speed.
        This is exactly his code, and it does improve trememdously. The reason
        for the improved runtime is that we are doing fewer "if" checks in each
        iteration.

        O(N), 44 ms, 90% ranking.
        """
        try:
            n1, n2 = head, head.next
            while n1 != n2:
                n1 = n1.next
                n2 = n2.next.next
            return True
        except:
            return False



sol = Solution3()
tests = [
    ('abab', True),
    ('aba', False),
    ('abcabcabcabc', True),
    ('abcabcababcabcab', True),
    ('abcbac', False),
    ('aabaabaab', True),
    ('a', False),
    ('aaaaaaa', True),
    ('aaaaab', False),
]

for i, (s, ans) in enumerate(tests):
    res = sol.repeatedSubstringPattern(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
