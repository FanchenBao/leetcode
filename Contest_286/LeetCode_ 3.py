# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        p_anchor = [
            [],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ]
        if intLength == 1:
            return [int(p_anchor[1][q]) if q <= 9 else -1 for q in queries]
        unit_count = [0, 1, 1, 10, 10, 100, 100, 1000, 1000, 10000, 10000, 100000, 100000, 1000000, 1000000, 10000000]
        res = []
        for q in queries:
            if q > unit_count[intLength] * 9:
                res.append(-1)
                continue
            res.append([''] * intLength)
            quo, rem = divmod(q - 1, unit_count[intLength])
            res[-1][0] = res[-1][-1] = str(quo + 1)
            cur_len = intLength - 2
            i = 1
            while cur_len > 1:
                quo, rem = divmod(rem, unit_count[cur_len])
                res[-1][i] = res[-1][-i - 1] = str(quo)
                cur_len -= 2
                i += 1
            if cur_len:
                res[-1][i] = res[-1][-i - 1] = p_anchor[cur_len][rem]
            res[-1] = int(''.join(res[-1]))
        return res
        
        
sol = Solution()
tests = [
    ([1,2,3,4,5,90], 3, [101,111,121,131,141,999]),
    ([2,4,6],4,[1111,1331,1551]),
]

for i, (queries, intLength, ans) in enumerate(tests):
    res = sol.kthPalindrome(queries, intLength)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
