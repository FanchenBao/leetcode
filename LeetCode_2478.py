# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from bisect import bisect_left
from random import randint
from itertools import accumulate


class Solution1:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        """TLE
        """
        primes = {'2', '3', '5', '7'}
        if s[0] not in primes or s[-1] in primes:
            return 0
        N = len(s)
        prime_indices = [i for i, d in enumerate(s) if d in primes]
        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def helper(idx: int, part: int) -> int:
            if part == 1 and N - idx >= minLength:
                return 1
            if N - idx < part * minLength:
                return 0
            res = 0
            for j in range(bisect_left(prime_indices, idx + minLength), len(prime_indices)):
                next_idx = prime_indices[j]
                if N - next_idx < (part - 1) * minLength:
                    break
                if s[next_idx - 1] not in primes:
                    res += helper(next_idx, part - 1)
            return res

        return helper(0, k) % MOD


class Solution2:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        """Althought TLE again, this is the un-optimized DP solution with
        runtime O(K * N^2)
        """
        primes = {'2', '3', '5', '7'}
        if s[0] not in primes or s[-1] in primes:
            return 0
        MOD = 10**9 + 7
        N = len(s)
        # dp[i][j] is the number of partitions in s[:j + 1] with i partitions
        # Note that we use a 1D DP here. The base case is i == 1
        dp = [int(s[j] not in primes and j + 1 >= minLength) for j in range(N)]
        for i in range(2, k + 1):
            tmp = [0] * N
            for j in range(minLength * i - 1, N):
                if s[j] in primes:
                    continue
                for t in range(j - minLength + 1, minLength * (i - 1) - 1, -1):
                    if s[t] in primes:
                        tmp[j] += dp[t - 1]
            dp = tmp
        return dp[-1] % MOD


class Solution3:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        """The same as the previous DP solution, but we notice that the most
        inner loop is basically a prefix sum of the dp values of the previous
        row. We can optimize it via prefix sum
        """
        primes = {'2', '3', '5', '7'}
        if s[0] not in primes or s[-1] in primes:
            return 0
        MOD = 10**9 + 7
        N = len(s)
        # dp[i][j] is the number of partitions in s[:j + 1] with i partitions
        # Note that we use a 1D DP here. The base case is i == 1
        dp = [int(s[j] not in primes and j + 1 >= minLength) for j in range(N)]
        presum = [0]
        for j in range(1, N):
            if s[j] in primes:
                presum.append(presum[-1] + dp[j - 1])
            else:
                presum.append(presum[-1])
        for i in range(2, k + 1):
            tmp = [0] * N
            presum_tmp = [0] * N
            for j in range(minLength * i - 1, N):
                if s[j] in primes:
                    presum_tmp[j] = presum_tmp[j - 1] + tmp[j - 1]
                else:
                    tmp[j] = presum[j - minLength + 1]
            dp = tmp
            presum = presum_tmp
        return dp[-1] % MOD


# sol1 = Solution1()
# sol = Solution2()

# tests = [
#     (''.join(str(randint(1, 9)) for _ in range(100)), randint(1, 10), randint(1, 10)) for _ in range(1000)
# ]

# for i, (s, k, minLength) in enumerate(tests):
#     ans = sol1.beautifulPartitions(s, k, minLength)
#     res = sol.beautifulPartitions(s, k, minLength)
#     if res != ans:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}, Test: {s=}, {k=}, {minLength=}')

sol = Solution3()
tests = [
    ("23542185131", 3, 2, 3),
    # ("23542185131", 3, 3, 1),
    # ("3312958", 3, 1, 1),
    # ("7828745959293979512154292859512679792934793978763959293424767156567959567139745429797456597826382958243929397958285978247839397971587976762854797874585179263974393179217971597439267159597174393871767671292159395179582476397626797436717821212956297951545621597478797459797974347929767971385629717134587854787636597824217679245426583626717679797958517626567429792659582971795878397428782871215676787159382674265429392651743151717658343676212659747676797859795456262139245436742471292959793176587124217926395829793976592938382158793878715456262659342951587126282478795679742174345154397679717674383971212978743478397156265928597621213829742426762674795929793878767421313671297124717679345676512879783159367478347159767959787951765934387429792978787429793459717439382626543179787456343978783851247174765979715458765129765629362426797954342859317871587979395851762979362151397659795951715936347978792154397971547624247474513859563976397479295879515959293159367179765876787426317174315936763976597179595826", 500, 1, 1),
    # ("7168478767745784486796868352684255144884429621717744728155732836463829936516286365298277648528959258364168243968916296344425173714766624353272627456669996654822818444452166725218324193869295694378978655868328822361825979769792933729317582342953794499174838517497317531869121266142829279916178595651324845491618788677956198616577116757162727617219588213314612549924474142271698399374782566436391238126855651173197559436855446682245481738356791988489548784114582721293783496249274995359174493144796379969771331358167433218123114372718354286479712867596827923128434548361875813159961727899295233313366541614555355499713188618882173668589163421496966294486523847225291534561536412844191976958916185323297672889567476546544187357552661214937562591999277876312356889379387285695166827419394414993749374786858885483989648487634525799838226576288926853999557616233128943655384567385333267374291429512699484228872249328262867879682171378624478691368413468911572272866519255887632821372947918121936984476787999", 36, 8, 382427327),
    # ("79662968978318724", 5, 3, 0),
]

for i, (s, k, minLength, ans) in enumerate(tests):
    res = sol.beautifulPartitions(s, k, minLength)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
