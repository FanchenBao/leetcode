# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        """No need to binary search.

        First, we try 1-digit number of partitions. If that is not sufficient,
        we try 2-digit, then 3-digit, etc. until we find the number of digits
        in the total number of partitions that can fit the given message.

        Then, we perform the partition per digit partition at a time. That means
        we do <1/total>...<9/total>, then <10/total>...<99/total>, then
        <100/total>...<999/total>, etc.

        There is a trick. Since we only know the number of digits in the total
        number of partitions, we cannot fill that number up initially during
        the construction of the result. We simply put a '*' there. Once we
        have completed the partitions, we can replace the '*' with the total
        partitions.

        O(N), 299 ms, faster than 93.89%
        """
        N = len(message)
        k = 1
        max_fit = 0
        while True:
            max_part = 10**k - 10**(k - 1)
            if 2 * k + 3 < limit:
                max_fit += (limit - 2 * k - 3) * max_part - (10**(k - 1) - 1)
            else:
                break
            if max_fit >= N:
                break
            k += 1
        if max_fit < N:
            return []
        res = []
        st, i, j = 1, 0, 1
        while i < N:
            to_take = limit - len(str(st)) - k - 3
            for _ in range(st, 10 * st):
                res.append(f'{message[i:min(i + to_take, N)]}<{j}/*>')
                i += to_take
                if i >= N:
                    break
                j += 1
            st *= 10
        return [r.replace('*', str(j)) for r in res]


class Solution2:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        """Brute force, go from one partition until the desired number of
        partitions. At each partition, we can compute the total length, and
        compare that to the max length possible. We stop when a fit has been
        encountered.

        O(N), 379 ms, faster than 88.04%
        """
        k = 1
        N = len(message)
        cur_len = N
        while (occ := 3 + 2 * len(str(k))) < limit:
            cur_len += occ + (len(str(k)) - len(str(k - 1))) * (k - 1)
            if cur_len <= limit * k:
                break
            k += 1
        if occ >= limit:
            return []
        res = []
        i = 0
        for j in range(1, k + 1):
            to_take = limit - 3 - len(str(k)) - len(str(j))
            res.append(f'{message[i:i + to_take]}<{j}/{k}>')
            i += to_take
        return res


sol = Solution2()
tests = [
    ("short message", 4, []),
    ("this is really a very awesome message", 9, ["thi<1/14>","s i<2/14>","s r<3/14>","eal<4/14>","ly <5/14>","a v<6/14>","ery<7/14>"," aw<8/14>","eso<9/14>","me<10/14>"," m<11/14>","es<12/14>","sa<13/14>","ge<14/14>"]),
    ("short message", 15, ["short mess<1/2>","age<2/2>"]),
    ("aaaaaa aaaaaa aaa aaaaaa aaaaaaaaaaaaaaaaaaaa aaaaa aaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaa aaaa aaaaaaaaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaa aaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaa a aaaaaaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaa aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaa aaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaa aaaa aaaaa aaa aa aaaaaaaaaaaaaaaaaaa a aaaaaaaaaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaa aaaaaaaaaaa aaaaaaaaaa aaaaaaaaaaaa aaaaaa aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaa aaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaa aaaaaaaaaaaaaaaaaa aaaaa aaaaaaaaaaaaaaaaa a aaaaaaaaaaaaaaaaa aaaaaaaaa aaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaa aaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaa aaaaaaaaaaa a aaaaaaaaaaaaaaa aaaaaaaa aaaaaaaaaaa aaaaaaaaaaaaaaaaa aaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaa aaaa aa aaaaaaaaaaaaa aaaaaaaaaa aaaaa aaaaaa aaaaaaaaaaaaaaaaaaa aa aaa aaaaaaaaaaaaa aaa aaaaaa aaaaaaaaaaaaaaaaaaa aaaaa aaaaaaaaaa aaaaaaa aaaaaaaaaaaaaaaaa aaaaaaaaa aaaaaaaaa", 1269, ["aaaaaa aaaaaa aaa aaaaaa aaaaaaaaaaaaaaaaaaaa aaaaa aaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaa aaaa aaaaaaaaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaa aaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaa a aaaaaaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaa aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaa aaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaa aaaa aaaaa aaa aa aaaaaaaaaaaaaaaaaaa a aaaaaaaaaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaa aaaaaaaaaaa aaaaaaaaaa aaaaaaaaaaaa aaaaaa aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaa aaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaa aaaaaaaaaaaaaaaaaa aaaaa aaaaaaaaaaaaaaaaa a aaaaaaaaaaaaaaaaa aaaaaaaaa aaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaa aaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaa aaaaaaaaaaa a aaaaaaaaaaaaaaa aaaaaaaa aaaaaaaaaaa aaaaaaaaaaaaaaaaa aaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaa aaaa aa aaaaaaaaaaaaa aaaaaaaaaa aaaaa aaaaaa aaaaaaaaaaaaaaaaaaa aa aaa aaaaaaaaaaaaa aaa aaaaaa aaaaaaaaaaaaaaaaaaa aaaaa aaaaaaaaaa aaaaaaa aaaaaaaaaaaaaaaaa aaaaaaaaa aaaaaaaaa<1/1>"]),
    ("baaaababab aabaaba", 7, ["ba<1/9>","aa<2/9>","ab<3/9>","ab<4/9>","ab<5/9>"," a<6/9>","ab<7/9>","aa<8/9>","ba<9/9>"]),
    ("this is really a very awesome messaaaaaaage", 10, ["this <1/9>","is re<2/9>","ally <3/9>","a ver<4/9>","y awe<5/9>","some <6/9>","messa<7/9>","aaaaa<8/9>","age<9/9>"]),
    ("abcabcabcabcabcabcabcabcabc", 8, ["abc<1/9>","abc<2/9>","abc<3/9>","abc<4/9>","abc<5/9>","abc<6/9>","abc<7/9>","abc<8/9>","abc<9/9>"]),
]

for i, (message, limit, ans) in enumerate(tests):
    res = sol.splitMessage(message, limit)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
