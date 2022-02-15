# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        """Failed. I checked the answer here:

        https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP

        The first idea I had is to find all consecutive substrings, compute
        the total number of subsubstrings each has, and add them together. This
        is apparently wrong, because I am double-counting a lot of substrings.

        The second idea is to find extension beyond the canonical alphabet, and
        try to count the number of unique substrings with regards to the
        extension. This was way too complicated and it failed as well.

        The third idea is to turn each consecutive substring into an interval,
        and try to merge the intervals to arrive at a solution. It worked if
        there was no extension, yet with extension, this idea was the equally
        complicated as the second one.

        Then I gave up.

        The idea of DP never occurred to me, because my head was too deep in
        the analysis approach. The DP idea is very neat: find the length of the
        longest substring that ends in a particular letter, then that substring
        contains all substrings that end in that letter. The answer is the sum
        of all substrings that end in each letter.

        O(N), 88 ms, 80% ranking.
        """
        dp = {chr(i + 97): 0 for i in range(26)}
        cnt = 1
        dp[p[0]] = 1
        for i in range(1, len(p)):
            if ord(p[i]) == ord(p[i - 1]) + 1 or ord(p[i]) == ord(p[i - 1]) - 25:
                cnt += 1
            else:
                cnt = 1
            dp[p[i]] = max(dp[p[i]], cnt)
        return sum(dp.values())


sol = Solution()
tests = [
    ('a', 1),
    ('zab', 6),
    ('cac', 2),
    ('abcaaa', 6),
    ('abcab', 6),
    ('abcabcde', 15),
    ("opqrstuvwxbcabcdefghijklmnopqrstuvwxycdefghijklmnopefghijklmnopqrghijklmnfghijklmnopqrstuvwxypqrstuvwxghijklmnopqrstuvwklmnopqrstuvwxklmnopqrsturstcdefghijklmnhijklmnopqrstghijklmnopqrefghijklmnopqrstuvwxstuvwxyijklmnopqrstuvwxyghijklmnopnopqrstuvwxyzabcdefghijklmnnopqpqrstuvwxqrstuvwxyzqrstuvwklmnopqefghijklmnopqrstfghijklmnopcdefghijklmdefghabcdefghijklmnpqdefopqrstuvbcdefghijklmnjklmnopabcdefghijklmnopstuvwxmnopqrstuvwxyzqrstuvwxyzcdefghijklmnopqrstuvwxyabcdefghijklmnopefghihijklmnopqrstumnopqrstuvwxklmnopdefghijklmnopqijklmnopqrstuvwxyzabcdefghijklmnopqrpqrstuvijklmnopqrabcdefghijklmnopqrstuvwjkldefstefghijklmnopqrstjklmnopqefghijkabcdefghijklmnopqabcdefefghijklmnopqabcdefghijklmnbcdefghijklmnhijkltuvwvwxcdefghijklmnopqrstuvwxijklmnopqrsabcdefghijklmnotuvwxstuvwxabcdefghijklmnopqrsxyfghijklmnopqrstuvwxyzpqrstuvwxhijklmnopqrstuvwxjklmnopqrstuvefghijklmnopqrstuvwopqrstuvwxyklmnopqrstuvwxefghvwxghijklmnopqrstuhijklmnopqrstuvwxyzmnopqrstuopqrstuvwxbcdefghijklmnopqrstuvwjklmnopqrstuvlmnopqrstuopqrstuvwxyghijklmnopqrsthijklmnopbcdefghijklmnopqrstupqrstabcdefghijklmnopqrstopqrklmnopqrstuvwxlmabcdefghicdecdeklmnopqrstuklmnopqrstuvwxghijklmjklmghijklmnopqrstuvwxytuvefghijklmnopqrefghijklmstuvwdefghijklmnklmnopqrstuvwxyqrstuvwxyabcdefghijklefgcdefghijklmnopqrstcdefghijklmnopqrstuvijklmnopghijklmnopqrstuvlmuvbcdefghijktuvwhijklmnefghijklmnopqrstuhijklmnopqrghijklmmnopqrstuvwxyzijklcdefghijklmnomnopqrstuvwxylmnopqrstuvwxydefghijklmnopqrlmnopqrefghijefghiklmnopqrstuvefghijklmnopqrstuvcdefghijklmnopqrabcdfghibcdefghijklmnopqrstuvwxhijklmefghijklmnopqrstuvwxyzcdefghijklmnopqrstfghijklmnopqrstuvwxyzhijklmnopqrstjklmnopqrsjklmnopqrstuklmnopbcdefghijklmnopqrstuvwxydefghijklmnopqrstfghijklmnopqrstuvabcdefghijklmnopqcdefghrstuvwxycdefghijklmnopqrslmnopqrstuvwxyzefghijklmnopqrstuvwwcdefghijklmnopnopqrsghijklmnopqijklmnopqrsklmnomnopqfghijklmnopqrstuvwxdefghijklmnopqrstuvwxfghijklmnopqrstuvopqrstuvqcdefghijklmnopqrstuvtuvwxyijklmnopqrstuvwxynopqrstuvwxyzklmnopqrstuvxyzdefghijopqrstuvwijghuvcdefghijklmnopqrstuvwmnopqrstuvwxefghijklmnopijklmnopmnopqrstutdefghijklmnopqrstuvwxklmnopqrsklmnopqrstuvwxbcdefghijklmnopqrstuvwxyzmnopqrcdefghijklmnopqrstjklmnopqrsdefghijklmnopqrstubcdefghijklmnopcdefghijklmnopqrstuvwxyzmnopqropqrstuefghklmnopqrstuvwxbcdefghijklmnoabcdefghijklcdefghijklmnopqrstuvwxymnopqrstuvwtuvwvwxyzefghijklmnopqrstuvwcdefghijklmnopqrsstijklmnopqrstuvwqrabcdefghijklmnopcdefghijklmnopqrstjklmnotuvwxyzhijklmnopqklmnopqrcstuvwxyfghijklmnopqrstuvwtuvwxfgghijklmnopqrstuvefgbcdefdefghijklmnopqrstdefghijkdefghijklmnklmnefghijklmnopqrstuvwxdefghijklmnopqrjklmnopqrstuvwxopqrstuvwxyzcdefghijklmnopqabcdefghijklmnopqrsghijklmnopqrstuvwxyfgrstcdefghijklmnopqrstklmnopbcdefghijklmnabcdefghijtuvdefghijklmnopqabcdefghijklmnopqrstuvwxyzfghijkhijklmijklmnopqrstuvcdefghijklmnfghijklmnopqrsqrstueffghijklmdefgefghijklmabcdefghijjklmnopqrstfghefghijklmnopqrstulmnopqrijkfgopqrslmnopqrstuvwxyjklmnopqijklmnopghijklmnohijklmnopqdefghijklmnopqrstuvjklmnopqrstuvwghijklmnodefghijklmnhijklmnopqrstghijklmnopqrstuvwnopqrstmnopqrstuvwxyzrstuvwdehijklmnoabcdefghijklmnopqrstuvlmnopqlmnopqrmnopqrsnopklmnopqdefghijklmnopqjklmnoqrstuvwxijklmnopqbcdefghijklmnopqrsdefghijkvwxyzhirspqrabcdijklmnopfghijklmnpqrdefghijklmnopdeabcdefghijkijopqrstuvwxythijklmnopqrstuvwxyzfghijklmnopqrsghijklmnopqrtuvjklthijklmvwxyzbcdefghnopqrstuvwxydghijklmnopqrstmnopgopqpqrsqrstudefghijklmnstuvwxqrstuvwfghijklmnopqrstuvwxyabcdefghijklmnstuvwxcdefghijklmnopqrstuvwxyzklmnopqrstuvwxabcdefghijklmnopqrstuvwpqdefghijkdefghijklmnrstuvwxjkhiefgrstuvwxlmnopqrsdefghijklmnopqrstuvwxycdefghijklmnopqrstuvwnopqrstuvwxyzafghijklmnopqrstghijklmnopqrstcdeabcdefghijklmnopqrstuvlmnopqrstuijklmnouvwxyijklmnlmnopqrswxyzopqrstuvghijklbcdejklmnopqrstuvwxyefdefghijkdefghijklmnopqrstuvwghijklmnopmnopqrfghijklmnabcdefghijklmnopqrstuvwbcdefghijklmnopqrstijklklmnopqrstughiefghijklmnopqrstdefghijklmnabcdefghijklmnopqrstghijklmnopqrstuvwxyefghijklmnopqrstuvwxyfghijklmnopquvwwfghijklmnopqrstmnopqrstabcdefghijklvwxyzfghijklmcdefghiopqrstuvwxyzuvwxyefghijklmnopqrstuvwhijklmnopqhijklmnopqrstuvwxyzcdefghijklmnopqrstuvbcdeftuvwxstuvwxymnefghijklmnopqrstuvbcdefghijklmnopqrstuvwxmnopqrspqrstuvwxyzefghijklmnopqrstuvwxjklklmnopqrstuvnopqrslmnpqrstuvwyzklmnopqijklqrstuvwxfghijklmnopqrstuvwxyrstuvvwxycdefghijklmnopqrstuvwrstuvwxyzabcdefghijkijklmnopqrstuvwxyzcdefghijklmnopqrstuefghijklmnopqrstuvwxabcdefghijklmnopqstcdefghijhijnopdefghijklmnopqrstuvjklmnopqrpqhijklmnopqrstcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwphijklmnopqrsefghilmnopqrstuvwxlmnoghijklmnopqrstuvwxyzfghijklmnopqklmnopqrstuvqrstuvwxyzlmnopqrstulmnopqrsttuvwxnopqrstuopqrstuvwxyzcopqrstuvwxyjklmnopqrstuvabcdefghijghijpqefghijklmnopqrstcdefghijklmnnopqrstuvwxyijklmnopqrstuvwxbcdefghijklmnopqrstlmnopqrstuvwhijklmnopqrstuvwxbcdefghijklmnopqrstuvwxymnopqrabghabcdefghiabcdefghijklmnopqrsbcklpqrstuvwxymnopqrsklmnodefghijklmnopqrstumnopqrstuvwjklmnopqrstuvwxyefghdefghijklmnopqrstuvaablmnopqrstbcdefghijuvwmnopqrslmlmnopqlmnopqrstuvwxytuvuvjklmnghijklmnopqrstuvwrstuvwxhijklmnopqrstuvwxyznopqrstuvklmnopqrstuvnopqrstunopqrqrstmnopqrstuvwxpqrstuvwxyznopqrstujklmnopqrstcdefghijnopqrstuvwxyzqrstuvwxycdefghijklmnopqrstuvklmnopqrsklmnopfghijklmnopqrbuvwxyzvwxytuvwxyzabcdefghijklmnoppqrstpqrstuvwdefghijklmnopqrsklmnopabcdefghijklmnopqrstuvtuvwxycdefghijklmnopqbcdefghijklmnopqrstuabcdefgijklmnopqrstuvwxyubcdefghijklbcbcdfgklmnopqrfghiklmnmnopqrnopqklmnoptabcdefghijklmjkbcdefghijklmnopqklmnopqrbcdefghijklmnopefghijklmnopqrstuvwxyzkklmnopqrscdefghijklmnpqrtuvwxyzvwxyzstuvababcdefrsjkmnopqghijklmnopqrstuvwxyijklmnopqrmnohijklmnopqrsbcdefghijklmnopqrstlmnopqrstcdefghijklfghijklmnopqrstuvwxyzghijklmnjklklmnopqrmnopqrsthijklmnobcdefghijklmnopzbcdefghijklmnopqrstuvwcdjklmnopqrsthijkabcdefjklmnopqrstuvwhiopqrstuvcdefghijklmnopqrsjklmnopqrabcdefghijklmnopqrstuvwxyzijklmnopqrpqrsghbcdefghijkopqrstuvwxyefghighijklmnopxyefghijklmnopqrijklmnopqrscdefghijklmnopqrstuefabcdefghijklmnopqdefghijklmnopqrstuvwxjklmnoijklmlmnopqrstuvwanopqrqrsuvwxyjklmnopijklmnopghijklmnopqrstuvwxyzcdefghijklmnpqrstuvhijuvwxyzhijkopqrsthijklmnmnopqrdefghijklmnopqijklmnodefghijklmnopqrstuvwxyzfghijklmnopqrstuvwxlmnopqropqrsrstuvwxybcqrstucdefghfghijklmnopqrstuvbcdefghijklmnklmnopqrstuefghijklmnopqrstuvwcdefghijklmnopqrstuvuvwxyzbcdefghijklabcdefabuvbcdefghijklmnstpqrstuefghijklmnofghijklmnopqklmnopqrstdefgdefghijklmnopqrstuvhijklmnopqrstuvwxyzghidefghijklmghtuvopbcdefghijwcdefghijklmnopqrstuvwxyzlmnopqrstuvwxyztuvwdefgopqrsmnopqrsopqrstuvwxyzopqrstuvwxyefghijklmnobcdefghqrstijklmnoppqrstujklmncdefghijklmnopqrstefghijklmnopqrstuvwxyfghijklmnopqrstuvwxrstuvwxyzklmbcdefghijklmnoppqrstuvwefrstuvwlmnopqrstuvwxabcdefghijklmnopqrstuvwxlmnopqrjklmnmnfghijklmnabcdefghijklmnobcdefghijklmnopqrsdefghijklstopqrstuvwopqrstuvwxyabcdefghijklmfghijklmnopqrstuvwxcdefghijklmnopqrstuvwxyzghiopqrstuvwxybcdefghijklmnopqrstuvwcdghijklmnopqgbcdefghijklmnopqrstuabcdefghuvwfghijcdefghituklmnabcdefhijklmnopqklmnopqcdefghijklmnopqrstuvcdefghijklmnopqrstuvwxkbcdefghijklmnopqrstuijklmnopqrstuvwxybcdefghijklpqbcdefghijklmnopqrstuvijklwxyzwxyijklmnopqrstuvwxyzklmnopqrstuvwuvwxyznopqrstuvwxyfghijklmnopqrstuvlmnoefghijklmnefghihijklmnefghijkllcdefghijklmnopqrstuvwxyzdklmabcdefghijklmnoghijklmnpqrstuvwxybcdefghijklmnopqrstuvwxghijklmnopqrstuvwxyefttcdefghijklmnopqrstuvwxyzopqrsghijklmnopqrstuvwxfghijklmnopqrstuvwxabcdefghijklmnopqrstuvwxyzopqrstjklmnophijklmnopqrstuvwjklmnopqrstuvwxcdefghijklmnouvmnopqrstuhijklmnopqrpqrstuvwxrstuvwnojklmghijklmndefghlmnopqrstuqrstjklmnopqrstuvwdefghijklmnopdepqrstuvwefghijklmnopqrstuvjklmnopqrsijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwnopqrsefghijklmnopqrstuvcdefghipqbcdefghijklmnopqrstabcdefghijklmnofghijklmnefghijklmnopqrstghijklmnklmnopqrstuvwxyvwcdefghijklmnopqrsstuvwxyzmnopqrsghijklmnabcdefghijklmbcdefghijklmnopqrstuvwxzghijklmnopqrstucdefghijklmfghijklmnefefghijklmnopqcdefghiijklmnopqrstopqrstuvwxyrstuvwxyzsbopqrstdefghijklmnopqrstuvwxyzefghijklmnopqrstufghijklmnopqrstuvvwxyztuvhijijklmnopqrstuvghibcdefghijklefghijklmnopqrstuvhijklmnopqrstuvlmnopjklmnopqrabcdefghijklmnopqrstabcdefghijklmnopqrstulmnopqabcdefghdefghijklmnabcdefghijklmnopqrstuvwxyzbcdefghijklmnopqrstuvwxjklmnopqrsthijjkyzfghijklmnopqrstumnopqrstuijklmnopqrpqrklmnopqrstnopqrstuvwopqmnopqrstcdefgjklmnopqrstuvwbcdefghijklmnopqrstuvefgbcdefghijklmnopqrghijklmnomnopzmnopqrstuvwxijklmnopqrstuvwxyzcdjklmnopqrshideftuvwxyzabcdefghijklmnopqrsbcdefghijklmnopqrstuvwfgabcdefghijklmnopqrstjklmnopqrstuvcdefghijklmnopqrstuvwxyzghijklmnopghijklmnopqrstuvwxyzlmnopqrstuvwhijklmnvwxyklmnopqrstuvjklghijkbmnopqrstuvwxmnopqrstuvwxymnopqrstuvwxklmnlmnowxyzciwxyzmnopqrsbcklmnopqrstudefghijklmnopqrslmnoppqrstuvwabrhijklfghijklmnopqrstuvwxefhijklmnjkljklmnopqrstuvwcdefghihijklmnopqrmnopqjklmnopqrstuvwxxylmnopqrspqrstuvwxyzyzdefghijklmnopqrshijklmnopqbcdefghijklmnopqrstuvwxyznopqbcdefghbcdefghijklmnolmnopqrstuvwxjklmnopqrstuvwxyzabcdefghijklmnopqrsvwabcdcdefghijklmnocdefghiijghijklmnopqrstuhijeffghnopqopqrsabcdefcdefghijklmnopqrstuvwnopqrstuvhijkfghijklmnstuefghijklmnopbcdefghijklmnopqrstuvwxyzfghiabcdefghimnopqrstuvwxyzdefghijklmnopqrstuvtuvwxjklmnopqrstuvwxyzghijklmnopqrsdefghnopqrstxyklmnopcdaghijklmnopqrstuvwxyzbcdefgqrstuvwghijklmnopfghijklvwxywxefghijklmnopqrstabcdefjklmnopqrstuvwxydefghijklmnjklmnopqrstuvxyefghijklmnopqrstuvhijklmnopqrstupqrsklabcdefghijklmnlmnohijklmqrstuvwxghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxpqrsjklmnopqrstuvwxabcdefghistuvhijklmnoefghighijklmnopqrstuvwxijklmnopqrijklmnopqrslmnopqrstuvwxyklmnopqrsiabcdefghfghijklmnhijklmfghijklmnopqrstuvwxyfghijkfghijklmnopqrstumnopqrstbcdefghijklmnopqnoabcdefghijklmnopqrsdefghijklmnopqrstuvwxdefghiqrstuvwxyvwxylmnopqrstefghijklmqrstuvwxnomnopqrstabtuvwxyklmnopklmnopqrstuvwxyabcdefghijklmnopqrstuv", 831),
    ('zabcdefghijklmnopqrstuvwxyzabcdefghijklm', 715),
    ("yhxtdobyly", 8),
    ('abebc', 6),
]

for i, (p, ans) in enumerate(tests):
    res = sol.findSubstringInWraproundString(p)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')