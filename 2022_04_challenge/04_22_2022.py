# from pudb import set_trace; set_trace()
from typing import List


class MyHashMap:

    def __init__(self):
        """LeetCode 706

        Exactly the same method as designing a hashset.

        439 ms, faster than 38.87%
        """
        self.M = 1000
        self.hashmap = [[] for _ in range(self.M)]

    def put(self, key: int, value: int) -> None:
        hk = key % self.M
        for it in self.hashmap[hk]:
            if it[0] == key:
                it[1] = value
                return
        self.hashmap[hk].append([key, value])

    def get(self, key: int) -> int:
        hk = key % self.M
        for it in self.hashmap[hk]:
            if it[0] == key:
                return it[1]
        return -1

    def remove(self, key: int) -> None:
        hk = key % self.M
        val = self.get(key)
        if val >= 0:
            self.hashmap[hk].remove([key, val])

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
