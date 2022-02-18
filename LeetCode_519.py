# from pudb import set_trace; set_trace()
from typing import List
from random import randint


class Solution1:

    def __init__(self, m: int, n: int):
        """The key is to NOT set up a matrix, which saves A LOT OF memory. Plus
        we don't need the matrix anyway.

        We also don't need to use the pop-the-index-array method, because the
        flip call is at most 1000, which means even if we have to do repeated
        random call, it won't cause too much time. Thus, the solution is to
        use a set to keep all the indices that have been flipped already. Just
        randomly select a value until it is not in the flipped set. The reset
        is as simple as setting the flipped set to an empty set.

        82 ms, 46% ranking.
        """
        self.m = m
        self.n = n
        self.total = m * n
        self.flipped = set()

    def flip(self) -> List[int]:
        while True:
            idx = randint(0, self.total - 1)
            if idx not in self.flipped:
                break
        self.flipped.add(idx)
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        self.flipped = set()


class Solution2:

    def __init__(self, m: int, n: int):
        """Similar idea as popping the end of a list, but without actually
        having to set up the list (setting up such list leads to memory limit
        exceed error). We use a hashmap to keep track of the element that is
        swapped from the tail. For the other element in the list, if it has
        not been subject to swap, the value will stay the same as the index.

        Ref: https://leetcode.com/problems/random-flip-matrix/discuss/154053/Java-AC-Solution-call-Least-times-of-Random.nextInt()-function

        74 ms, 52% ranking.
        """
        self.m = m
        self.n = n
        self.last = m * n - 1
        self.mapList = {}

    def flip(self) -> List[int]:
        idx = randint(0, self.last)
        self.last -= 1
        res = self.mapList.get(idx, idx)  # swapped out
        self.mapList[idx] = self.mapList.get(self.last, self.last)  # swapped in
        return [res // self.n, res % self.n]

    def reset(self) -> None:
        self.mapList = {}
        self.last = self.n * self.m - 1


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
