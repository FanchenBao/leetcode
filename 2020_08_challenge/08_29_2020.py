# from pudb import set_trace; set_trace()
from typing import List
from itertools import combinations
from collections import defaultdict
from functools import lru_cache


class CombinationIterator1:
    """Cheating solution, because we are using itertools.combinations"""

    def __init__(self, characters: str, combinationLength: int):
        self.comb = combinations(characters, combinationLength)
        self.next_val = ''

    def next(self) -> str:
        if self.next_val:
            temp = self.next_val
            self.next_val = ''
            return temp
        else:
            return ''.join(next(self.comb))

    def hasNext(self) -> bool:
        if not self.next_val:
            self.next_val = ''.join(next(self.comb, ['']))
        return self.next_val


class CombinationIterator2:
    """Custom implemented combination"""

    def __init__(self, characters: str, combinationLength: int):
        self.comb = self.combination(characters, combinationLength)
        self.idx = 0

    @lru_cache(maxsize=None)
    def combination(self, characters, length):
        if length == 1:
            return list(characters)
        else:
            res = []
            for i in range(len(characters) - length + 1):
                res += [characters[i] + comb for comb in self.combination(characters[i + 1:], length - 1)]
            return res

    def next(self) -> str:
        self.idx += 1
        return self.comb[self.idx - 1]

    def hasNext(self) -> bool:
        return self.idx < len(self.comb)


class CombinationIterator3:
    """Use bitmask"""

    def __init__(self, characters: str, combinationLength: int):
        self.comb = self.combination(characters, combinationLength)
        self.idx = 0

    def combination(self, characters, length):
        comb = []
        ch_len = len(characters)
        for mask in range(2**ch_len - 1, 0, -1):  # bitmask 111, 110, 101, etc.
            binmask = format(mask, f'0{ch_len}b')
            c = ''
            for b, ch in zip(binmask, characters):
                if b == '1':
                    c += ch
            if len(c) == length:
                comb.append(c)
        return comb

    def next(self) -> str:
        self.idx += 1
        return self.comb[self.idx - 1]

    def hasNext(self) -> bool:
        return self.idx < len(self.comb)


ci = CombinationIterator3('gkosu', 3)
print(ci.comb)
# print(ci.next())
# print(ci.hasNext())
# print(ci.next())
# print(ci.hasNext())
# print(ci.next())
# print(ci.hasNext())

