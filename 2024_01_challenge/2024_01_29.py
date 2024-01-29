# from pudb import set_trace; set_trace()
from typing import List
import math


class MyQueue:
    """
    LeetCode 232

    Use two stacks, one for pushing and the other for popping. When the pop
    stack is empty, get everything from the push stack into the pop stack.

    44 ms, faster than 17.34%
    """

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
        
    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if self.peek():
            return self.pop_stack.pop()
        
    def peek(self) -> int:
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        if self.pop_stack:
            return self.pop_stack[-1]
        return 0

    def empty(self) -> bool:
        return len(self.push_stack) + len(self.pop_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
