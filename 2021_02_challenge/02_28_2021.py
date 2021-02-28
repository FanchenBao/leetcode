# from pudb import set_trace; set_trace()
from typing import List
import heapq
from collections import defaultdict


class FreqStack1:
    """LeetCode 895

    Use a heap to manage the order of the values in the stack. The criteria
    of ordering is the frequency, followed by the position in the stack.
    Frequency is tacked by a separate dictionary, while position is tracked by
    a counter. Each value in the heap (stack) is a tupel of (-freq, -pos, value)
    and note that both freq and pos are negative values because we use a min
    heap.

    For each push and pop, the runtime is O(logN). 332 ms, 41% ranking.
    """

    def __init__(self):
        self.heap = []
        self.freq = defaultdict(int)
        self.cter = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        self.cter += 1
        heapq.heappush(self.heap, (-self.freq[x], -self.cter, x))

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.freq[val] -= 1
        return val


class FreqStack2:
    """This is the official solution, and it is very smart. It uses a stack of
    stack, which is `self.fstk`, to record the order of frequency. For instance,
    at pos 2 of self.fstk, we have all the values with frequency 2 + 1 = 3. And
    all these values are stored in yet another stack with the order of
    appearance. Therefore, when we pop, we only need to pop the top of self.fstk
    because the most frequent values are stored there. And within self.fstk[-1],
    we can always pop the top, because the values in self.fstk[-1] are pushed
    in according to their appearances.

    This is a very smart solution. And it runs in O(1), so it's also faster than
    my heap solution. The runtime is 288 ms, 97% ranking.
    """

    def __init__(self):
        self.freq = defaultdict(int)
        self.fstk = []

    def push(self, x: int) -> None:
        self.freq[x] += 1
        if len(self.fstk) < self.freq[x]:
            self.fstk.append([])
        self.fstk[self.freq[x] - 1].append(x)

    def pop(self) -> int:
        val = self.fstk[-1].pop()
        if not self.fstk[-1]:
            self.fstk.pop()
        self.freq[val] -= 1
        return val


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
