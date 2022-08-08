# from pudb import set_trace; set_trace()
from typing import List
from random import randint


class Solution0:
    def totalSteps(self, nums: List[int]) -> int:
        queue = nums
        res = 0
        while queue:
            temp = []
            for i, n in enumerate(queue):
                if i == 0 or n >= queue[i - 1]:
                    temp.append(n)
            if len(queue) == len(temp):
                break
            queue = temp
            res += 1
        return res


class Solution1:
    def totalSteps(self, nums: List[int]) -> int:
        """This is a very convoluted logic.

        1. We use an aux array to store two pieces of information about each
        val. First, the index of the first peak to the left of the value that
        is larger than it. Second, the number of steps needed to remove the val
        We store these two values as a list of length two, and always append it
        to aux array.

        2. Start from the begining of nums and look for the first peak. We know
        that all the values leading up to the peak, including the peak, will
        not be removed. All the non-removed values will have their aux entry
        being [i, 0], which means they are their own largest peak to the left,
        and it takes 0 step to remove them.

        3. The first time that value drops, we record it in aux as [i - 1, 1],
        which means the first peak to its left that is larger than it has index
        i - 1, and it takes 1 step to remove the value.

        4. Now, the more complex logic kicks in. We iterate through the
        remainder of the array. Consider each of the four scenarios below.
            a. nums[j] < nums[j - 1] < nums[j - 2]: a continuous downtrend.
            This means nums[j] will be removed in the same step as nums[j - 1].
            Thus, it has the same aux entry as aux[j - 1]
            b. nums[j] < nums[j - 1] but nums[j - 1] >= nums[j - 2]:
            nums[j - 1] is a peak or extending a peak. In this case,
            nums[j - 1] is the first peak to the left of nums[j] that is larger
            than it, hence aux[-1][0] = j - 1. And, since nums[j - 1] is a peak
            our step count must reset to 1. Hence aux[-1][1] = 1.
            c. nums[j] == nums[j - 1]: we are extending whatever happens before
            Apparently, nums[j] and nums[j - 1] has the same peak to the left
            that is larger than it. So aux[-1][0] = aux[j - 1][0]. With regards
            to the number of steps, it depends on whether nums[j - 1] gets
            removed. If it is not removed, then neither will nums[j]. However,
            if it is removed, then nums[j] must be removed after nums[j - 1].
            Hence, aux[-1][1] = 0 if aux[j - 1][1] == 0 else aux[j - 1][1] + 1
            d. nums[j] > nums[j - 1]: this is the most complex logic. The
            current val is bigger than the previous. We have two scenarios. The
            trivial one is that nums[j] is smaller than the previous peak of
            nums[j - 1], then nums[j] will have the same previous peak as
            nums[j - 1], and its step count will be the step count of
            nums[j - 1] plus one. However, if nums[j] is larger than the
            previous peak of nums[j - 1], then we must keep searching for the
            previous peak of the previous peak of nums[j - 1]. We must keep
            this search, until we either find a previous peak that is larger
            than nums[j] or end up with a previous peak that is not removable.
            If it's the latter situation, that means nums[j] is also not
            removable. If its the former situation, we have located the previous
            peak. With regards to the number of steps, each time we progress
            towards a new previous peak, the current val we compare to has the
            potential to be the exact value that is removed right before
            nums[j]. Thus, we need to update the step count of nums[j] with
            the step count of each val compared to, and keep track of the max
            steps along the way.

        1726 ms, faster than 22.82%
        """
        aux = [[0, 0]]  # ele = [index of previous peak larger than me, number of steps to remove me]
        N = len(nums)
        for i in range(1, N):
            if nums[i] < nums[i - 1]:
                break
            aux.append([i, 0])
        else:
            return 0
        aux.append([i - 1, 1])
        res = 1
        for j in range(i + 1, N):
            if nums[j] < nums[j - 1] < nums[j - 2]:
                aux.append(aux[-1])
            elif nums[j] < nums[j - 1] and nums[j - 1] >= nums[j - 2]:
                aux.append([j - 1, 1])
            elif nums[j] == nums[j - 1]:
                aux.append(aux[-1] if aux[-1][1] == 0 else [aux[-1][0], aux[-1][1] + 1])
            elif nums[j] > nums[j - 1]:
                pre_peak_idx = aux[-1][0]
                aux.append([-1, aux[-1][1] + 1])
                while nums[j] > nums[pre_peak_idx]:
                    aux[-1][1] = 0 if aux[pre_peak_idx][1] == 0 else max(aux[-1][1], aux[pre_peak_idx][1] + 1)
                    if pre_peak_idx == aux[pre_peak_idx][0]:
                        aux[-1][0] = j
                        break
                    else:
                        pre_peak_idx = aux[pre_peak_idx][0]
                if aux[-1][0] < 0:  # not set yet
                    if nums[j] == nums[pre_peak_idx]:
                        aux[-1][0] = aux[pre_peak_idx][0]
                        aux[-1][1] = 0 if aux[pre_peak_idx][1] == 0 else max(aux[-1][1], aux[pre_peak_idx][1] + 1)
                    else:
                        aux[-1][0] = pre_peak_idx
            res = max(res, aux[-1][1])
        return res


class Solution2:
    def totalSteps(self, nums: List[int]) -> int:
        """lee215's solution
        Ref: https://leetcode.com/problems/steps-to-make-array-non-decreasing/discuss/2085864/JavaC%2B%2BPython-Stack-%2B-DP-%2B-Explanation-%2B-Poem

        My solution is quite close, despite being a lot more verbose. But his
        solution helps me understand the problem better. What is clear is that
        the difficult part is always having a value larger than some previous
        values. To figure out what to do with such value, we must find a
        previous peak that is larger than the current val. In my solution, I
        use some pointers to keep track of each value's previous peak. But this
        can be more easily achieved via monotonic stack, in particular, mono-
        tonic decreasing stack.

        Given nums[i] and a monotonic decreasing stack. As long as nums[i] is
        larger or equal to the end of the stack, we can be sure that nums[i]
        must be popped after the end of the stack. Thus we keep popping the
        stack, and keeping track of the largest number of steps needed to
        remove any of the popped value. We stop until the end of the stack is
        larger than the current value. This means the current value must be
        removed after all the values in between stack[-1] and nums[i] have been
        removed. And since we have kept track of the max number of steps needed
        to remove all the values that have just been popped, we know that to
        remove nums[i], we must use max_steps + 1 step. The beauty of this
        approach is also that if we pop everything in the stack, then nums[i]
        must be the largest value so far, which means it can never be popped.
        On the other hand, if nums[i] is immediately smaller stack[-1] without
        any popping, then we know nums[i] must be removed in the first step,
        because without popping, nums[i] and stack[-1] are adjacent.

        O(N), 1169 ms, faster than 71.33%
        """
        steps = [0] * len(nums)
        stack = []
        for i, n in enumerate(nums):
            cur_steps = 0
            while stack and n >= nums[stack[-1]]:
                cur_steps = max(cur_steps, steps[stack.pop()])
            if stack:  # n must be removed. Otherwise, n will not be removed
                steps[i] = cur_steps + 1
            stack.append(i)
        return max(steps)


sol0 = Solution0()
sol = Solution2()
num_tests = 100
l = 100
max_val = 1000
tests = [[randint(1, max_val) for _ in range(l)] for _ in range(num_tests)]
# tests = [
#     (20, 10, 16, 2, 8, 8, 16),
# ]
# tests = [
#     ([5,3,4,4,7,3,6,11,8,5,11], 3),
#     ([4,5,7,7,13], 0),
#     ([6, 10, 10, 2, 3], 2),
#     ([7, 4, 1, 8, 10], 1),
#     ([10, 5, 10, 9, 10], 1),
#     ([9, 3, 10, 9, 2], 1),
#     ([9, 1, 5, 10, 9], 2),
#     ([1, 6, 8, 4, 9], 1),
#     ([6, 1, 1, 10, 10], 2),
#     ([4, 5, 2, 1, 7], 1),
#     ([5, 1, 9, 3, 7], 2),
#     ([6, 8, 5, 7, 1], 2),
#     ([1, 4, 3, 3, 5, 10, 3, 6, 2, 1], 2),
#     ([10, 9, 7, 2, 1, 2, 5, 6, 9, 8], 5),
#     ([4, 1, 2, 6, 4, 1, 9, 3, 9, 1], 2),
#     ([1, 1, 5, 10, 5, 8, 6, 2, 9, 7], 3),
#     ([5, 10, 8, 2, 4, 6, 9, 7, 7, 7], 4),
#     ([9, 2, 9, 7, 3, 3, 10, 2, 9, 9], 3),
#     ([4, 9, 1, 5, 3, 2, 7, 6, 2, 6], 3),
#     ([2, 9, 10, 6, 8, 3, 8, 9, 7, 10], 4),
#     ([7, 8, 10, 4, 7, 8, 10, 2, 10, 6], 3),
#     ([7, 7, 3, 5, 5, 7, 10, 5, 4, 8], 3),
# ]

for i, nums in enumerate(tests):
    ans = sol0.totalSteps(nums)
    res = sol.totalSteps(nums)
    if res != ans:
        print(f'Test: {tests[i]}; Fail. Ans: {ans}, Res: {res}')
