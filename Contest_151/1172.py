#! /usr/bin/env python3
from typing import List

# from collections import deque
# from bisect import bisect_right
# from pprint import pprint as pp
# from random import randint
# from collections import OrderedDict
"""08/26/2019

Solution1:

I am surprised that this problem is not as difficult as I had expected. The
only tricky part is to update self.left_most_index after each operation. I set
self.left_most_index to -1 to indicate that all current stacks are full and a
new stack must be provisioned for the next push. For the three operations, here
is a breakdown of their algorithm

push: As mentioned above, if self.left_most_index == -1, we need to provision a
new stack and set self.left_most_index to the index of the end index of list
self.stacks. Otherwise, we always add the val to the stack currently pointed to
by self.left_most_index. After adding the val, if there is still capacity in
self.stacks[self.left_most_index], we don't need to change anything. If there
is no more capacity, we need to find a new self.left_most_index. This is where
I fear I might TLE, because in this solution, the method of locating the new
self.left_most_index is a linear search for the next stack that has some capacity
left. If no such stack can be found, we set self.left_most_index to -1.

pop: When self.stacks contains nothing, we return -1 and also set
self.left_most_index to -1. Otherwise, we can always pop something from the right
most stack. After the pop, we need to check whether the right most stack is
empty. If not, we leave everything as is and return the popped value. If it is
empty, we need to remove all empty stacks to the right. Afterwards, we need to
check whether the stack pointed to by self.left_most_index has been removed. If
it hasn't, we don't have to change anything. Otherwise, we set self.left_most_index
to -1, because no current stack would have capacity (because if there is a stack
with capacity, then self.left_most_index would not be pointing to the stack
that has just been removed).

popAtStack: If index is out of range, return -1 and nothing needs to change. If
index points to the end of self.stacks, then popAtStack() is the same as pop()
and we can reuse code. If index is within the current self.stacks, we need to
check whether self.stacks[index] is emtpy. If it is empty, we return -1 and
there is no need to change anything (because nothing has changed after calling
popAtStack()). Otherwise, we pop the val at self.stacks[index], and update
self.left_most_index if necessary, i.e. if the stack with its top val pooped
has index smaller than self.left_most_index, we set self.left_most_index to
this stack.

And that's it. This solution clocked in at 924 ms, 60%.


Solution from discussion:
https://leetcode.com/problems/dinner-plate-stacks/discuss/366331/C%2B%2BPython-Solution

I am too lazy to implement this, but the idea is brilliant: use a heap to manage
the left most indices. Since the only chance of creating capcity is through
popAtStack, we need to record the indices for this call in a min heap, thus we
would always have access to the left most index that points to a stack with
capacity. When this heap is empty, we know a new stack needs to be provisioned.
The only tricky part is when we push into the left most index and make that
stack full. Thus, before we push, we need to check the top of the min heap and
see whether the stack pointed to by that top index still has capacity. If not,
we need to remove the top index and try the next one. This is a much better
solution than mine in terms of tracking the left most index.
"""


class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks: List[List[int]] = []
        self.left_most_index = -1  # index of left most stack that has capacity

    def push(self, val: int) -> None:
        if self.left_most_index == -1:
            self.stacks.append([])
            self.left_most_index = len(self.stacks) - 1
        self.stacks[self.left_most_index].append(val)
        if len(self.stacks[self.left_most_index]) == self.capacity:
            for i in range(self.left_most_index + 1, len(self.stacks)):
                if len(self.stacks[i]) < self.capacity:
                    self.left_most_index = i
                    break
            else:
                self.left_most_index = -1

    def pop(self) -> int:
        if not self.stacks:
            self.left_most_index = -1
            return -1
        else:
            res = self.stacks[-1].pop()
            while self.stacks and not self.stacks[-1]:
                self.stacks.pop()
            # update left_most_index if necessary
            if self.left_most_index >= len(self.stacks):
                self.left_most_index = -1
            return res

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        elif index == len(self.stacks) - 1:
            return self.pop()
        else:
            # update left_most_index if index is smaller
            self.left_most_index = min(self.left_most_index, index)
            return self.stacks[index].pop()
