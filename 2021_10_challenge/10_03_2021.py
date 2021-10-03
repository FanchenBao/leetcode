# from pudb import set_trace; set_trace()
from typing import List


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


class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        """LeetCode 55

        I use a segment tree to check whether it is possible to go from any
        position to the end. For instance, given nums[i] = 2, I check whether it
        is possible to go from i + 1 or i + 2 towards the end. If any of these
        two positions allows access to the end, it is possibe to go from i to the
        end.

        This requires a query of a range [i + 1, i + 2]. More generically, for
        any i, we need to query [i + 1, min(i + nums[i], n - 1)]. A segment tree
        can perform such query and update in log(N) time. I use the binary
        indexed tree implementation for simplicity reason.

        O(NlogN) time complexity, 2072 ms, 16% ranking.
        """
        n = len(nums)
        bit = BIT(n)
        bit.update(n - 1, 1)  # last position, always reachable from itself
        for i in range(n - 2, -1, -1):
            if bit.query(min(i + nums[i], n - 1)) - bit.query(i) > 0:
                bit.update(i, 1)
            else:
                bit.update(i, 0)
        return bit.query(0) > 0


class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        """Greedy. Going backwards in nums, trying to find the latest, the last
        position i such that access to the end is possible. There can be many
        positions that allow access to the end, but if we identify i, then we
        automatically include all the other positions, because if any position
        before i can reach the end, then those positions can also reach the end
        through i.

        We keep finding the last position until we reach the beginning. If the
        first element is also the last position to reach the end, we say the
        jump game is possible.

        I got this solution from my previous attempt in May 2019.

        O(N), 464 ms, 90% ranking.
        """
        n = len(nums)
        last = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0


class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        """A better implementation of the greedy idea.

        Ref: https://leetcode.com/problems/jump-game/discuss/1500445/don't-make-question-difficult-using-dp-orT.C.-greaterO(n)S.C.-greatero(1)-or-c%2B%2Bor-greedyor-code-with-explanation-.

        The idea is to find out the max position reachable from the current
        position. As we traverse through nums, the max position reachable
        directly from i is i + nums[i]. But, it is also possible that the
        positions prior to i can have a longer reach. Thus, the max reach at i
        is max(pre_reach, i + nums[i]). It is possible that the previous reach
        cannot reach i. In this case, we should have encountered this situation
        when such previous reach is encountered. Say pre_reach is i - 1, which 
        doesn't reach i. Then we should have handled this situation at position
        i - 1. If i - 1 + nums[i - 1] > i - 1 (i.e. nums[i - 1] != 0), then our
        pre_reach would've increased to beyond i - 1. The only reason that it
        does not increase is that we are stuck at i - 1. And we can check it by
        examining whether the max reach at i - 1 is equal to i - 1.
        """
        reach, n = 0, len(nums)
        for i, num in enumerate(nums):
            reach = max(reach, i + num)
            if reach == i and i != n - 1:
                return False
        return True


sol = Solution3()
tests = [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([0], True),
    ([3, 2, 1, 0], True),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.canJump(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
