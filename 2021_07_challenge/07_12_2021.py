# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """LeetCode 205

        It's an easy question, but with a trick that we must check the
        uniqueness of mapping from s to t and from t to s. This means if a
        letter in t has been mapped before, it cannot be mapped again.

        O(N), 40 ms, 72% ranking.
        """
        m = {}
        mapped = set()
        for ls, lt in zip(s, t):
            if ls not in m:
                if lt in mapped:
                    return False
                m[ls] = lt
                mapped.add(lt)
            elif m[ls] != lt:
                return False
        return True


class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """Fancier version of Solution1"""

        def check(s1, s2) -> bool:
            m = {}
            for l1, l2 in zip(s1, s2):
                if l1 not in m:
                    m[l1] = l2
                elif m[l1] != l2:
                    return False
            return True

        return check(s, t) and check(t, s)


class Solution3:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """Official solution that finds the pattern of both strings. Then all we
        need to do is to compare the pattern. The pattern is found by replacing
        the string with the indices of the letters when they appear for the
        first time.
        """

        def transform(string: str) -> str:
            m = {}
            res = ''
            for i, le in enumerate(string):
                if le not in m:
                    m[le] = i
                res += str(m[le])
            return res

        return transform(s) == transform(t)


sol = Solution3()
tests = [
    ('egg', 'add', True),
    ('foo', 'bar', False),
    ('paper', 'title', True),
    ('a', 'a', True),
    ('a', 'b', True),
    ('badc', 'baba', False),
]

for i, (s, t, ans) in enumerate(tests):
    res = sol.isIsomorphic(s, t)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
