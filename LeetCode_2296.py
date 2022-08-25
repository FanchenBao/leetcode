# from pudb import set_trace; set_trace()
from typing import List
from collections import deque


class ListNode:
    def __init__(self, val, _pre=None, _next=None):
        self.val = val
        self.pre = _pre
        self.next = _next


class TextEditor1:
    """One shot, and we got it!

    Use a doubly-linked list, and the problem is medium at most.

    O(K) time complexity for each operation. 7823 ms, faster than 11.40%
    """

    def __init__(self):
        self.dummy_head = ListNode('*')
        self.dummy_tail = ListNode('*')
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.pre = self.dummy_head
        self.cur = self.dummy_tail

    def addText(self, text: str) -> None:
        for le in text:
            node = ListNode(le, _pre=self.cur.pre, _next=self.cur)
            self.cur.pre.next = node
            self.cur.pre = node

    def deleteText(self, k: int) -> int:
        res = 0
        while self.cur.pre.val != '*' and k:
            tmp = self.cur.pre
            tmp.pre.next = self.cur
            self.cur.pre = tmp.pre
            tmp.pre = tmp.next = None
            k -= 1
            res += 1
        return res

    def _str_on_left(self, n: int) -> str:
        res = []
        node = self.cur.pre
        while node.val != '*' and n:
            res.append(node.val)
            node = node.pre
            n -= 1
        return ''.join(res[::-1])

    def cursorLeft(self, k: int) -> str:
        while self.cur.pre.val != '*' and k:
            self.cur = self.cur.pre
            k -= 1
        return self._str_on_left(10)

    def cursorRight(self, k: int) -> str:
        while self.cur.val != '*' and k:
            self.cur = self.cur.next
            k -= 1
        return self._str_on_left(10)


class TextEditor2:
    """Using the hint with two deques. Brilliant, just brilliant!

    So much faster:  828 ms, faster than 85.62%
    """

    def __init__(self):
        self.prefix = deque()
        self.suffix = deque()

    def addText(self, text: str) -> None:
        for le in text:
            self.prefix.append(le)

    def deleteText(self, k: int) -> int:
        res = 0
        while self.prefix and k:
            self.prefix.pop()
            k -= 1
            res += 1
        return res

    def cursorLeft(self, k: int) -> str:
        while self.prefix and k:
            self.suffix.appendleft(self.prefix.pop())
            k -= 1
        return ''.join(self.prefix[i] for i in range(max(-10, -len(self.prefix)), 0))

    def cursorRight(self, k: int) -> str:
        while self.suffix and k:
            self.prefix.append(self.suffix.popleft())
            k -= 1
        return ''.join(self.prefix[i] for i in range(max(-10, -len(self.prefix)), 0))

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
