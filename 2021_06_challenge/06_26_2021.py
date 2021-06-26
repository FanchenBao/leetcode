# from pudb import set_trace; set_trace()
from typing import List
from random import randint
import math


class Solution0:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    count[i] += 1
        return count


class SegTree:
    def __init__(self, N: int):
        self.st = [0] * (2 * N)

    def update(self, node: int, num: int, lr: int, rr: int) -> None:
        if lr == rr:
            self.st[node] += 1
            return
        mid = (lr + rr) // 2
        if num <= mid:
            self.update(node * 2, num, lr, mid)
        else:
            self.update(node * 2 + 1, num, mid + 1, rr)
        self.st[node] = self.st[node * 2] + self.st[node * 2 + 1]

    def query(self, node: int, lr: int, rr: int, xl: int, xr: int) -> int:
        if xl > xr:
            return 0
        if xl == lr and xr == rr:
            return self.st[node]
        mid = (lr + rr) // 2
        if xr <= mid:
            return self.query(node * 2, lr, mid, xl, xr)
        elif xl > mid:
            return self.query(node * 2 + 1, mid + 1, rr, xl, xr)
        else:
            return self.query(node * 2, lr, mid, xl, mid) + self.query(node * 2 + 1, mid + 1, rr, mid + 1, xr)


class Solution1:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """LeetCode 315

        Very difficult for me. I have to rely on the solution. Here is the
        reference:

        https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/1298226/Easy-Solution-w-Explanation-or-Segment-Tree-and-Binary-Indexed-Tree-Approach

        I thought about segment tree, but didn't puruse because my understanding
        of segment tree is not correct. I was trying to use indices as proxy for
        range, and that went nowhere. The correct way is to use the actual
        values of the element in nums as the range. Then we can ask the right
        question: given a value n, how many numbers are there in the range n - 1
        to min of nums. This is a segment tree problem.

        But then, when I tried to build the segment tree, I got blocked again,
        despite the fact that I have built segment tree before on my own. I got
        stuck by two concepts. The first is that in an array implementation of
        segment tree, each node does not inherently contain the information of
        the range it represents. Therefore, we must pass the range of each node
        in the argument. And that range value has nothing to do with the indices
        of the array representation of the segment tree.

        The second block is the size of the segment tree. I thought given the
        range size of N, we only need 2 * N - 1 nodes. It is true, if we do not
        use the array implementation. For array implementation of a tree, the
        tree must be complete. Therefore, the size of the array must accommodate
        the smallest complete binary tree that holds the segment tree. The
        formula is 2^(log2(N) + 1).

        O(Nlog(N)), 6612 ms, 6% ranking.
        """
        min_n, max_n = min(nums), max(nums)
        N = max_n - min_n + 1
        ST = SegTree(2**(math.floor(math.log2(N)) + 1))
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            ST.update(1, nums[i], min_n, max_n)
            res[i] = ST.query(1, min_n, max_n, min_n, nums[i] - 1)
        return res


class BIT:
    def __init__(self, N: int):
        """Initialize a binary indexed tree.

        :param N: The size of the range, including min and max.
        """
        # use 1-based BIT, thus array size must be one larger than the range.
        self.bit = [0] * (N + 1)

    def update(self, pos: int, delta: int) -> None:
        """Update the value at `pos` by adding `delta`.

        Also update all the other ranges that contain `pos`.

        :param pos: The position inside a range whose value needs to be
            updated. Note that this position is one less than the index
            of the self.bit array.
        :param delta: The additional value that needs to be added to
            the value at the given position, and all the other ranges
            including the given position.
        """
        # KEY POINT: BIT index is 1-based, thus its index is one larger
        # than the given position.
        i = pos + 1
        while i < len(self.bit):
            self.bit[i] += delta
            i += (i & -i)

    def query(self, max_r: int) -> int:
        """Query the sum of values in the range 0 to `max_r`.

        The meaning of "values" us defined by the `delta` parameter
        in self.update(). It is not necessarily prefix sum.

        :param max_r: The end of the range which we want to query.
        :return: Sum of values in the range 0 to `max_r`.
        """
        # KEY POINT: Bit index is 1-based, thus its index is one larger
        # than the given max range.
        i, res = max_r + 1, 0
        while i:
            res += self.bit[i]
            i -= (i & -i)
        return res


class Solution2:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """Binary Indexed Tree solution.
        """
        max_n = 10**4
        bin_id_tree = BIT(2 * max_n)
        res = [0] * len(nums)
        for i in range(len(nums) - 1, - 1, -1):
            bin_id_tree.update(nums[i] + max_n, 1)
            res[i] = bin_id_tree.query(nums[i] + max_n - 1)
        return res


sol0 = Solution0()
sol = Solution2()
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
length = 4
num_test = 10
tests = [[randint(1, 10) for _ in range(length)] for _ in range(num_test)]

# tests = [[6, 1, 9, 10]]

for i, test in enumerate(tests):
    res = sol.countSmaller(test)
    ans = sol0.countSmaller(test)
    if res != ans:
        print(f'Fail. {ans=}, {res=}, {test=}')
