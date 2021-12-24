# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
from random import choice, randint


class Solution1:

    def __init__(self, nums: List[int]):
        """Since there is no restriction on the use of the random module, we
        can simply call choice to grab a random index. Of course, we first
        obtain all the indices associated with a number in nums.

        316 ms, 50% ranking.
        """
        self.indices = defaultdict(list)
        for i, n in enumerate(nums):
            self.indices[n].append(i)

    def pick(self, target: int) -> int:
        return choice(self.indices[target])


class Solution2:

    def __init__(self, nums: List[int]):
        """Reservoir sampling. Here is my understanding of it.

        Given a stream of numbers for which the size is unknown. We want to
        randomly pick the index of a target value. We can loop through the
        stream to obtain the count of the target value. The question is how to
        randomly pick one index out of the count WITHOUT incurring any space
        overhead in the solution.

        Consider nums = [1, 2, 3, 3, 3] and target = 3
        Let's say we want to return index 4. The only way to do so is to wait
        until index 4 is encountered, at which time we will have count = 3.
        Thus, we only need to produce a probability of 1/3, and the index 4
        will have the probably of 1/3.

        If we want to have index 3 be picked. The first time it is picked, we
        have count = 2. Thus, the probability is 1/2 at the moment. Next round
        we have count = 3. Our rule of picking is that we will always pick a
        larger index as we loop forward. Thus at the current moment, the only
        other index we can pick is 4. So want to avoid picking 4. The
        probability of picking 4 is 1/3, as described in the previous paragraph
        Therefore, the probability of not picking 4 is 1 - 1/3 = 2/3. Thus,
        over the two rounds, the probability of keeping the index = 3 is 1/2 *
        2/3 = 1/3. MAGIC!

        If we want to have index 2 be picked. The first time it is pickeed, we
        have probability 1. The second time, we have count = 2. And the
        probability of index 3 is picked is 1/2. Thus the probability of 1 still
        being picked is 1 - 1/2 = 1/2. The third time we have count = 3. And
        the probability of index 4 is picked is 1/3. Thus the probability of 1
        still being picked is 1 - 1/3 = 2/3. Thus, the overall probability of
        1 being picked over the three rounds is 1 * 1/2 * 2/3 = 1/3. MAGIC!!

        Hence, reservoir sampling works. Although, since there is no memory
        requirement in this problem, it is not really necessary.

        276 ms, 96% ranking.

        But the major improvement is the space. This one uses 18.2 MB, whereas
        Solution1 requires 23.7 MB.
        """
        self.nums = nums

    def pick(self, target: int) -> int:
        count, res = 0, -1
        for i, n in enumerate(self.nums):
            if n == target:
                count += 1
                if randint(1, count) == 1:  # producing probability of 1/count
                    # If 1/count is hit, we have a new index.
                    # Otherwise, there is 1 - 1/count probability that a
                    # previously picked index remains
                    res = i
        return res
        


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
