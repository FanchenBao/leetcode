# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """LeetCode 936

        This is a very hard problem. I couldn't solve it in four hours. This
        is the official solution from here:

        https://leetcode.com/problems/stamping-the-sequence/solution/

        I didn't use the same algorithm, but the basic idea is the same. We
        reverse the process, and do a first run using sliding window to find any
        substring in target matches to stamp. Any match position will be turned
        into a wild card letter.

        After the first run, we will check the last letter. If it has been
        converted to wild card, the run is successful. Otherwise, we directly
        return [].

        Then, we perform subsequent runs, to convert the remaining letter to
        wild card. If convertion is not possible, on any letter, we return [].

        Each time a convert is encountered, we record the position of the stamp.
        The result is the reverse of the recorded stamps.

        O(MN), where M is the length of stamp and N length of target.
        208 ms, 51% ranking.
        """
        n, N = len(stamp), len(target)
        tlst = list(target)
        res = []
        for i in range(N - n + 1):  # the first run
            for j in range(n):
                if tlst[i + j] != stamp[j] and tlst[i + j] != '*':
                    break
            else:
                for j in range(n):
                    tlst[i + j] = '*'
                res.append(i)
        if tlst[-1] != '*':
            return []
        end = N - 1
        while end >= 0:  # the secodn run
            while end >= 0 and tlst[end] == '*':
                end -= 1
            if end < 0:
                break
            for i in range(min(end, N - n) + 1):
                for j in range(n):
                    if tlst[i + j] != stamp[j] and tlst[i + j] != '*':
                        break
                else:
                    change = False
                    for j in range(n):
                        if tlst[i + j] != '*':
                            tlst[i + j] = '*'
                            change = True
                    if change:
                        res.append(i)
            if tlst[end] != '*':
                return []
        return res[::-1]


class Solution2:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """The same solution but with slightly different implementation. We
        count how many wild cards that have been incorporated, and use that as
        the sentinel to determine when the runs shall end.
        """
        n, N = len(stamp), len(target)
        tlst = list(target)
        res = []
        num_stars = 0
        for i in range(N - n + 1):  # the first run
            for j in range(n):
                if tlst[i + j] != stamp[j] and tlst[i + j] != '*':
                    break
            else:
                for j in range(n):
                    if tlst[i + j] != '*':
                        tlst[i + j] = '*'
                        num_stars += 1
                res.append(i)
        if tlst[-1] != '*':
            return []
        while True:
            delta_star = 0
            for i in range(N - n + 1):  # subsequent run
                for j in range(n):
                    if tlst[i + j] != stamp[j] and tlst[i + j] != '*':
                        break
                else:
                    change = False
                    for j in range(n):
                        if tlst[i + j] != '*':
                            tlst[i + j] = '*'
                            delta_star += 1
                            change = True
                    if change:
                        res.append(i)
            num_stars += delta_star
            if num_stars == N:
                return res[::-1]
            if delta_star == 0:
                return []


sol = Solution2()
tests = [
    ('abc', 'aacbc', []),
    ('abc', 'ababc', [0, 2]),
    ('abca', 'aabcaca', [0, 3, 1]),
    ('a', 'aaaa', [3, 2, 1, 0]),
    ('aa', 'aaaa', [2, 1, 0]),
    ('aaa', 'aaaa', [1, 0]),
    ('aaaa', 'aaaa', [0]),
    ('cab', 'cabbb', [2, 1, 0]),
    ("ffebb", "fffeffebbb", [0, 1, 5, 4]),
    ('aye', 'eyeye', []),
    ('mda', 'mdadddaaaa', []),
    ('de', 'ddeddeddee', [6, 3, 0, 8, 7, 4, 1]),
]

for i, (stamp, target, ans) in enumerate(tests):
    res = sol.movesToStamp(stamp, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
