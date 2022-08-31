# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        dp = [0]
        while dp[-1] < 2001:
            tmp = dp[-1] + a
            if tmp == x:
                return len(dp)
            if tmp in forbidden:
                break
            dp.append(tmp)
        i = 0
        while True:
            i += 1
            lst = []
            for j in range(len(dp)):
                tmp = dp[j] - b
                if tmp >= 0:
                    if tmp == x:
                        return i + j
                    if tmp in forbidden:
                        break
                    else:
                        lst.append(tmp)
            if not lst:
                break
            dp = lst
        return -1


sol = Solution()
tests = [
    ([14,4,18,1,15], 3, 15, 9, 3),
    ([8,3,16,6,12,20], 15, 13, 11, -1),
    ([1,6,2,14,5,17,4], 16, 9, 7, 2),
    ([128,178,147,165,63,11,150,20,158,144,136],61,170,135,6),
    ([162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98],29,98,80,121),
]

for i, (forbidden, a, b, x, ans) in enumerate(tests):
    res = sol.minimumJumps(forbidden, a, b, x)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
