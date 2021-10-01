# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """LeetCode 698

        I think this is quite a complex problem. First of all, we can easily
        eliminate the impossible cases. There are two types of impossible cases
        1. The total sum divided by k is not an integer.
        2. The largest value in nums is larger than target

        We make sure that nums is sorted, then we will start from the largest
        value going downwards. For each large value, we find all possible states
        that can form our target with such large value. After that, we go
        through each of the state, and find the next large value and produce
        all the states that allow the next large value to accumulate to the
        target. We keep doing this for k times until we encounter two scenarios
        1. For the next large value, there is no state that can accumulate to
        the target with the next large value. When this happens, we can return
        False immediately.
        2. We go through all k rounds and there are still valid states left. In
        this case, we return True.

        Now, the algo to find all the states that allows a large value to form
        the target is a DFS. We can use backtrack, but that feels cumbersome.
        Given that the length of the array is only 16, we can use a bit mask to
        serve as the state. So each dfs call will return a list of bit masks
        representing the current state where the large value can sum up with
        some small values to reach the target.

        From the outside, this solution looks like a combination of DFS and BFS.
        But the BFS is not the critical part. The DFS is. And using bit mask to
        represent state greatly simplifies the DFS procedure, i.e. we don't have
        to backtrack. We can keep the original state intact.

        No idea the time complexity, but it feels O(2^N) to me. (UPDATE: the
        actual time complexity is O(2^N * N))

        62 ms, 59% ranking.
        """
        nums.sort()
        n, total = len(nums), sum(nums)
        target = total // k
        if target * k != total or nums[-1] > target:
            return False

        def dfs(state, idx, target) -> List[int]:
            if target == 0:
                return [state]
            if target < 0:
                return []
            res = []
            for j in range(idx, -1, -1):
                if state & (1 << (n - 1 - j)) == 0:
                    res.extend(dfs(state | (1 << (n - 1 - j)), j - 1, target - nums[j]))
            return res

        queue = [0]
        for _ in range(k):
            temp = []
            for state in queue:
                for i in range(n - 1, -1, -1):
                    if state & (1 << (n - 1 - i)) == 0:
                        break
                temp.extend(dfs(state | (1 << (n - 1 - i)), i - 1, target - nums[i]))
            if not temp:
                return False
            queue = temp
        return True


class Solution2:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """This solution came from

        https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/1494999/C%2B%2BJavaPython-Top-down-DP-Bitmask-Clean-and-Concise

        Very smart solution. We ask this simple question, if nums[i] is the last
        number to add to some subset, what is the requirement of the other
        numbers? They must form k - 1 targerts with the remaining value being
        exactly targt - nums[i]. Thus, to find out whether all nums can be
        partitioned into k subsets, we can check the remaining numbers by taking
        nums[i] out and see if any remaining numbers can satisfy the requirement
        mentioned above. In other words, given current state 11111, we are
        checking the viability of 11110, 11101, 11011, 10111, and 01111. This
        process can recurse until our state becomes 00000, i.e. no number is
        involved. The viability check is to see whether the remaining value
        after partition for each state can allow the addition of nums[i].

        O(2^N * N)
        """
        n, total = len(nums), sum(nums)
        target = total // k
        if target * k != total or nums[-1] > target:
            return False

        @lru_cache(maxsize=None)
        def dp(state: int) -> int:
            if state == 0:
                return 0
            for i in range(n):
                if (state >> i) & 1:
                    # try to add nums[i] to create the current state
                    remains = dp(state ^ (1 << i))
                    if remains >= 0 and remains + nums[i] <= target:
                        # we can add nums[i] to create the current state
                        # Note that we can return here immediately when a
                        # possible partition is found. This is because the
                        # return value of dp is the sum of all numbers in the
                        # state mod target. So as long as a valid partition
                        # is available, the return value is always the same
                        return (remains + nums[i]) % target
            return -1

        return dp((1 << n) - 1) != -1


sol = Solution2()
tests = [
    ([4, 3, 2, 3, 5, 2, 1], 4, True),
    ([1, 2, 3, 4], 3, False),
    ([2, 2, 2, 2, 3, 4, 5], 4, False),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.canPartitionKSubsets(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
