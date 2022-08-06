# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """LeetCode 458

        This problem is tough because it is difficult to parse.

        The first key to understnd the problem is that one pig can drink any
        number of buckets at once and any number of pigs can drink from one
        bucket.

        With that in mind, the problem is equivalent to finding the total
        number of states that can be created with the number of tests. If this
        value is larger or equal to the number of buckets, then we are able
        to assign a unique state to the bucket, and can identify which bucket
        is poisonous when its assigned state has dead pigs.

        To put it in another way, a state is equivalent to a feeding state of
        all pigs. Given one test, a pig has two feeding states: not feeding or
        feeding. Given two tests, a pig has three feeding states: not feeding,
        feeding once, or feeding twice. Thus, given t tests, a pig has t + 1
        number of feeding states. That means, given x pigs with t tests, we
        can have (t + 1)^x number of feeding states. All of these feeding
        states are unique. And that is the total number of states we can have.

        Then the problem is to find the smallest x such that (t + 1)^x >= n,
        where n is the number of buckets.

        It's more of a mind twister. Once it clicks, it's an easy problem. But
        it took me great effort to find the click.

        52 ms, faster than 36.50%
        """
        return math.ceil(math.log(buckets) / math.log(minutesToTest // minutesToDie + 1))


sol = Solution()
tests = [
    (1000, 15, 60, 5),
    (4, 15, 15, 2),
    (4, 15, 30, 2),
]

for i, (buckets, minutesToDie, minutesToTest, ans) in enumerate(tests):
    res = sol.poorPigs(buckets, minutesToDie, minutesToTest)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
