# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class CombinationIterator1:
    """LeetCode 1286

    I am pretty sure this is not what the question intended, because I did not
    build any mechanism for iterator. I simply create the entire list of
    combinations, save it in the memory, and iterate it through. But this gets
    the job done.

    O(nCr), 48 ms, 88% ranking.
    """

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.comb = self._comb(0, combinationLength)
        self.idx = 0

    @lru_cache(maxsize=None)
    def _comb(self, idx: int, comb_len: int) -> List[str]:
        if comb_len == 1:
            return list(self.chars[idx:])
        res = []
        for i in range(idx, len(self.chars) - comb_len + 1):
            res += [self.chars[i] + c for c in self._comb(i + 1, comb_len - 1)]
        return res

    def next(self) -> str:
        self.idx += 1
        return self.comb[self.idx - 1]

    def hasNext(self) -> bool:
        return self.idx < len(self.comb)


class CombinationIterator2:
    """Use yield

    I had problem with this yield, because I was using lru_cache on it. This is
    wrong, because when I cacheed the value of self._comb(), the iterator
    remains there, such that if it has been exhausted already, a new call to
    self._comb() would not produce anything. In other words, we shall not cahce,
    but call self_comb() fresh each time.

    However, will this increase run time? The answer is no, because using yield
    is akin to caching the past (whereas lru_cache or any memoization is caching
    the future).
    """

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.next_c = ''
        self.comb = self._comb(0, combinationLength)

    def _comb(self, idx: int, comb_len: int):
        if not comb_len:
            yield ''
        else:
            for i in range(idx, len(self.chars) - comb_len + 1):
                for c in self._comb(i + 1, comb_len - 1):
                    yield self.chars[i] + c

    def next(self) -> str:
        if self.next_c:
            self.next_c, temp = '', self.next_c
            return temp
        return next(self.comb)

    def hasNext(self) -> bool:
        if not self.next_c:
            self.next_c = next(self.comb, '')
        return self.next_c != ''


CI = CombinationIterator2('abc', 2)
print(next(CI.comb))
print(next(CI.comb))
print(next(CI.comb))
# print(CI.next_c)
# print(CI.next())
# print(CI.next_c)
# CI.next()
# print(CI.next_c)
# CI.next()

# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
