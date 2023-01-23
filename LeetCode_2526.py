# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter, deque


class DataStream1:

    def __init__(self, value: int, k: int):
        """Very naive solution, but it works.

        However, the performance is terrible.

        2073 ms, faster than 5.04%
        """
        self.counter = Counter()
        self.queue = deque()
        self.k = k
        self.value = value

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.counter[num] += 1
        if len(self.queue) < self.k:
            return False
        if len(self.queue) > self.k:
            p = self.queue.popleft()
            self.counter[p] -= 1
            if not self.counter[p]:
                self.counter.pop(p)
        return len(self.counter) == 1 and self.queue[0] == self.value


class DataStream2:

    def __init__(self, value: int, k: int):
        """Each element in the queue shall be [value, count]

        Much faster, but the percentage is stil abysmal

        914 ms, faster than 5.76%
        """
        self.queue = deque()
        self.k = k
        self.value = value
        self.count = 0

    def consec(self, num: int) -> bool:
        if not self.queue or self.queue[-1][0] != num:
            self.queue.append([num, 0])
        self.count += 1
        self.queue[-1][1] += 1
        if self.count < self.k:
            return False
        if self.count > self.k:
            self.count -= 1
            self.queue[0][1] -= 1
            if not self.queue[0][1]:
                self.queue.popleft()
        return len(self.queue) == 1 and self.queue[0][0] == self.value


class DataStream3:

    def __init__(self, value: int, k: int):
        """Just count it -_-|||

        Screw me.

        Ref: https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/discuss/3014963/Python-Just-count-it!

        585 ms, faster than 40.84%
        """
        self.k = k
        self.value = value
        self.count = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.count += 1
        else:
            self.count = 0
        return self.count >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)

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
