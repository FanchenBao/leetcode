class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        The goal is to write Manacher from scratch.

        It took some efforts but I think it's well worth it and quite fun.

        O(N), 114 ms, faster than 95.22%
        """
        ss = '#'.join(f'^{s}&')
        dp = [0] * len(ss)
        j = 0
        max_i = 0
        for i in range(1, len(ss)):
            l, r = i - 1, i + 1
            if i <= j + dp[j]:  # see if ss[i] is within previous max reach
                ii = 2 * j - i
                # max left reach of ii can be restricted by the max left reach
                # of j
                reach = ii - max(j - dp[j], ii - dp[ii])
                l, r = i - reach - 1, i + reach + 1
            while l >= 0 and r < len(ss) and ss[l] == ss[r]:
                l -= 1
                r += 1    
            dp[i] = r - 1 - i
            if r - 1 > j + dp[j]:
                j = i
            if dp[i] > dp[max_i]:
                max_i = i
        return ''.join(ss[max_i - dp[max_i]:max_i + dp[max_i] + 1].split('#'))



sol = Solution()
tests = [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("aacabdkacaa", "aca"),
    ("babadada", "adada"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.longestPalindrome(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
