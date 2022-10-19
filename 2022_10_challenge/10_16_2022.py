# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from itertools import accumulate


class Solution1:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """LeetCode 1335

        This is the exact same method as the problem yesterday. The answer is
        to insert d - 1 separaters in jobDifficulty, such that the sum of max
        of each intervals reaches min. We can assume that the first separator
        be placed after each val in jobDifficulty, find the current max, and
        recurse on the remaining.

        However, one important trick is to set the right boundary of the
        iteraction of each recurision call to N - rem + 1, because once we go
        beyond that, it is guaranteed that the returned value is inf (this is
        because we will have more days left and the number of jobs).

        Also, we implement a prefix sum to speed up some computation, and
        another check in the loop to facilitate early termination.

        O(N^2 * D), 2121 ms, faster than 45.21%
        """
        N = len(jobDifficulty)
        presum = list(accumulate(jobDifficulty))
        
        @lru_cache(maxsize=None)
        def dp(idx: int, rem: int) -> int:
            # impossible, too many days, not enough jobs
            # impossible, no days left but there is stil jobs
            if N - idx < rem or (rem == 0 and idx < N):
                return math.inf
            if N - idx == rem:  # take one job per day
                return presum[-1] - presum[idx - 1] * int(idx > 0)
            cur_max = -1
            res = math.inf
            for i in range(idx, N - rem + 1):
                cur_max = max(jobDifficulty[i], cur_max)
                if cur_max >= res:
                    break
                res = min(res, cur_max + dp(i + 1, rem - 1))
            return res

        res = dp(0, d)
        return res if res < math.inf else -1


class Solution2:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """This is a O(ND) time complexity solution from lee215

        https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/490316/JavaC%2B%2BPython3-DP-O(nd)-Solution

        It seems like a 1D DP, but it also uses stack to reduce the amount of
        computation.

        We use dp and tmp for the previous and current DP state. dp[i] is the
        min schedule difficulty from 0 to i for the (j - 1)th day. tmp[i] is the
        min schedule difficulty from 0 to i for the jth day.

        Thus, when we are at tmp[i], we first look back at dp[i - 1]. Say we
        take job[i] by itself, then tmp[i] = dp[i - 1] + jobDifficulty[i]

        Then, we consider whether it is possible to group job[i] with any of
        the previous jobs. For each day, we maintain a monotonic decreasing
        stack, which stores the indices of the job with decreasing difficulty.

        We compare jobDifficulty[i] with the tail of the stack. If the tail
        is smaller, then we have the possibility to group all the jobs from
        job[stack[-1]] till job[i], because they will all have the same max
        difficulty, which is jobDifficulty[i]. This might reduce the counting
        of multiple local high job difficulties.

        Once we reach job[stack[-1]] that is larger than jobDifficulty[i], we
        have the possibility to include jobDifficulty[i] into job[stack[-1]].

        Once both conditions are considered, we will have arrived at the min
        schedule difficulty for the current day at job[i]

        O(ND), 59 ms, faster than 99.45%. This is bonkers!!
        """
        N = len(jobDifficulty)
        if N < d:
            return -1
        dp = [math.inf] * N  # schedule difficulty on 0th day
        tmp = [0] * N
        for k in range(d):
            stack = []
            for i in range(k, N):  # after k days, at least k jobs must have been done
                tmp[i] = (dp[i - 1] if i > 0 else 0) + jobDifficulty[i]
                while stack and jobDifficulty[i] >= jobDifficulty[stack[-1]]:
                    j = stack.pop()
                    # group all jobs from j to i together
                    tmp[i] = min(tmp[i], tmp[j] - jobDifficulty[j] + jobDifficulty[i])
                if stack:
                    # include ith job with the stack[-1]th job
                    tmp[i] = min(tmp[i], tmp[stack[-1]])
                stack.append(i)
            dp, tmp = tmp, dp
        return dp[-1] if dp[-1] < math.inf else -1





sol = Solution2()
tests = [
    ([6,5,4,3,2,1], 2, 7),
    ([9,9,9], 4, -1),
    ([1,1,1], 3, 3),
    ([641,915,240,922,191,820,413,871,515,360,78,547,790,335,846,132,344,62,582,159,662,14,614,364,802,981,679,956,831,142,707,391,81,842,365,743,825,849,767,798,841,194,287,720,948,706,559,688,41,63,624,854,788,180,171,316,302,595,684,984,666,914,0,611,451,648,966,100,135,787,942,773,273,426,187,65,161,163,324,207,911,58,334,849,727,380,354,574,223,653,602,879,183,273,904,669,214,434,220,112,176,196,471,736,377,946,279,308,590,646,977,548,995,119,440,365,893,522,604,79,399,484,240,165,64,505,446,257,17,148,825,239,45,491,801,378,513,311,616,263,511,787,944,395,453,949,327,521,701,529,535,988,525,872,299,594,881,258,304,410,162,70,770,630,573,248,226,101,333,814,540,135,609,754,177,656,262,981,80,941,266,742,818,167,764,191,662,179,321,942,389,173,801,637,463,483,984,335,283,400,498,526,59,32,945,914,924,34,637,225,866,61,499,777,110,425,8,777,189,446,505,993,657,992,216,496,522,816,524,587,97,210,807,55,286,556,812,79,161,618,616,990,400,605,91,146,520,59,724,311,935,134,606,737,40,944,101,893,50,438,635,774,360,748,745,571,7,200,288,642,698,411,977,261,839,228,472,938,483,699,682,931,480,710,618,158,775,801,434,816,599,893,314,190,104,720,416,196,515,864], 4, 2079),
    ([749,811,666,27,594,696,572,886,198,761,292,542,257,470,408,145,26,677,34,577,758,175,558,247,493,274,629,436,797,108,306,111,104,435,529,158,73,24,704,646,275,230,301,467,919,446,851,868,971,195,838,799,685,428,942,813,499,756,733,508,823,884,539,137,997,533,236,92,169,708,237,427,546,380,505,902,159,944,802,520,830,550,968,951,991,40,691,212,788,748,906,839,400,367,984,454,171,785,931,841,583,876,490,112,184,97,811,83,465,889,679,203,496,434,342,591,313,940,223,534,737,182,119,331,63,130,459,913,558,418,576,918,472,437,490,805,188,252,447,256,384,464,488,760,943,587,512,316,80,513,542,846,118,56,634,601,380,74,489,667,446,518,106,949,825,126,51,626,285,8,770,302,54,981,699,765,899,996,319,675,908,93,756,151,793,942,68,927,732,353,121,795,359,569,603,195,789,531,84,613,827,647,728,307,469,449,22,161,164,114,367,703,384,979,1000,703,380,533,984,432,906,481,92,123,293,799,63,863,860,255,842,907,293,739,316,699,236,714,475,154], 10, 3295),
    ([972,507,267,699,223,530,365,853,267,294,897,754,402,678,446,235,950,867,46,185,541,555,164,199,262,612,872,238,571,885,327,47,597,70,123,147,321,824,557,616,928,224,409,292,234,69,740,850,703,315,232,102,766,209,100,948,268,120,458,911,168,748,572,951,172,226,603,233,822,750,410,30,891,979,172,574,461,325,860,37,63,266,537,153,499,551,32,463,855,159,646,161,645,776,297,821,531,16,677,848,811,223,792,203,954,78,40,580,976,623,26,51,637,98,309,462,509,21,640,31,87,581,954,415,994,397,807,894,609,993,231,675,109,838,874,635,748,326,933,230,255,363,57,488,145,476,923,282,157,919,504,531,320,539,659,501,22,510,48,405,944,965,455,521,170,59,673,815,27,229,826,379,892,403,598,370,529,909,921,716,194,748,166,12,701,304,828,94,477,576,326,85,446,439,135,154,127,484,333,524,749,466,757,826,802,57,553,525,308,975,254,505,128,261,168,390,810,268,175,994,921,67,453,877,139,721,931,460,67,29,264,355,934,894,263,542,811], 4, 2024),
]

for i, (jobDifficulty, d, ans) in enumerate(tests):
    res = sol.minDifficulty(jobDifficulty, d)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
