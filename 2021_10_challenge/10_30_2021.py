# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def longestDupSubstring(self, s: str) -> str:
        """TLE
        
        This solution uses a dict to record the indices of each letter in s.
        For each idx, the value records the dup length when matching the current
        idx with any of its previous occurrences.

        Unfortunately, this solution runs in O(N^2) in worst case scenario,
        where all the letters in s are the same.

        It passes 52/66 test cases before time out.
        """
        dp = {}
        res_len, res_end_pos = 0, 0
        for i, le in enumerate(s):
            if le not in dp:
                dp[le] = {i: {}}
            else:
                cdict = {}
                for pi, pdict in dp[le].items():
                    if pi == 0 or s[pi - 1] != s[i - 1]:
                        cdict[pi] = 1
                    else:
                        cdict[pi] = 1 + dp[s[i - 1]][i - 1][pi - 1]
                    if cdict[pi] > res_len:
                        res_len = cdict[pi]
                        res_end_pos = i
                dp[le][i] = cdict
        return s[res_end_pos - res_len + 1:res_end_pos + 1]


class Solution2:
    def longestDupSubstring(self, s: str) -> str:
        """Using both hints

        Two key insights:

        1. Binary search. This is the most important insight. We can start with
        half the length of s as a potential answer. If we can find dup at this
        length, that means there might be dup substring of even higher length.
        Thus we binary search for a higher value. If we cannot find dup at this
        length, that means the dup substring must have lower length. Then we
        binary search the lower half.

        2. Using a set to quickly check whether there exists dup for substring
        of a given length. This is touted as the Rabin-Karp algo, which uses
        modulo as the hash function. But in our case, we can simply use a set
        to serve as the hash function.

        With these insights, the final difficult part is to determine how the
        lo and hi shall change during binary search. If the condition is lo < hi
        we know one of these two needs to change after each round. Is it hi -= 1
        or lo += 1? It's the latter, because the computation of mid bias towards
        lo. If we keep lo the same, we will run into the situation where hi = 
        lo + 1, and mid = (lo + hi) // 2 == lo. And this causes infinite loop.
        Hence, we use lo += 1.

        O(NlogN), 2992 ms, 43% ranking.

        UPDATE: the runtime is not O(NlogN), but O(N^2logN) in worst case,
        because hashing of the strings in set takes O(L) where L is the
        length of the string. The point of using Rabin-Karp is to reduce the
        hashing complexity to O(1) on average because we can do rolling hash.

        We were able to pass the OJ because LeetCode loosened the memory limit
        so that we can set a hashset in place of Rabin-Karp. This solution has
        memory usage at 14%
        """
        N = len(s)
        lo, hi = 0, len(s)
        res = ''
        while lo < hi:
            mid = (lo + hi) // 2
            bag = set()
            for i in range(mid - 1, N):
                cstr = s[i - mid + 1:i + 1]
                if cstr not in bag:
                    bag.add(cstr)
                else:
                    res = cstr
                    break
            else:
                hi = mid
                continue
            lo = mid + 1
        return res


class Solution3:
    def longestDupSubstring(self, s: str) -> str:
        """My attempt at Rabin-Karp.

        O(NlogN), 1996 ms, 65% ranking. But the biggest improvement is memory
        usage. Now at 47%.
        """
        MOD = 1000000009
        N = len(s)
        b = 256  # base, it has to be larger than the character set. Given
        # that the character set is ASCII, we use 256 for safety.

        def check(substr_len: int) -> str:
            """This is the Rabin-Karp implementation, following strickly from
            the wikipedia page: https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
            """
            aux = 1  # equivalent of (b^(substre_len - 1)) % MOD
            for _ in range(substr_len - 1):
                aux = (aux % MOD) * b
            aux = aux % MOD
            ha = 0  # hash of the first substring of length substr_len
            for i in range(substr_len):
                ha = (ha * b + ord(s[i])) % MOD
            seen = defaultdict(list)
            seen[ha].append(0)
            for i in range(1, N - substr_len + 1):
                # Rolling hash
                ha = ((ha + MOD - ord(s[i - 1]) * aux) * b + ord(s[i + substr_len - 1])) % MOD
                if ha in seen:
                    target = s[i:i + substr_len]
                    for j in seen[ha]:
                        if s[j:j + substr_len] == target:
                            return target
                seen[ha].append(i)
            return ''

        lo, hi = 0, len(s)
        res = ''
        while lo < hi:
            mid = (lo + hi) // 2
            temp = check(mid)
            if len(res) < len(temp):
                res = temp
            if temp == '':
                hi = mid
            else:
                lo = mid + 1
        return res




sol = Solution3()
tests = [
    ('banana', 'ana'),
    ('abcd', ''),
    ('b', ''),
    ('bb', 'b'),
    ('pmyiaxmicpmvqywlkisfzzutlxxjipitwcfxgqqfnxizowkqfmzsvkxryknasyvthozahbmapwqocupxcktmmtddxgatzftamrsvtddjpbnrojcqonmzxmknashplmykdbadiiccdkbyyzifqxvqfwgwihxgnrhqlmqprnjawuzcotutbkgnykuuwtzzzppmoyfmplhpznpnlwwbndekakpsmehzmbcfoyudgwsvehzgsfwqdkihiiwxfskicrbmoevxvpmmymihlkmgnuyohcofzfkehccwxezxypnnvqzrilr', 'knas'),
]

for i, (s, ans) in enumerate(tests):
    res = sol.longestDupSubstring(s)
    if len(res) == len(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
