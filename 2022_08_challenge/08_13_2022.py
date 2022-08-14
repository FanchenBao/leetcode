# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """LeetCode 30

        Sliding window. The fact that each word has the same length tells us
        that we only need to do len(word) rounds of sliding window, because
        after that, we will be repeating previous work. Hence, we pick a
        starting point, use Counter to match substring to words, and slide
        window it len(word) steps at a time. Then once we are done one round,
        we move forward one step and repeat.

        O(MN), where N = len(s), M = len(word), 366 ms, faster than 71.15% 
        """
        n = len(s)
        m = len(words[0])
        tgt_len = m * len(words)
        if n < tgt_len:
            return []
        words_c = Counter(words)
        res = []
        for start in range(m):
            cur_c = Counter()
            # build the initial counter
            for i in range(start, start + tgt_len, m):
                cur_c[s[i:i + m]] += 1
            if cur_c == words_c:
                res.append(start)
            # sliding window, one len(word) step at a time
            left, right = start + m, start + tgt_len + m - 1
            while right < n:
                cur_c[s[left - m:left]] -= 1
                cur_c[s[right - m + 1:right + 1]] += 1
                if cur_c == words_c:
                    res.append(left)
                left += m
                right += m
        return res        


sol = Solution()
tests = [
    ("barfoothefoobarman", ["foo","bar"], [0, 9]),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
    ("barfoofoobarthefoobarman", ["bar","foo","the"], [6, 9, 12]),
    ("aaaaaaaaaaaa", ["aa","aa"], [0,1,2,3,4,5,6,7,8]),
]

for i, (s, words, ans) in enumerate(tests):
    res = sorted(sol.findSubstring(s, words))
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
