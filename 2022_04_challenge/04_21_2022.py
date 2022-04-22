# from pudb import set_trace; set_trace()
from typing import List


class MyHashSet:

    def __init__(self):
        """LeetCode 705

        There are many ways to implement a good hash function. But for the
        purpose of this problem, I chose the easiest hash function, which is
        modulo. And we use the built-in functions to handle the search and
        replace operations.

        177 ms, 86.63%
        """
        self.M = 1000
        self.hash = [[] for _ in range(self.M)]

    def add(self, key: int) -> None:
        hk = key % self.M
        if key not in self.hash[hk]:
            self.hash[hk].append(key)

    def remove(self, key: int) -> None:
        hk = key % self.M
        if key in self.hash[hk]:
            self.hash[hk].remove(key)

    def contains(self, key: int) -> bool:
        hk = key % self.M
        return key in self.hash[hk]


sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
