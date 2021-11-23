# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter, defaultdict


class DSU:
    """Disjoint Set Union.

    It supports union and find in log(N) time. It has rank and path compression.
    Shamelessly copied from:

    https://leetcode.com/problems/swim-in-rising-water/discuss/1284843/Python-2-solutions%3A-Union-FindHeap-explained

    Update 06/25/2021: Improved functionality by returning boolean value in
    self.union function. Reference:

    https://leetcode.com/problems/redundant-connection/solution/
    """

    def __init__(self, N: int):
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        xr, yr = self.find(x), self.find(y)
        if xr != yr:
            if self.rnk[xr] < self.rnk[yr]:
                self.par[xr] = yr
            elif self.rnk[xr] > self.rnk[yr]:
                self.par[yr] = xr
            else:
                self.par[yr] = xr
                self.rnk[xr] += 1
            return True
        return False  # x, y already in the same union



class Solution1:
    def largestComponentSize(self, nums: List[int]) -> int:
        """TLE
        """
        dsu = DSU(max(nums) + 1)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if math.gcd(nums[i], nums[j]) > 1:
                    dsu.union(nums[i], nums[j])
        for n in nums:
            dsu.find(n)
        for n in sorted(nums):
            print(n, dsu.par[n])
        return max(Counter(dsu.par).values())


class Solution2:
    def largestComponentSize(self, nums: List[int]) -> int:
        """Use prime numbers to factor each nums

        I have two blunders when using this method. First, I did not check the
        queue after all nums have been processed. It is possible that multiples
        of a prime number larger than the one listed in primes still exist in
        the queue. They must be processed as well.

        The second blunder is that I forgot to take away all counts of the same
        factor.

        5192 ms
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]
        dsu = DSU(max(nums) + 1)
        queue = [(i, n) for i, n in enumerate(nums)]
        for p in primes:
            temp = []
            group = 0
            for i, n in queue:
                if n % p == 0:
                    if not group:
                        group = nums[i]
                    else:
                        dsu.union(group, nums[i])
                    while n % p == 0:
                        n //= p
                elif n < p:
                    continue
                temp.append((i, n))
            queue = temp
        # handle the case where there are un-unioned values after turning every
        # number to a prime. E.g. if we have 463 and 926. They will not be
        # unioned during the prime checks, because the prime check stops at 317.
        # But, the prime check does reduce 926 to the prime value 463. Thus, we
        # can just union all the prime valeus that are the same in the remaining
        # queue
        groups = {}
        for i, n in queue:
            if n not in groups:
                groups[n] = nums[i]
            else:
                dsu.union(groups[n], nums[i])
        for n in nums:
            dsu.find(n)
        return max(Counter(dsu.par).values())


class Solution3:
    def largestComponentSize(self, nums: List[int]) -> int:
        """Borrow from the solution I used back in 08/31/2020
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]
        dsu = DSU(max(nums) + 1)
        prime_groups = defaultdict(list)
        for n in nums:
            x = n
            for p in primes:
                if x % p == 0:
                    prime_groups[p].append(n)
                    while x % p == 0:
                        x //= p
                elif x < p:
                    break
            if x > 1:
                prime_groups[x].append(n)  # x is now a prime value
        for group in prime_groups.values():
            for i in range(1, len(group)):
                dsu.union(group[0], group[i])
        for n in nums:
            dsu.find(n)
        return max(Counter(dsu.par).values())


sol = Solution3()
tests = [
    ([4,6,15,35], 4),
    ([20,50,9,63], 2),
    ([2,3,6,7,4,12,21,39], 8),
    ([65,35,43,76,15,11,81,22,55,92,31], 9),
    ([2,7,522,526,535,26,944,35,519,45,48,567,266,68,74,591,81,86,602,93,610,621,111,114,629,641,131,651,142,659,669,161,674,163,180,187,190,194,195,206,207,218,737,229,240,757,770,260,778,270,272,785,274,290,291,292,296,810,816,314,829,833,841,349,880,369,147,897,387,390,905,405,406,407,414,416,417,425,938,429,432,926,959,960,449,963,966,929,457,463,981,985,79,487,1000,494,508], 84),
    ([5803,6153,13,2062,6161,2068,7172,8219,6174,2080,36,4138,6188,8237,46,8240,8242,4151,6202,8253,8269,2126,6226,2135,4187,97,102,9233,6263,126,3776,2178,4233,8330,9581,8342,152,6297,5487,4253,8350,2208,6308,4262,4263,6314,1053,8373,184,4281,2242,8388,6346,6352,2258,6355,2261,2084,4815,6365,2270,225,4330,4333,6525,4341,6390,3455,4355,262,8456,6410,2318,6873,4379,6435,297,2439,302,2364,2372,334,4431,2387,340,8590,345,2400,8548,6508,367,4466,371,6516,2429,2662,391,2442,8589,398,8595,2452,4506,415,2467,8612,8615,4525,6578,8627,4535,2489,445,4542,447,8644,4558,629,6611,4567,6564,6620,4582,6638,496,4596,2549,4605,513,6660,8714,4620,2579,2585,6685,544,4644,557,8816,6717,8767,6723,2628,582,4679,3853,4689,2643,599,4700,614,8807,618,4882,6768,626,4724,2677,2689,642,4740,6790,4749,158,8848,5913,4769,2724,2730,4779,8897,717,2206,719,2769,8916,6871,4825,2788,8934,6890,751,6898,4855,2811,8960,4915,8967,4877,786,2835,2843,2848,6945,2851,8997,2856,6958,6961,9011,9012,9014,6976,4931,4932,842,7309,4947,9046,7001,2910,9055,2917,1169,7017,874,7655,9072,2931,9078,2935,9024,7044,9103,912,9105,923,5021,7071,1520,5029,2982,5033,2987,7089,7667,2997,950,7533,7096,954,6033,5059,970,9719,973,3023,1669,5075,3034,2895,5084,9181,7141,7142,3050,9196,7150,9201,1015,5116,9220,9223,3083,1036,1041,175,7197,1055,1057,3108,3109,7212,3123,5173,7223,1081,7007,1085,3143,9293,5424,5205,1893,7266,1128,9325,1146,1157,5258,9357,1166,9361,7325,9385,9392,7346,3254,1208,5309,9412,9416,5321,1229,7374,1238,5339,9436,5344,1254,9451,5368,3326,5376,1282,2945,3341,3343,7440,7441,1298,3348,5397,5398,3351,3633,5416,7465,3975,1325,3376,1335,3385,9536,7492,5445,3399,3402,3408,5462,9559,9934,5474,1383,3437,7535,9593,9597,1406,5503,7555,5511,3464,1423,7568,7570,3651,7573,3481,1437,7589,3496,9649,5559,9665,1474,7627,1487,7632,1495,5592,9126,3558,593,7657,9708,3568,5618,595,3575,5625,3583,1536,1537,5634,9131,7685,5646,3601,1556,7705,9757,1572,9777,3635,7736,5692,9795,3656,7773,6758,7783,7792,9842,9847,1667,7813,8813,9873,1682,1683,9880,1648,9899,3756,1710,5811,3769,9916,7114,4725,1728,9924,5835,3790,4387,740,7906,5859,1778,3828,3830,1784,9983,1799,9994,5901,1807,1810,5909,8836,1818,5919,5921,1827,7978,5931,3900,1853,7998,3907,8005,8012,3925,8030,3935,3940,5989,8038,3730,5998,3953,8054,1914,6020,6023,1931,1934,6031,8080,1688,8516,1955,4006,4007,6059,6064,1981,4037,6087,1999,2002,4054,8159,4072,6124,2032,4083,2037,8186], 439),
]


for i, (nums, ans) in enumerate(tests):
    res = sol.largestComponentSize(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
