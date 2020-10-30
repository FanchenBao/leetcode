# from pudb import set_trace; set_trace()
from typing import List, Tuple


class Solution1:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """27% ranking.

        Very tough for me. I have to first revisit how LIS algorithm works, and
        then based on that, I have to figure out how to keep track the total
        number of LIS ending at each position.

        Two arrays, L and C, recording the max length and number of LIS at each
        position. As we go through the inner loop, the rule of updating L is the
        same as the traditional LIS problem: we pick the largest L[j] + 1.
        In addition, we also need to update the C array, which copies C[j] to
        C[i] because when the LIS is extended from position j, the total number
        of LIS remains the same as when it is at position j.

        When L[j] + 1 is equal to L[j], that means by extending from j, you
        get the same max length as what you have right now at position i. In
        this case, the total number of LIS ending at position i shall be the
        sum of C[i] and C[j].

        At the end, we first find max length, then look for the counts in C at
        the same location where max length is achieved in L. We sum them up
        as our result.
        """
        if not nums:
            return 0
        L, C = [1] * len(nums), [1] * len(nums)
        for i, n in enumerate(nums):
            for j in range(i):
                if n > nums[j]:
                    if L[j] + 1 > L[i]:
                        L[i], C[i] = L[j] + 1, C[j]
                    elif L[j] + 1 == L[i]:
                        C[i] += C[j]
        max_len = max(L)
        return sum(C[k] for k, l in enumerate(L) if l == max_len)



class SegNode:
    def __init__(self, rl, rr):
        self.val = (0, 1)
        self.rl = rl
        self.rr = rr
        self.rm = (self.rl + self.rr) // 2
        self._left = self._right = None

    # Dynamically create left or right. This is super important because
    # otherwise, the algorithm times out due to creating the entire segment
    # tree.
    @property
    def left(self):
        self._left = self._left or SegNode(self.rl, self.rm)
        return self._left

    @property
    def right(self):
        self._right = self._right or SegNode(self.rm + 1, self.rr)
        return self._right


def merge(v1: Tuple, v2: Tuple) -> Tuple:
    """Merge two (length, count) of adjacent ranges. Note that the length is the
    LIS from the beginning of the input numbers till some number within the
    range denoted by the node thta holds the tuple. Length is NOT the length of
    LIS contained within the range denoted by the node.

    For instance, for a range [3, 6], if the length is 6, that means the LIS
    starting from the beginning of the numbers, which apparently is outside of
    the range [3, 6], and ending in range [3, 6] is of length 6.
    """
    if v1[0] == v2[0]:
        return (v1[0], v1[1] + v2[1]) if v1[0] else (0, 1)
    else:
        return max(v1, v2)


def insert(node: SegNode, key: int, val: Tuple) -> None:
    """Insert a val, which is the length and count of LIS that ends with key
    into the given node.
    """
    if node.rl == node.rr:
        node.val = merge(val, node.val)
    else:
        if node.rm >= key:
            insert(node.left, key, val)
        else:
            insert(node.right, key, val)
        node.val = merge(node.left.val, node.right.val)


def query(node: SegNode, key: int) -> Tuple:
    """Query the segment tree to get the legnth and count of LIS within the
    range denoted by the node
    """
    if node.rr <= key:
        return node.val
    if node.rl > key:
        return (0, 1)
    return merge(query(node.left, key), query(node.right, key))


class Solution2:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        root = SegNode(min(nums), max(nums))
        for n in nums:
            length, count = query(root, n - 1)
            insert(root, n, (length + 1, count))
        return root.val[1]


sol = Solution2()
tests = [
    ([1, 3, 5, 4, 7], 2),
    ([2, 2, 2, 2, 2], 5),
    ([1, 2, 3, 4, 1, 2, 3, 4, 5], 5),
    ([1, 2, 1, 2], 3),
    ([1, 2, 3, 1, 2], 1),
    ([1, 2, 3, 1, 2, 3], 4),
    ([1, 2, 3, 1, 2, 3, 4], 4),
    ([1, 2, 4, 3, 5, 4, 7, 2], 3),
    ([1, 1, 1, 2, 2, 2, 3, 3, 3], 27),
    ([100, 90, 80, 70, 60, 50, 60, 70, 80, 90, 100], 1),
    ([1, 2], 1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findNumberOfLIS(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
