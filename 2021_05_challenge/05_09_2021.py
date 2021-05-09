# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        """LeetCode 1354

        We solve this problem in reverse. We find the largest value in target
        and figure out how can we reach it. The only way to reach the largest
        value is that in the previous round, the value sitting at the same
        position as the current largest value is cur_max - (sum - cur_max). Let
        us call sum - cur_max = remain and cur_max - remain = r. If r is larger
        than 0, then we can replace current largest with r and repeat the same
        procedure for the next step. Otherwise, we declare that it is impossible

        We tried this straightforward solution, but got TLE for this test case
        [1, 1000000]

        Apparently, by performing cur_max - remain every single time, we are
        wasting resources because cur_max can be gigantic, while remain is very
        small. In this case, each time cur_max - remain happens, we will end
        up with an r that is still the max of the next iteration. So essentially
        what we need is to compute cur_max % remain. This way, we can directly
        arrive at an r that can save a lot of iterations.

        However, there are tricky edge cases. First of all, if remain == 1, then
        cur_max % remain = 0, which technically speaking is a failed case, since
        we cannot replace any value in target with 0. However, remain == 1 is
        a special case which only happens when there are two elements in target.
        And whenever one of the two elements is 1, it is immediately possible.

        Another edge case is when remain = 0, which can happen when target is of
        length 1 and the element is not 1. In this case, we will endter the
        while loop but end up with remain = 0. This is an impossible case.

        Once these two edge cases and the mod operation is used, the problem is
        solved.

        O(Nlog(N)), 248 ms, 84% ranking.

        NOTE: the post by lee215 is definitely worth reading.

        https://leetcode.com/problems/construct-target-array-with-multiple-sums/discuss/510256/JavaC%2B%2BPython-Backtrack-OJ-is-wrong

        Apparently, the problem was not well configured initially, missing test
        cases and TLE for brute force solution. The test cases I got hit was
        suggested by him, so much kudos to him.

        Another interesting thing is about the run time. I say it is Nlog(N)
        based on a ballpark estimation. Lee215 said it is N + log(maxA)log(N),
        O(N) is to build the heap queue. Log(N) is heap push and pop. These are
        fine. The last part log(maxA) is the number of times the while loop runs
        The reasoning is that this process is similar to gcd function, which
        always pick the current largest and reduce it to a remainder. According
        to lee215, gcd runs at log(maxA) time, thus the while loop in the
        solution also runs log(maxA) times. I am convinced.
        """
        s = sum(target)
        mod_target = [-t for t in target]
        heapq.heapify(mod_target)
        while mod_target[0] != -1:
            cur_max = -heapq.heappop(mod_target)
            remain = s - cur_max
            if remain == 1:
                return True
            if remain >= cur_max or remain == 0:
                return False
            r = cur_max % remain
            if r == 0:
                return False
            heapq.heappush(mod_target, -r)
            s = remain + r
        return True


sol = Solution()
tests = [
    ([9, 3, 5], True),
    ([1, 1, 1, 2], False),
    ([8, 5], True),
    ([1, 100000000], True),
    ([2], False),
]

for i, (target, ans) in enumerate(tests):
    res = sol.isPossible(target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
