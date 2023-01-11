# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        if limit <= 5:
            return []
        N = len(message)
        lo, hi = 1, N + 1
        num_part = math.inf
        while lo < hi:
            mid = (lo + hi) // 2
            # print(lo, mid, hi)
            k = len(str(mid))
            max_need = 2 * k + 3
            if max_need > limit:
                hi = mid
            else:
                # compute the range of message length for which mid number of
                # parts with limit can work
                r_base = 0
                kk = len(str(mid - 1))
                st, en = 10**(kk - 1), mid - 1
                while st <= en and kk:
                    r_base += ((en - st) + 1) * (limit - kk - k - 3)
                    kk -= 1
                    st, en = 10**(kk - 1), st - 1
                rl, rr = r_base + 1, r_base + limit - max_need
                print(lo, mid, hi, r_base, rl, N, rr)
                if rl > rr:  # edge case, e.g. mid = 10, limit = 7
                    hi -= 1
                else:
                    if rl <= N <= rr:
                        num_part = mid
                        hi = mid
                    elif N < rl:
                        hi = mid
                    else:
                        lo += 1  # go up gently
        if num_part == math.inf:
            return []
        res = []
        st, en = 1, min(9, num_part)
        i, j = 0, 1
        while j <= num_part:
            to_take = limit - len(str(st)) - len(str(num_part)) - 3
            for _ in range(st, en + 1):
                res.append(f'{message[i:i + to_take]}<{j}/{num_part}>')
                i += to_take
                j += 1
            st, en = en + 1, min(10**(len(str(st)) +1) - 1, num_part)
        return res


sol = Solution()
tests = [
    # ("this is really a very awesome message", 9, ["thi<1/14>","s i<2/14>","s r<3/14>","eal<4/14>","ly <5/14>","a v<6/14>","ery<7/14>"," aw<8/14>","eso<9/14>","me<10/14>"," m<11/14>","es<12/14>","sa<13/14>","ge<14/14>"]),
    # ("short message", 15, ["short mess<1/2>","age<2/2>"]),
    # ("aaaaaa aaaaaa aaa aaaaaa aaaaaaaaaaaaaaaaaaaa aaaaa aaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaa aaaa aaaaaaaaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaa aaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaa a aaaaaaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaa aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaa aaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaa aaaa aaaaa aaa aa aaaaaaaaaaaaaaaaaaa a aaaaaaaaaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaa aaaaaaaaaaa aaaaaaaaaa aaaaaaaaaaaa aaaaaa aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaa aaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaa aaaaaaaaaaaaaaaaaa aaaaa aaaaaaaaaaaaaaaaa a aaaaaaaaaaaaaaaaa aaaaaaaaa aaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaa aaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaa aaaaaaaaaaa a aaaaaaaaaaaaaaa aaaaaaaa aaaaaaaaaaa aaaaaaaaaaaaaaaaa aaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaa aaaa aa aaaaaaaaaaaaa aaaaaaaaaa aaaaa aaaaaa aaaaaaaaaaaaaaaaaaa aa aaa aaaaaaaaaaaaa aaa aaaaaa aaaaaaaaaaaaaaaaaaa aaaaa aaaaaaaaaa aaaaaaa aaaaaaaaaaaaaaaaa aaaaaaaaa aaaaaaaaa", 1269, ["aaaaaa aaaaaa aaa aaaaaa aaaaaaaaaaaaaaaaaaaa aaaaa aaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaa aaaa aaaaaaaaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaa aaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaa a aaaaaaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaa aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaa aaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaa aaaa aaaaa aaa aa aaaaaaaaaaaaaaaaaaa a aaaaaaaaaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaa aaaaaaaaaaa aaaaaaaaaa aaaaaaaaaaaa aaaaaa aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaa aaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaa aaaaaaaaaaaaaaaaaa aaaaa aaaaaaaaaaaaaaaaa a aaaaaaaaaaaaaaaaa aaaaaaaaa aaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaa aaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaa aaaaaaaaaaa a aaaaaaaaaaaaaaa aaaaaaaa aaaaaaaaaaa aaaaaaaaaaaaaaaaa aaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaa aaaa aa aaaaaaaaaaaaa aaaaaaaaaa aaaaa aaaaaa aaaaaaaaaaaaaaaaaaa aa aaa aaaaaaaaaaaaa aaa aaaaaa aaaaaaaaaaaaaaaaaaa aaaaa aaaaaaaaaa aaaaaaa aaaaaaaaaaaaaaaaa aaaaaaaaa aaaaaaaaa<1/1>"]),
    # ("baaaababab aabaaba", 7, ["ba<1/9>","aa<2/9>","ab<3/9>","ab<4/9>","ab<5/9>"," a<6/9>","ab<7/9>","aa<8/9>","ba<9/9>"]),
    # ("this is really a very awesome messaaaaaaage", 10, ["this <1/9>","is re<2/9>","ally <3/9>","a ver<4/9>","y awe<5/9>","some <6/9>","messa<7/9>","aaaaa<8/9>","age<9/9>"]),
    ("abcabcabcabcabcabcabcabcabc", 8, ["abc<1/9>","abc<2/9>","abc<3/9>","abc<4/9>","abc<5/9>","abc<6/9>","abc<7/9>","abc<8/9>","abc<9/9>"]),
]

for i, (message, limit, ans) in enumerate(tests):
    res = sol.splitMessage(message, limit)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
