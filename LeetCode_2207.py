# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        """Too confident. The edge case is when pattern[0] == pattern[1]. But
        it is important that this is the only legit way to check for the edge
        case. If we check n == 0, that is WRONG.

        O(N), 578 ms, faster than 31.88%
        """
        p0ids, p1ids = [], []
        for i, t in enumerate(text):
            if t == pattern[0]:
                p0ids.append(i)
            elif t == pattern[1]:
                p1ids.append(i)
        res = 0
        m, n = len(p0ids), len(p1ids)
        if pattern[0] == pattern[1]:
            # the two letters in the pattern are the same
            return (m + 1) * m // 2
        i = j = 0
        while i < m:
            if j == n or p0ids[i] < p1ids[j]:
                res += len(p1ids) - j
                i += 1
            else:
                j += 1
        return res + max(m, n)


class Solution2:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        """This is from Lee215. Similar idea, but much better implementation
        and without the need to extra arrays to keep track of the indices. We
        only need to keep track of the count of pattern[0] and pattern [1].
        Each time pattern[0] is encountered, we can produce 0 new patterns. But
        each time pattern[1] is encountered, we can produce the current cnt0
        number of new patterns.
        """
        res, cnt0, cnt1 = 0, 0, 0
        for t in text:
            # Notice the trick here. It is not elif. This is to handle the
            # case where pattern[0] == pattern[1]
            # Also notice that the check for pattern[1] must occur before the
            # check for pattern[0]. Otherwise, we would double count when
            # pattern[0] == pattern[1]
            if t == pattern[1]:
                res += cnt0
                cnt1 += 1
            if t == pattern[0]:
                cnt0 += 1
        return res + max(cnt0, cnt1)


sol = Solution2()
tests = [
    ("abdcdbc", "ac", 4),
    ("aabb", "ab", 6),
    ("vnedkpkkyxelxqptfwuzcjhqmwagvrglkeivowvbjdoyydnjrqrqejoyptzoklaxcjxbrrfmpdxckfjzahparhpanwqfjrpbslsyiwbldnpjqishlsuagevjmiyktgofvnyncizswldwnngnkifmaxbmospdeslxirofgqouaapfgltgqxdhurxljcepdpndqqgfwkfiqrwuwxfamciyweehktaegynfumwnhrgrhcluenpnoieqdivznrjljcotysnlylyswvdlkgsvrotavnkifwmnvgagjykxgwaimavqsxuitknmbxppgzfwtjdvegapcplreokicxcsbdrsyfpustpxxssnouifkypwqrywprjlyddrggkcglbgcrbihgpxxosmejchmzkydhquevpschkpyulqxgduqkqgwnsowxrmgqbmltrltzqmmpjilpfxocflpkwithsjlljxdygfvstvwqsyxlkknmgpppupgjvfgmxnwmvrfuwcrsadomyddazlonjyjdeswwznkaeaasyvurpgyvjsiltiykwquesfjmuswjlrphsdthmuqkrhynmqnfqdlwnwesdmiiqvcpingbcgcsvqmsmskesrajqwmgtdoktreqssutpudfykriqhblntfabspbeddpdkownehqszbmddizdgtqmobirwbopmoqzwydnpqnvkwadajbecmajilzkfwjnpfyamudpppuxhlcngkign", "rr", 496),
    ("tollaoweoaxzxwngdkjtrbcpfvqbfthtktaxv", "am", 3),
]

for i, (text, pattern, ans) in enumerate(tests):
    res = sol.maximumSubsequenceCount(text, pattern)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
