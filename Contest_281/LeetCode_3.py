# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        letters = sorted(counter, reverse=True)
        i, j, N = 0, 1, len(letters)
        res = ''
        while True:
            num = min(repeatLimit, counter[letters[i]])
            res += letters[i] * num
            if j == N:
                break
            counter[letters[i]] -= num
            if counter[letters[i]] == 0:
                i = j
                j += 1
            else:
                res += letters[j]
                counter[letters[j]] -= 1
                if counter[letters[j]] == 0:
                    j += 1
        return res

        
sol = Solution()
tests = [
    ('cczazcc', 3, 'zzcccac'),
    ('aababab', 2, 'bbabaa'),
]

for i, (s, repeatLimit, ans) in enumerate(tests):
    res = sol.repeatLimitedString(s, repeatLimit)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
