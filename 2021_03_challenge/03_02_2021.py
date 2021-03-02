# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """LeetCode 645

        A set solution. We recognize the repeat by pushing the value in nums
        into a set. We identify the missing value using set difference.

        O(N), 184 ms, 89% ranking.
        """
        num_set = set()
        repeat = None
        for n in nums:
            if n in num_set:
                repeat = n
            num_set.add(n)
        return [repeat, list(set(range(1, len(nums) + 1)) - num_set)[0]]


class Solution2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """A bucket solution. We initialize all values in the bucket as -1. As
        we iterate through nums, we increment the bucket whose index corresponds
        to the value in nums. Eventually, the missing one has the bucket value
        still as -1, and the repeat has its value as 1.

        O(N), 192 ms, 74% ranking.
        """
        buckets = [-1] * 10000
        for n in nums:
            buckets[n - 1] += 1
        return [buckets.index(1) + 1, buckets.index(-1) + 1]


class Solution3:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """My O(1) space solution, which involves swapping num with
        nums[num - 1]. We keep swapping, which essentially puts each number in
        its correct position, until we hit a situation where num has already
        been put in the correct position. That number is the repeat. We also set
        the value to -1 when we identify a mismatch. Eventually, all the numbers
        shall be in place, except the -1.

        The only tricky part is that -1 could become the target for swapping.
        This will lead to infinite loop. So we must not allow target value to be
        negative.

        O(N), 200 ms
        """
        repeat = None
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                target = nums[i]
                nums[i] = -1
                while target > 0 and nums[target - 1] != target:
                    nums[target - 1], target = target, nums[target - 1]
                if target > 0:
                    repeat = target
        return [repeat, nums.index(-1) + 1]


class Solution4:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """This is the official solution for O(1) space. Pretty smart. We
        use inversion to indicate which num has been encountered. Thus, if a num
        sees that its corresponding value has already been inverted, that num
        must be the repeat. For finding the missing one, the position where the
        num has not been inverted, i.e. still positive, must represent the
        missing value.

        O(N), 216 ms
        """
        repeat, missing = None, None
        for n in nums:
            if nums[abs(n) - 1] < 0:
                repeat = abs(n)
            else:
                nums[abs(n) - 1] *= -1
        for i, n in enumerate(nums):
            if n > 0:
                missing = i + 1
                break
        return [repeat, missing]


sol = Solution4()
tests = [
    ([1, 2, 2, 4], [2, 3]),
    ([1, 1], [1, 2]),
    ([3, 2, 2], [2, 1]),
    ([3, 2, 3, 4, 5, 6], [3, 1]),
    ([4, 2, 2, 1], [2, 3]),
    ([8, 7, 3, 5, 3, 6, 1, 4], [3, 2]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findErrorNums(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
