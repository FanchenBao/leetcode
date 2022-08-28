# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        """It's a bit complicated, but not difficult. The key step is to sort
        indices, along with sources and targets, such that they occur from
        small to large in terms of indices. Then we can scan s from left to
        right. Each time an index hit a value in indices, we check source. If
        the check completes, we put target into an aux list. Otherwise, we move
        on to the next index.

        O(MlogM + N), where M = len(indices), N = len(s).
        53 ms, faster than 65.79%
        """
        combined = sorted((idx, src, tgt) for idx, src, tgt in zip(indices, sources, targets))
        aux = []
        pre = i = j = 0
        while i < len(s) and j < len(combined):
            if i == combined[j][0]:
                _, src, tgt = combined[j]
                aux.append(s[pre:i])
                pre = i
                k = 0
                while i < len(s) and k < len(src):
                    if s[i] != src[k]:
                        break
                    i += 1
                    k += 1
                else:
                    if k == len(src):
                        aux.append(tgt)
                    pre = i
                    i -= 1
                j += 1
            i += 1
        aux.append(s[pre:])
        return ''.join(aux)


class Solution2:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        """Just go through indices and compare substring of s to source directly
        This way, we don't have to check letters one-by-one.

        Inspired by https://leetcode.com/problems/find-and-replace-in-string/discuss/130587/C%2B%2BJavaPython-Replace-S-from-right-to-left

        O(MlogM + MN), 50 ms, faster than 71.41%
        """
        combined = sorted((idx, src, tgt) for idx, src, tgt in zip(indices, sources, targets))
        res, pre = '', 0
        for idx, src, tgt in combined:
            res += s[pre:idx]
            if s[idx:idx + len(src)] == src:
                res += tgt
                pre = idx + len(src)
            else:
                pre = idx
        return res + s[pre:]
        

sol = Solution2()
tests = [
    ("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"], 'eeebffff'),
    ("abcd", [0, 2], ["ab","ec"], ["eee","ffff"], 'eeecd'),
    ("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"], "vbfrssozp"),
    ("jjievdtjfb", [4,6,1], ["md","tjgb","jf"], ["foe","oov","e"], "jjievdtjfb")
]

for i, (s, indices, sources, targets, ans) in enumerate(tests):
    res = sol.findReplaceString(s, indices, sources, targets)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
